#!/usr/bin/env bash
sudo apt update && sudo apt install pulseaudio pulseaudio-module-zeroconf -y
echo "load-module module-native-protocol-tcp auth-ip-acl=127.0.0.1;172.23.100.0/24" | sudo tee -a /etc/pulse/system.pa.d/soundViaLAN.pa
echo "load-module module-zeroconf-publish" | sudo tee -a /etc/pulse/system.pa.d/soundViaLAN.pa
sudo cp pulseaudio.service /etc/systemd/system/pulseaudio.service
systemctl --user mask pulseaudio.socket
systemctl --user disable pulseaudio.service
sudo systemctl enable --now pulseaudio
sudo systemctl start pulseaudio

