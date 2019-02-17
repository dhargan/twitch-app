from django.shortcuts import render
from django.http import JsonResponse
from . import TWITCH_CREDENTIALS, TWITCH_ENDPOINTS
import requests
import json


def login_page(request):
    data = {
        'client_id': TWITCH_CREDENTIALS['CLIENT_ID'],
        'redirect_uri': TWITCH_CREDENTIALS['REDIRECT_URI'],
        'response_type': 'code',
        'scope': 'user:read:email',
        'code': request.GET.get('code', -1)
    }

    return render(request, 'login.html', data)

def twitch_auth(request):
    data = {
        'client_id': TWITCH_CREDENTIALS['CLIENT_ID'],
        'client_secret': TWITCH_CREDENTIALS['CLIENT_SECRET'],
        'redirect_uri': TWITCH_CREDENTIALS['REDIRECT_URI'],
        'code': request.POST.get('code', -1),
        'scope': request.POST.get('scope', ""),
        'grant_type': 'authorization_code'
    }

    response = requests.post(TWITCH_ENDPOINTS['authorization'], data)
    json_acceptable_string = response.text
    response = json.loads(json_acceptable_string)

    headers = {'Authorization': 'Bearer '+response['access_token']}
    response = requests.get(TWITCH_ENDPOINTS['users'], headers=headers)
    json_acceptable_string = response.text
    response = json.loads(json_acceptable_string)

    return JsonResponse(response)

def watch_stream(request):
    data = {
        'streamer': request.GET.get('streamer', '')
    }

    return render(request, 'stream.html', data)





