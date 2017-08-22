build:

app:
	cd ./backend && python app.py

db:
	mongod --dbpath ./data/db