init:
	pip3 install -r requirements.txt

update:
	pip install --upgrade Click Flask gunicorn itsdangerous MarkupSafe Jinja2 Werkzeug Pystarter
	pip freeze > requirements.txt

clean:
	pystarter clean

run: clean
	gunicorn run:app --reload