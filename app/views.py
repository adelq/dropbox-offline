from django.shortcuts import render_to_response
from django.http import HttpResponse, HttpResponseRedirect
import api
import json
import base64

class File:
    def __init__(self, filename, size, date_modified):
        self.filename = filename
        self.size = size
        self.date_modified = date_modified

def welcome(request):
    return initialize(request)
    
def initialize(request):
    request.session['app_key'] = api.app_key()
    request.session['app_secret'] = api.app_secret()
    tokens = api.request_oauth_token(request.session['app_key'], request.session['app_secret'])
    request.session['oauth_token'] = oauth_token = tokens[1]
    request.session['oauth_token_secret'] = oauth_token_secret = tokens[0]
    return HttpResponseRedirect('https://www.dropbox.com/1/oauth/authorize?oauth_token=%s&oauth_callback=http://project-livec9fd0cdb8477.rhcloud.com/almost' % oauth_token)
    
def check(request):
    data = api.get_file_data(request.session['access_token'], request.session['access_token_secret'], request.session['app_key'], request.session['app_secret'])
    return HttpResponse(data)

def almost(request):
    tokens = api.request_access_token(request.session['oauth_token'], request.session['oauth_token_secret'], request.session['app_key'], request.session['app_secret'])
    request.session['access_token'] = tokens[1]
    request.session['access_token_secret'] = tokens[0]
    return HttpResponseRedirect('/done')
    
def done(request):
    list_of_file_objects = []
    request.session['AUTHENTICATED'] = True
    dictionary = json.loads(api.get_file_data(request.session['access_token'], request.session['access_token_secret'], request.session['app_key'], request.session['app_secret']))
    file_list = dictionary['contents']
    for file in file_list:
        f = File(filename=file['path'], size=file['bytes'], date_modified=file['modified'])
        f.content = base64.b64encode(api.get_file(f.filename, request.session['access_token'], request.session['access_token_secret'], request.session['app_key'], request.session['app_secret']))
        list_of_file_objects.append(f)
    return render_to_response('file_list.html', {'files': list_of_file_objects})

