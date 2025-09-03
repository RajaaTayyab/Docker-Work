-------------------------------- Description --------------------------------
What happens when you try this and what is wrong with it? Next, how do you fix it?
Answer There is an extraneous semicolon in the Dockerfile



-------------------------------- Run instructions --------------------------------
> docker build -t testenv1 .
> docker run --rm -e ITEM=5 testenv1
