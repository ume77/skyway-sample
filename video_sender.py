import subprocess
import sys


def video_sender(video_host, video_port):
    cmd = 'gst-launch-1.0' \
          ' autovideosrc name=src0' \
          ' ! video/x-raw,width=640,height=480' \
          ' ! videoconvert' \
          ' ! x264enc bitrate=90000' \
          ' pass=quant' \
          ' quantizer=25' \
          ' rc-lookahead=0' \
          ' sliced-threads=true' \
          ' speed-preset=superfast' \
          ' sync-lookahead=0' \
          ' tune=zerolatency' \
          ' ! rtph264pay pt=100 mtu=1400 config-interval=3' \
          ' ! udpsink port=' + video_port + ' host=' + video_host + ' sync=false'

    subprocess.call(cmd, shell=True)


if __name__ == '__main__':
    # test example "127.0.0.1:50001"
    host_port = sys.argv[1].split(':')
    print(host_port[0])
    print(host_port[1])
    video_sender(host_port[0], host_port[1])
