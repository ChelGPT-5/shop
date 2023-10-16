import time

from celery import shared_task

@shared_task
def some_task():
    time.sleep(5)
    return 'text1234'

@shared_task
def some_schedule_task():
    return 'text4321'