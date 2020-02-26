setup:
	@pip install -r requirements.txt

build:
	@python manage.py migrate
	@python manage.py runserver