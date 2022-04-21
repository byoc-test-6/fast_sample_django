from django.http import HttpResponse


def health(request):
    return HttpResponse("Hello, world. You're at the polls index.")


def run_task(request):
    from fast_sample_django.tasks import add
    add.delay(4, 4)
    return HttpResponse("Submitted task")

