#!/bin/bash
# Sends DELETE request to URL passed as the first argument and displays the reponse body
curl -sX DELETE "$1"
