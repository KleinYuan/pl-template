build:
	docker build -t pl-template-docker .

run:
	sudo docker run -it \
        --runtime=nvidia \
        --name="pl-template-docker" \
        --net=host \
        --privileged=true \
        --ipc=host \
        --memory="10g" \
        --memory-swap="10g" \
        -v ${PWD}/src:/root/src \
      	pl-template-docker bash