APP=simulator

build:
	docker build . -t $(APP)

run:
	docker run -p 5000:5000 $(APP)


up: build run

compose-build:
	docker-compose build

compose-up:
	docker-compose up

compose: compose-build compose-up