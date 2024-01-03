#!/bin/bash
# sending GET request to url with specified custom header
curl -sH "X-School-User-Id: 98" "$1"
