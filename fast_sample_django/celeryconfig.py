import os

broker_url = "sqs://"
task_serializer = 'json'
task_default_queue = 'default'
broker_transport_options = {
    "region": os.getenv('AWS_REGION'),
    "visibility_timeout": 30,
    'predefined_queues': {
        'default': {
            'url': os.getenv('SQS_URL'),
        }
    }
}