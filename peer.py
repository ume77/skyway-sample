from util import do_get, do_post, do_delete
from config import EP_PEERS, EP_EVENTS


def call_post_peer(peer_id, app_key, app_host):
    path = EP_PEERS
    prm = {
      "key": app_key,
      "domain": app_host,
      "peer_id": peer_id,
      "turn": True,
      "credential": {
        "timestamp": 1582789414,
        "ttl": 3600,
        "authToken": "jfdcSAe2kaj/i7/IO5MEvJA7JecVimAOb48WgLhJux4="
      }
    }
    return do_post(path, prm)


def call_get_peers_events(peer_id, token):
    path = EP_PEERS + "/" + peer_id + "/" + EP_EVENTS + "?token=" + token
    prm = {}
    return do_get(path, prm)


def call_delete_peers(peer_id, token):
    path = EP_PEERS + "/" + peer_id + "?token=" + token
    prm = {}
    return do_delete(path, prm)


