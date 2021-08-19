#!/bin/bash
#script that takes in a URL and displays all HTTP methods the server will accept.
curl -X OPTIONS "$1" -i -s | grep Allow: | cut -b 8-
