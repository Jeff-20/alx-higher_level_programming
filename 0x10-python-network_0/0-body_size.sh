#!/bin/bash
# This script takes a URL, sends a request to it,
# and displays the sze of the body of the response

curl -sI "$1" | grep Content-Length | cut -d " " -f 2
