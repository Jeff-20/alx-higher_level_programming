#!/bin/bash
# This script takes a URL, sends a request to it, and displays the size of the response body
curl -sI "$1" | grep Content-Length | cut -d " " -f 2
