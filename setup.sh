#!/bin/bash
# Create project structure

mkdir -p {src,tests,docs,examples,notebooks}
mkdir -p src/{agent,sandbox,tools,utils}
mkdir -p tests/{unit,integration}

# Create placeholder files
touch src/agent/{loop.py,planner.py,executor.py}
touch src/sandbox/{pyodide_runtime.py,vfs.py,security.py}
touch src/tools/{describe.py,help.py,base.py}
touch src/utils/{cache.py,logging.py}

echo "Project structure created!"
