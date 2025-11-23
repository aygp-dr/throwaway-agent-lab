// Main thread - blocks until worker completes
function syncFetch(url) {
  const buffer = new SharedArrayBuffer(4);
  const signal = new Int32Array(buffer);
  const { port1, port2 } = new MessageChannel();
  
  worker.postMessage({ url, buffer, port: port2 }, [port2]);
  
  Atomics.wait(signal, 0, 0);  // Block!
  
  const result = receiveMessageOnPort(port1);
  port1.close();
  
  if (result.message.error) throw result.message.error;
  return result.message.data;
}

// Worker thread - performs async operation
onmessage = async ({ url, buffer, port }) => {
  const signal = new Int32Array(buffer);
  try {
    const data = await fetch(url).then(r => r.arrayBuffer());
    port.postMessage({ data: new Uint8Array(data) });
    Atomics.store(signal, 0, 1);
  } catch (error) {
    port.postMessage({ error });
    Atomics.store(signal, 0, -1);
  } finally {
    Atomics.notify(signal, 0);  // Wake main thread
    port.close();
  }
};
