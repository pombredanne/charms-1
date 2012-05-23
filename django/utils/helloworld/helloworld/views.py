import os

from django.template.response import TemplateResponse


def hello_world(request):
    return TemplateResponse(request, 'env.html', {'environ': os.environ})
