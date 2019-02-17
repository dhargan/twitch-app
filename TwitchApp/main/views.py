from django.shortcuts import render
from django.http import JsonResponse
from . import TWITCH_CREDENTIALS, TWITCH_ENDPOINTS
import requests
import json


def login_page(request):
    """
    Login page which the user ser can login using Twitch API.
    If the login is successful, the user will be redirected with the authorization code.
    """
    data = {
        'client_id': TWITCH_CREDENTIALS['CLIENT_ID'],
        'redirect_uri': TWITCH_CREDENTIALS['REDIRECT_URI'],
        'response_type': 'code',
        'scope': '',
        'code': request.GET.get('code', -1)
    }

    return render(request, 'login.html', data)

def twitch_auth(request):
    """
    1) POST client id, client secret, redirect_uri, code, scope and grant type.
    2) Get response. If everything went well, take access_token and go the the next step. Otherwise, return empty JSON object
       # TODO: Using both access token AND refresh token should be a better idea
    3) GET user data by sending the access token via header.
    4) Build JSON object with the response and send it to the client.
    """
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

    try:
        access_token = response['access_token']

        headers = {'Authorization': 'Bearer '+access_token}
        response = requests.get(TWITCH_ENDPOINTS['users'], headers=headers)
        json_acceptable_string = response.text
        response = json.loads(json_acceptable_string)

        return JsonResponse(response)
    except KeyError:
        return JsonResponse({})

def watch_stream(request):
    """
    streamer: Login name of the selected streamer.
    client_id: Client id of our app.

    Both arguments are going to be used by the client side, in order to fetch streamer data.
    """
    data = {
        'streamer': request.GET.get('streamer', ''),
        'client_id': TWITCH_CREDENTIALS['CLIENT_ID']
    }

    return render(request, 'stream.html', data)





