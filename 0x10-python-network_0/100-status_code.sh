#!/bin/bash
# Bash script for URL request and display of status code
curl -s -o /dev/null -Lw "%{http_code}\n" "$1"
