#!/bin/bash
# Bash script to trigger server response with 'You got me!
curl -so /dev/null -Lw "You got me!" "0.0.0.0:5000/catch_me"
