APP=simulator

build:
	docker build . -t $(APP)

run:
	docker run -p 5000:5000 $(APP)

up: build run