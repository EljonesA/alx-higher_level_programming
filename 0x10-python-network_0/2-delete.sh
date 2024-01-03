#!/bin/bash
# script sends DELETE request to url, and displays body of reponse
curl -X DELETE -s "$1"
