-------------------------------- Description --------------------------------
If you have a already running container that you need to pass a file to how can you send that file to it?



Answer:
docker cp <source> <container id> <destination>

docker cp config.json abc123:/app/config/
