# Docker動作環境構築手順 (HBA版)

### ubuntuのイメージをpull
docker pull ubuntu18.04

### ubuntuのコンテナを起動(コンテナ名：ubuntu1804)
```
docker container run -it -d --name <conatiner-name> ubuntu:18.04
```

### ubuntuにrootでログイン
```
docker exec -it <conatiner-name> bash
```

### Proxyを環境変数に設定
```
export HTTP_PROXY="http://<host>:<port>/"
export HTTPS_PROXY="http://<host>:<port>/"
export http_proxy="http://<host>:<port>/"
export https_proxy="http://<host>:<port>/"
```

### aptパッケージを更新
```
apt update
apt -y upgarde
```

### タイムゾーンを設定
```
apt install tzdata
```

### nodejs関連
```
apt install -y nodejs
apt install -y build-essential
```

### npmのproxyのインストールとproxy設定
```
apt install -y npm
npm -g config set proxy http://<host>:<port>
npm -g config set https-proxy http://<host>:<port>
npm -g config set registry http://registry.npmjs.org/
```

### yarnのインストール
```
npm -g i yarn
```

### yarnのproxy設定
```
yarn config set proxy http://<host>:<port> -g
yarn config set https-proxy http://<host>:<port> -g
```

### gstreamer関連インストール
```
apt install -y libgstreamer1.0-0
apt install -y gstreamer1.0-dev
apt install -y gstreamer1.0-tools
apt install -y gstreamer1.0-doc
apt install -y gstreamer1.0-plugins-base
apt install -y gstreamer1.0-plugins-good
apt install -y gstreamer1.0-plugins-bad
apt install -y gstreamer1.0-plugins-ugly
apt install -y gstreamer1.0-libav
apt install -y gstreamer1.0-doc
apt install -y gstreamer1.0-tools
apt install -y gstreamer1.0-x
apt install -y gstreamer1.0-alsa
apt install -y gstreamer1.0-gl
apt install -y gstreamer1.0-gtk3
apt install -y gstreamer1.0-qt5
apt install -y gstreamer1.0-pulseaudio
apt install -y libgstreamer-plugins-base1.0-dev
apt install -y libopencv-dev
apt install -y yasm
```

### その他のツールのインストール
```
apt install -y net-tools
apt install -y vim
apt install -y sudo
apt install -y unzip
```

### wgetのインストールとproxy設定
```
apt install -y wget
```
コメントアウトされているので、有効にして編集
```
vi /etc/wgetrc
https_proxy = http://<host>:<port>/
http_proxy = http://<host>:<port>/
```

### WecRTC Gateway Server起動ファイルのインストール
```
wget https://github.com/skyway/skyway-webrtc-gateway/releases/download/0.2.1/gateway_linux_x64 --no-check-certificate
sudo mv ./gateway_linux_x64 /usr/local/bin
sudo chmod +x /usr/local/bin/gateway_linux_x64
```

### pipインストール
```
apt install -y python3-pip
```

### pipのproxy設定
```
mkdir ~/.pip
vi ~/.pip/pip.conf
```
以下の内容を記述
```
[global]
trusted-host = pypi.python.org
               pypi.org
               files.pythonhosted.org
```

### python関連インストール
```
pip3 install -U pip
pip3 install numpy
pip3 install opencv-contrib-python
pip3 install watchdog
pip3 install requests
```

### userを作成
```
useradd -d /home/user -s /bin/bash -m user
```

### userでログイン
```
docker exec -u user -w /home/user -it <conatiner-name> bash
```

### ~/.bashrcを編集
```
vi ~/.bashrc
```
以下を最後の行に追加
```
export HTTP_PROXY="http://<host>:<port>/"
export HTTPS_PROXY="http://<host>:<port>/"
export http_proxy="http://<host>:<port>/"
export https_proxy="http://<host>:<port>/"
```

### ~/.bashrcを反映
```
source ~/.bashrc
```

### ソースファイルのzipファイル(analyze-server.zip)をホストからDockerにアップロード
```
docker cp analyze-server.zip ubuntu1804:/home/user
```

### zipファイルを解凍
```
unzip analyze-server.zip
```

### node-skyway-rtcgw-libと*.shを~に移動
```
cd ~
mv analyze-server/home/node-skyway-rtcgw-lib .
mv analyze-server/home/*.sh .
```

### node_module.zipを解凍
```
cd node-skyway-rtcgw-lib
unzip node_modules.zip
```

### API KEYを書き換える
```
vi config.js
```
```js
api_key: '<Skywayで登録したAPIキー>'
```

### 現在のコンテナから新しいイメージを作成
```
docker ps -a
docker stop <container-id>
docker commit <container-id> <new-image-name>
```

### 新しいイメージで新しいコンテナを起動(9001ポートを公開する場合)
```
docker container run -p 9001:9001 -it -d --name <new-container-name> <new-image-name>:latest
```

### 新しいコンテナにuserでログイン
```
docker exec -u user -w /home/user -it <new-conatiner-name> bash
```

### プレゼンス推定システムを起動
```
sh ./run.sh
```

