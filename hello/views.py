from django.http import HttpResponse
import logging

logger = logging.getLogger(__name__)


# Create your views here.

def helloworld(request):
    logging.error('Hello world DJ4E in the log...')
    print('Hello world f231f210 DJ4E in a print statement...')

    visits = request.session.get('visits', 0) + 1
    request.session['visits'] = visits
    if visits > 3:
        del (request.session['visits'])

    response = """<html><body><p>f231f210 Hello world DJ4E in HTML</p>
    
    <p>view count = """+str(visits)+"""</p>
    </body></html>"""
    resp = HttpResponse(response)
    resp.set_cookie('dj4e_cookie', 'f231f210', max_age=1000)
    return resp
