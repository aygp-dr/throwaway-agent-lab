import { test } from 'node:test';
import assert from 'node:assert';
import { loadPyodide } from 'pyodide';

test('Pyodide loads and runs basic python', async (t) => {
  const pyodide = await loadPyodide();
  const result = await pyodide.runPythonAsync('1 + 1');
  assert.strictEqual(result, 2);
});

test('Pyodide can import standard libraries', async (t) => {
  const pyodide = await loadPyodide();
  await pyodide.runPythonAsync('import json');
  const result = await pyodide.runPythonAsync('json.dumps({"a": 1})');
  assert.strictEqual(result, '{"a": 1}');
});
