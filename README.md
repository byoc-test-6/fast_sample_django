# Server

python manage.py runserver

# Worker

celery -A fast_sample_django.tasks worker --loglevel=INFO 

# Required environment variables

* AWS_REGION
* SQS_URL