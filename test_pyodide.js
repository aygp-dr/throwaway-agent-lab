import { loadPyodide } from "pyodide";

async function test() {
  try {
    console.log("Loading Pyodide...");
    const pyodide = await loadPyodide();
    console.log("Running Python...");
    const result = await pyodide.runPythonAsync("import sys; print(sys.version); 1 + 1");
    console.log("Pyodide Result:", result);
    console.log("Pyodide works!");
  } catch (e) {
    console.error("Pyodide failed:", e);
    process.exit(1);
  }
}

test();
