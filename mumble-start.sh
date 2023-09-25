#!/usr/bin/env bash


PWD=$(dirname "$(readlink -f $0)")

mumble 2>/dev/null >&2 &
echo "Starting mumble-keys.py. Enter sudo password is needed."
sudo "${PWD}/venv/bin/python" "${PWD}/mumble-keys.py"
