#!/usr/bin/env bash
cd bard
mkdir -p music
docker-compose up --build -d
cd ../soundViaLAN
./soundViaLAN.sh
cd ../UrSongDownloader
mkdir -p music
docker-compose up --build -d

