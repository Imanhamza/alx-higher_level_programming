#!/bin/bash
# Bash script for URL POST request and response display
curl -sX "PUT" -d "email=test@gmail.com&subject=I will always be here for PLD" "$1"
