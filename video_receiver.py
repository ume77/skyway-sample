import subprocess
import sys

"""
  const caps= [
    "application/x-rtp",
    "media=(string)video",
    "clock-rate=(int)90000",
    "encoding-name=(string)H264"
  ].join(',');

  const script = [
    `udpsrc port=${port} caps=${caps}`,
    'queue',
    'rtph264depay',
    'avdec_h264',
    'videoconvert',
    'jpegenc',
    'appsink max-buffers=1 name=sink'
  ].join(" ! ");
"""


def video_receiver(video_redirect_port):
    cmd = 'gst-launch-1.0' \
          ' udpsrc port=' + video_redirect_port + \
          ' caps="application/x-rtp,payload=(int)100"' \
          ' ! rtpjitterbuffer latency=500' \
          ' ! rtph264depay' \
          ' ! avdec_h264 output-corrupt=false' \
          ' ! videoconvert' \
          ' ! fpsdisplaysink sync=false'

    subprocess.call(cmd, shell=True)


if __name__ == '__main__':
    # test example "20000"
    port = sys.argv[1]
    print(port)
    video_receiver(port)
