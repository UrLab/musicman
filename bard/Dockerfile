FROM debian:bookworm

RUN apt update 
RUN apt upgrade -y
RUN apt install -y wget apt-utils alsa-utils pulseaudio mpc
RUN apt install -y \
    gir1.2-gst-plugins-base-1.0 \
    gir1.2-gstreamer-1.0 \
    gstreamer1.0-plugins-good \
    gstreamer1.0-plugins-bad \
    gstreamer1.0-plugins-ugly \
    gstreamer1.0-alsa \
    gstreamer1.0-pulseaudio \
    gstreamer1.0-libav \
    gstreamer1.0-tools \
    libcairo2-dev \
    libgirepository1.0-dev \
    python3-gst-1.0

RUN mkdir -p /etc/apt/keyrings
RUN wget -q -O /etc/apt/keyrings/mopidy-archive-keyring.gpg https://apt.mopidy.com/mopidy-archive-keyring.gpg
RUN wget -q -O /etc/apt/sources.list.d/mopidy.sources https://apt.mopidy.com/bookworm.sources

RUN apt update && apt install -y mopidy mopidy-mpd python3 python3-pip
RUN python3 -m pip install Mopidy-Iris --break-system-packages

RUN usermod -a -G audio mopidy

CMD ["mopidy", "--config", "/config/mopidy.conf"]

