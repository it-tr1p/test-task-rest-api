up:
	docker-compose -f docker-compose-local.yaml up -d
down:
	docker-compose -f docker-compose-local.yaml down && docker network prune --force

generate:
	alembic revision --m="$(NAME)" --autogenerate
migrate:
	alembic upgrade head