from celery.task import task, periodic_task

from .utils import create_pdf

@task(name='create_pdf')
def create_pdf_task(url):
    return create_pdf(url)