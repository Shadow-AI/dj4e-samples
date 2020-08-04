from django.http import HttpResponse
import logging

logger = logging.getLogger(__name__)


# Create your views here.

def helloworld(request):
    logging.error('Hello world DJ4E in the log...')
    print('Hello world DJ4E in a print statement...')
    response = """<html><body><p>Hello world DJ4E in HTML</p>
    <p>This sample code is available at
    <a href="https://github.com/csev/dj4e-samples">
    https://github.com/csev/dj4e-samples</a></p>
    </body></html>"""
    resp=HttpResponse(response)
    resp.set_cookie('dj4e_cookie', 'f231f210', max_age=1000)
    return resp
