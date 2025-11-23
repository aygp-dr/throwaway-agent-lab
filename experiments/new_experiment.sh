#!/bin/bash

if [ -z "$1" ]; then
  echo "Usage: $0 <experiment-slug>"
  echo "Example: $0 vfs-performance-bench"
  exit 1
fi

SLUG=$1
EXPERIMENTS_DIR="experiments"

# Find the next available number
LAST_NUM=$(find $EXPERIMENTS_DIR -maxdepth 1 -name "[0-9][0-9][0-9]-*" | sort | tail -n 1 | grep -oE "^$EXPERIMENTS_DIR/[0-9]+" | grep -oE "[0-9]+$")
if [ -z "$LAST_NUM" ]; then
  NEXT_NUM="001"
else
  NEXT_NUM=$(printf "%03d" $((10#$LAST_NUM + 1)))
fi

DIR_NAME="${NEXT_NUM}-${SLUG}"
FULL_PATH="${EXPERIMENTS_DIR}/${DIR_NAME}"

mkdir -p "$FULL_PATH"

# Create template README
cat > "$FULL_PATH/README.org" <<EOF
#+TITLE: Experiment ${NEXT_NUM}: ${SLUG}
#+DATE: $(date +%Y-%m-%d)
#+STATUS: In Progress

* Goal
Describe what you are trying to test or prove.

* Hypothesis
I believe that [doing X] will result in [Y].

* Method
1. Step 1
2. Step 2

* Results
(To be filled after execution)

* Conclusion
(Success/Failure/Next Steps)
EOF

echo "Created new experiment: $FULL_PATH"
echo "Usage: cd $FULL_PATH && emacs README.org"
