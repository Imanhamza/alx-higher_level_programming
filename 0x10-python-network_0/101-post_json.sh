#!/bin/bash
# Bash script for JSON POST request, display response body
curl -sX POST -H "Content-Type: application/json" -d "@$2" "$1"
