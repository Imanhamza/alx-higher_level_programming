#!/bin/bash
# Bash script to request a URL and display response body size
curl -sI "$1" | wc -c
