#!/bin/bash
# Sends a POST request to the passed URL, and displays the response body
curl -sd "email=test@gmail.com&subject=I will always be here for PLD" -X POST "$1"
