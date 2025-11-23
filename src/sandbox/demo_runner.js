import { loadPyodide } from "pyodide";
import fs from "fs/promises";
import path from "path";

async function setupPyodide() {
  const pyodide = await loadPyodide();
  
  // Install micropip to handle package installation
  await pyodide.loadPackage("micropip");
  const micropip = pyodide.pyimport("micropip");
  
  // Install common "tools"
  console.log("📦 Installing libraries (qrcode, Faker)...");
  await micropip.install(["qrcode", "Faker", "pillow"]); 
  console.log("✅ Libraries installed.");
  
  return pyodide;
}

async function runScript(scriptPath) {
  const pyodide = await setupPyodide();
  
  console.log(`\n🚀 Running ${path.basename(scriptPath)}...`);
  const code = await fs.readFile(scriptPath, "utf-8");
  
  // Mount a virtual directory for output
  pyodide.FS.mkdir("/output");
  
  try {
    // Run the code
    await pyodide.runPythonAsync(code);
    
    // Check for outputs
    const files = pyodide.FS.readdir("/output");
    console.log("\n📂 Output files in /output:");
    for (const file of files) {
      if (file !== "." && file !== "..") {
        console.log(` - ${file}`);
        // Read binary data if it's an image
        if (file.endsWith('.png')) {
             const content = pyodide.FS.readFile("/output/" + file);
             console.log(`   (Wrote ${content.length} bytes to virtual FS)`);
        }
      }
    }
  } catch (e) {
    console.error("❌ Error running script:", e);
  }
}

// CLI arg
const script = process.argv[2];
if (script) {
  runScript(script);
} else {
  console.log("Usage: node src/sandbox/demo_runner.js <path_to_python_script>");
}
