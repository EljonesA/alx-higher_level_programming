#!/bin/bash
# script that checks and displays allowed methods of a url
curl -sI "$1" | grep Allow | cut -c 8-
