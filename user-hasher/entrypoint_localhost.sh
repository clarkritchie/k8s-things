#!/usr/bin/env bash

set -e

cat << EOF >> /etc/bash.bashrc
alias ls='ls -la'
EOF

echo "Starting app..."
uvicorn src.main:app --host 0.0.0.0 --proxy-headers --port 8000 --reload --use-colors