#!/usr/bin/env bash
mkdir -p music
cd bard
docker-compose up --build -d
cd ../soundViaLAN
./soundViaLAN.sh
cd ../UrSongDownloader
docker-compose up --build -d

