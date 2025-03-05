#!/usr/bin/env bash
sudo apt update && sudo apt install pulseaudio -y
echo "load-module module-native-protocol-tcp auth-ip-acl=127.0.0.1;172.23.100.0/24" | sudo tee -a /etc/pulse/default.pa

