import json
import sys
import time
from config import APP_KEY, APP_HOST, RECV_ADDR, VIDEO_RECV_PORT, AUDIO_RECV_PORT, VIDEO_RTCP_RECV_PORT, AUDIO_RTCP_RECV_PORT
from peer import call_post_peer, call_get_peers_events, call_delete_peers
from media import call_post_media, call_delete_media, call_post_media_rtcp, call_delete_media_rtcp
from media_channel import call_post_media_connections, call_get_media_connections_events, \
    call_delete_media_connections
from video_sender import video_sender


def scenario_media_caller(target_id):
    peer_id = ''
    token = ''
    video_id = ''
    audio_id = ''
    video_rtcp_id = ''
    audio_rtcp_id = ''
    media_connection_id = ''
    status, text = call_post_peer(peer_id, APP_KEY, APP_HOST)
    if status == 201:
        # PEERS_CREATE
        data = json.loads(text)
        peer_id = data['params']['peer_id']
        token = data['params']['token']
        status, text = call_get_peers_events(peer_id, token)
        if status == 200:
            # OPEN
            status, text = call_post_media(True)
            if status == 201:
                # Created
                data = json.loads(text)
                video_ip, video_id, video_port = (data['ip_v4'], data['media_id'], data['port'])
                status, text = call_post_media(False)
                if status == 201:
                    # Created
                    data = json.loads(text)
                    audio_ip, audio_id, audio_port = (data['ip_v4'], data['media_id'], data['port'])
                    status, text = call_post_media_rtcp()
                    if status == 201:
                        data = json.loads(text)
                        video_rtcp_id, video_rtcp_port = (data['rtcp_id'], data['port'])
                        status, text = call_post_media_rtcp()
                        if status == 201:
                            data = json.loads(text)
                            audio_rtcp_id, audio_rtcp_port = (data['rtcp_id'], data['port'])
                            video_redirect = [RECV_ADDR, VIDEO_RECV_PORT]
                            audio_redirect = [RECV_ADDR, AUDIO_RECV_PORT]
                            video_rtcp_redirect = [RECV_ADDR, VIDEO_RTCP_RECV_PORT]
                            audio_rtcp_redirect = [RECV_ADDR, AUDIO_RTCP_RECV_PORT]
                            status, text = call_post_media_connections(peer_id, token, target_id,
                                                                       video_id, video_rtcp_id, audio_id, audio_rtcp_id,
                                                                       video_redirect, audio_redirect,
                                                                       video_rtcp_redirect, audio_rtcp_redirect)
                            if status == 202:
                                # MEDIA_CONNECTION_CREATE
                                data = json.loads(text)
                                media_connection_id = data['params']['media_connection_id']
                                status, text = call_get_media_connections_events(media_connection_id)
                                if status == 200:
                                    # READY
                                    print("peer_id:", peer_id)
                                    print("target_id:", target_id)
                                    print("video_ip:", video_ip)
                                    print("audio_ip:", audio_ip)
                                    print("video_port:", video_port)
                                    print("audio_port:", audio_port)
                                    print("video_rtcp_port:", video_rtcp_port)
                                    print("audio_rtcp_port:", audio_rtcp_port)
                                    print("video_redirect_port:", VIDEO_RECV_PORT)
                                    print("audio_redirect_port:", AUDIO_RECV_PORT)
                                    print("video_redirect_rtcp_port:", VIDEO_RTCP_RECV_PORT)
                                    print("audio_redirect_rtcp_port:", AUDIO_RTCP_RECV_PORT)
                                    video_sender(video_ip, str(video_port))
                                    time.sleep(1000)

    if media_connection_id != '':
        call_delete_media_connections(media_connection_id)
    else:
        if audio_rtcp_id != '':
            call_delete_media_rtcp(audio_rtcp_id)
        if video_rtcp_id != '':
            call_delete_media_rtcp(video_rtcp_id)
        if audio_id != '':
            call_delete_media(audio_id)
        if video_id != '':
            call_delete_media(video_id)
    if token != '':
        call_delete_peers(peer_id, token)


if __name__ == '__main__':
    callee_id = sys.argv[1]
    print("callee_id:", callee_id)
    scenario_media_caller(callee_id)
