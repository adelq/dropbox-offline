import requests

APP_KEY = "k8teuq593w8nqgz"
APP_SECRET = "5iwievofohddt69"

def app_key():
    return APP_KEY
    
def app_secret():
    return APP_SECRET
    
def request_oauth_token(APP_KEY, APP_SECRET):
    r = requests.post('https://api.dropbox.com/1/oauth/request_token', headers={'Authorization': 'OAuth oauth_version="1.0", oauth_signature_method="PLAINTEXT", oauth_consumer_key="%s", oauth_signature="%s&"' % (APP_KEY, APP_SECRET)})
    response = r._content
    oauth_token_secret = response.split('&')[0].split('=')[1]
    oauth_token = response.split('&')[1].split('=')[1]
    return oauth_token_secret, oauth_token
    
OAUTH_TOKEN = request_oauth_token(APP_KEY, APP_SECRET)[1]
OAUTH_TOKEN_SECRET = request_oauth_token(APP_KEY, APP_SECRET)[0]
    
def request_access_token(OAUTH_TOKEN, OAUTH_TOKEN_SECRET, APP_KEY, APP_SECRET):
    r = requests.post('https://api.dropbox.com/1/oauth/access_token', headers={'Authorization': 'OAuth oauth_version="1.0", oauth_signature_method="PLAINTEXT", oauth_consumer_key="%s", oauth_token="%s", oauth_signature="%s&%s"' % (APP_KEY, OAUTH_TOKEN, APP_SECRET, OAUTH_TOKEN_SECRET)})
    response = r._content
    access_token_secret = response.split('&')[0].split('=')[1]
    access_token = response.split('&')[1].split('=')[1]
    return access_token_secret, access_token
    
def get_file_data(OAUTH_TOKEN, OAUTH_TOKEN_SECRET, APP_KEY, APP_SECRET):
    r = requests.get('https://api.dropbox.com/1/metadata/sandbox/', headers={'Authorization': 'OAuth oauth_version="1.0", oauth_signature_method="PLAINTEXT", oauth_consumer_key="%s", oauth_token="%s, oauth_signature="%s&%s"' % (APP_KEY, OAUTH_TOKEN, APP_SECRET, OAUTH_TOKEN_SECRET)})
    return r._content
    
def get_file(path, OAUTH_TOKEN, OAUTH_TOKEN_SECRET, APP_KEY, APP_SECRET):
    r = requests.get('https://api-content.dropbox.com/1/files/sandbox/%s' % path , headers={'Authorization': 'OAuth oauth_version="1.0", oauth_signature_method="PLAINTEXT", oauth_consumer_key="%s", oauth_token="%s", oauth_signature="%s&%s"' % (APP_KEY, OAUTH_TOKEN, APP_SECRET, OAUTH_TOKEN_SECRET)})
    return r._content