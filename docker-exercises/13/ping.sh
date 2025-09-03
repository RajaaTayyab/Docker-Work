#!/bin/sh
httpd -f -p 8080 &

while true ; do
    echo "Ping"
    sleep 1
    curl -s ping :8000
done
