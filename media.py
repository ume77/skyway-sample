from util import do_get, do_post, do_put, do_delete
from config import EP_MEDIA, EP_RTCP


def call_post_media(is_video):
    path = EP_MEDIA
    prm = {
      "is_video": is_video
    }
    return do_post(path, prm)


def call_delete_media(media_id):
    path = EP_MEDIA + "/" + media_id
    prm = {}
    return do_delete(path, prm)


def call_post_media_rtcp():
    path = EP_MEDIA + "/" + EP_RTCP
    prm = {}
    return do_post(path, prm)


def call_delete_media_rtcp(rtcp_id):
    path = EP_MEDIA + "/" + EP_RTCP + "/" + rtcp_id
    prm = {}
    return do_delete(path, prm)

