#!/usr/bin/env bash

cd "$(dirname "$PWD")"


uvicorn --host 0.0.0.0 --port 1701 --reload "main:app"