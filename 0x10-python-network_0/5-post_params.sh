#!/bin/bash
# sending POST request to url with parameters and display the body
curl -sX POST -d "email=test@gmail.com&subject=I will be here for PLD" "$1"
