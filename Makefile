wait:
	python3 -c "import time; time.sleep(3)"

local_migrate:
	docker-compose -f docker-compose-local.yml up -d backend
	make wait
	docker exec -t codefather.dev-backend python3 /app/manage.py makemigrations
	docker exec -t codefather.dev-backend python3 /app/manage.py migrate

local_create_superuser:
	docker-compose -f docker-compose-local.yml up -d backend

local_collect_static:
	docker-compose -f docker-compose-local.yml up -d backend
	docker exec -t codefather.dev-backend python3 manage.py collectstatic --noinput

local_build:
	docker-compose -f docker-compose-local.yml build --no-cache
	make wait

	make local_migrate
	#make create_superuser

	make local_collect_static
	docker-compose -f docker-compose-local.yml down

local_up:
	docker-compose -f docker-compose-local.yml up

local_down:
	docker-compose -f docker-compose-local.yml down