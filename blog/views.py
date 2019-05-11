from django.http import HttpResponse
import datetime
from django.shortcuts import render

def post_list(request):
    return render(request, 'blog/post_list.html', {})

def current_datetime(request):
    now = datetime.datetime.now()
    html = "<html><body>It is now %s.</body></html>" % now
    return HttpResponse(html)