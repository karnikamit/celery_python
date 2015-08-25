__author__ = 'karnikamit'
from celery import Celery

app = Celery('tasks', broker='amqp://guest@localhost//', backend='amqp')
# app['CELERY_RESULT_BACKEND'] = 'amqp'