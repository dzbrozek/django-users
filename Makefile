.PHONY : shell build up bootstrap down removevolumes mypy test managepy precommit testci migrate makemigrations bash

build:
	docker build -t django-users \
	--build-arg USER_ID=$(shell id -u) \
	--build-arg GROUP_ID=$(shell id -g) \
	$(arguments) .
up:
	docker-compose up -d $(arguments)
bootstrap: down removevolumes
	docker-compose run --rm backend bootstrap
	make up
down:
	docker-compose down --remove-orphans
removevolumes: down
	-docker volume rm `docker volume ls -f name=django-users -q|grep -v "pycharm"`
mypy:
	docker-compose exec -T backend mypy --config-file ../mypy.ini ./
test:
	docker-compose exec backend python manage.py test $(arguments) --verbosity 3 --parallel
migrate:
	docker-compose exec -T backend python manage.py migrate
makemigrations:
	docker-compose exec -T backend python manage.py makemigrations
shell:
	docker-compose exec backend python manage.py shell_plus
bash:
	docker-compose exec backend bash
managepy:
	docker-compose exec -T backend python manage.py $(arguments)
precommit:
	pre-commit run --all-files
