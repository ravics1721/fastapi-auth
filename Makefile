

help:
	echo "\n \n*_*_*_*_ Usages Command _*_*_*_*_*_\n\n dev - Run app in dev mode\n";

env:
	poetry shell

setup: env
	poetry install

dev:
	uvicorn main:app --reload --port 8080