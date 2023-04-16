dev:
	docker exec -it -w /home/app $(shell docker compose ps -q base) /bin/sh

install:
	docker compose -f docker-compose.builder.yml build install

run:
	docker compose up -d

stop:
	docker compose down
