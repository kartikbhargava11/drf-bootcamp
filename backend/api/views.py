import json

from django.shortcuts import render
from django.http import JsonResponse


def api_home(request, *args, **kwargs):
    # request is instance of Django HttpRequest - Check Docs
    # dir(request)   
    body = request.body # byte string of JSON data
    data = {}
    try:
        data = json.loads(body) # takes string of JSON data and coverts it into a Python dictionary
    except:
        pass
    print(data)
    data["params"] = dict(request.GET)
    data['headers'] = dict(request.headers)
    data['content_type'] = request.content_type
    return JsonResponse(data)
