#!/usr/bin/env bash

process_ids=$(ps -ef | grep "python" | grep -v "grep" | grep -v "$0" | awk '{print $2}')

if [[ -n $process_ids ]]; then
    echo "Stopping all Python processes..."
    for pid in $process_ids; do
        echo "Killing process ID: $pid"
        kill -9 $pid
    done
    echo "All Python processes have been stopped."
else
    echo "No Python processes found."
fi