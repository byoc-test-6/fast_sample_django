from celery import Celery

app = Celery('tasks')
app.config_from_object('fast_sample_django.celeryconfig')


@app.task
def add(x, y):
    return x + y