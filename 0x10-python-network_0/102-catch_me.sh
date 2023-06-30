#!/bin/bash
# Bash script to trigger server response with 'You got me!
curl -so /dev/null -w "You got me!" -X PUT "0.0.0.0:5000/catch_me"
