#!/bin/bash
# Takes a URL as a argument, sends a GET request to the URL, and displays the reponse body
curl -sH "X-School-User-Id=98" "$1" 
