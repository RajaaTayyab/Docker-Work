#!/bin/sh
httpd -f -p 8080 &
while true ; do
    echo "Pong"
    sleep 1
    curl -s pong :8000
done
