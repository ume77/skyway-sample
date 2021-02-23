import requests
import json
from config import GW_SCHEME, GW_HOST, GW_PORT


METHOD_GET = 'get'
METHOD_POST = 'post'
METHOD_PUT = 'put'
METHOD_DELETE = 'delete'


def call_api(method, path, prm):
    url = GW_SCHEME + "://" + GW_HOST + ":" + GW_PORT + "/" + path
    print("method:", method)
    print("url:", url)
    print("prm:", prm)
    if method == METHOD_GET:
        r = requests.get(url, prm, timeout=1000)
    elif method == METHOD_POST:
        r = requests.post(url, json.dumps(prm))
    elif method == METHOD_PUT:
        r = requests.put(url, prm)
    elif method == METHOD_DELETE:
        r = requests.delete(url)
    status = r.status_code
    text = r.text
    print("status:", status)
    print("text:", text)
    return status, text


def do_get(path, prm):
    return call_api(METHOD_GET, path, prm)


def do_post(path, prm):
    return call_api(METHOD_POST, path, prm)


def do_put(path, prm):
    return call_api(METHOD_PUT, path, prm)


def do_delete(path, prm):
    return call_api(METHOD_DELETE, path, prm)
