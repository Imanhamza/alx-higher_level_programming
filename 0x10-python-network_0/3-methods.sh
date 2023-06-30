#!/bin/bash
# Bash script to display accepted HTTP methods of a URL
curl -sI "$1" | grep "Allow" | cut -d ' ' -f2-
