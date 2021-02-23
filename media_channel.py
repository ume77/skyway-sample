from util import do_get, do_post, do_delete
from config import EP_MEDIA, EP_CONNECTIONS, EP_EVENTS, EP_ANSWER


def call_post_media_connections(peer_id, token, target_id, video_id, video_rtcp_id, audio_id, audio_rtcp_id,
                                                                       video_redirect, audio_redirect,
                                                                       video_rtcp_redirect, audio_rtcp_redirect):
    path = EP_MEDIA + "/" + EP_CONNECTIONS
    constraints = create_constraints(video_id, audio_id, video_rtcp_id, audio_rtcp_id)
    redirect_params = create_redirect_params(video_redirect, audio_redirect, video_rtcp_redirect, audio_rtcp_redirect)
    prm = {
        "peer_id": peer_id,
        "token": token,
        "target_id": target_id,
        "constraints": constraints,
        "redirect_params": redirect_params,
    }
    return do_post(path, prm)


def call_post_media_connections_answer(media_connection_id, video_id, audio_id, video_rtcp_id, audio_rtcp_id,
                                       video_redirect, audio_redirect,
                                       video_rtcp_redirect, audio_rtcp_redirect):
    path = EP_MEDIA + "/" + EP_CONNECTIONS + "/" + media_connection_id + "/" + EP_ANSWER
    constraints = create_constraints(video_id, audio_id, video_rtcp_id, audio_rtcp_id)
    redirect_params = create_redirect_params(video_redirect, audio_redirect, video_rtcp_redirect, audio_rtcp_redirect)
    prm = {
        "constraints": constraints,
        "redirect_params": redirect_params,
    }
    return do_post(path, prm)


def call_get_media_connections_events(media_connection_id):
    path = EP_MEDIA + "/" + EP_CONNECTIONS + "/" + media_connection_id + "/" + EP_EVENTS
    prm = {}
    return do_get(path, prm)


def call_delete_media_connections(media_connection_id):
    path = EP_MEDIA + "/" + EP_CONNECTIONS + "/" + media_connection_id
    prm = {}
    return do_delete(path, prm)


def create_redirect_params(video_redirect, audio_redirect, video_rtcp_redirect, audio_rtcp_redirect):
    redirect_params = {
        "video": {
            "ip_v4": video_redirect[0],
            "port": video_redirect[1],
        },
        "audio": {
            "ip_v4": audio_redirect[0],
            "port": audio_redirect[1],
        },
        "video_rtcp": {
            "ip_v4": video_rtcp_redirect[0],
            "port": video_rtcp_redirect[1],
        },
        "audio_rtcp": {
            "ip_v4": audio_rtcp_redirect[0],
            "port": audio_rtcp_redirect[1],
        }
    }
    return redirect_params


def create_constraints(video_id, video_rtcp_id, audio_id, audio_rtcp_id):
    constraints = {
        "video": True,
        "videoReceiveEnabled": True,
        "audio": True,
        "audioReceiveEnabled": True,
        "video_params": {
            "band_width": 0,
            "codec": "H264",
            "media_id": video_id,
            "rtcp_id": video_rtcp_id,
            "payload_type": 100,
            "sampling_rate": 90000
        },
        "audio_params": {
            "band_width": 0,
            "codec": "OPUS",
            "media_id": audio_id,
            "rtcp_id": audio_rtcp_id,
            "payload_type": 111,
            "sampling_rate": 48000
        },
        "metadata": {}
    }

    #     "video": True,
    #     "videoReceiveEnabled": True,
    #     "audio": True,
    #     "audioReceiveEnabled": True,
    #     "video_params": {
    #         "band_width": 1500,
    #         "codec": "H264",
    #         "media_id": video_id,
    #         "rtcp_id": video_rtcp_id,
    #         "payload_type": 100,
    #     },
    #     "audio_params": {
    #         "band_width": 1500,
    #         "codec": "opus",
    #         "media_id": audio_id,
    #         "rtcp_id": audio_rtcp_id,
    #         "payload_type": 111,
    #     }
    return constraints
