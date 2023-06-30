#!/bin/bash
# Bash script for URL request and display of status code
curl -so /dev/null -w "%{http_code}\n" "$1"
