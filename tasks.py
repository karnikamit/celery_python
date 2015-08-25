__author__ = 'karnikamit'
from celery_server import app

@app.task
def add(x, y):
    return x + y