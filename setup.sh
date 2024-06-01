#!/bin/sh

apt-get update -y
apt-get upgrade -y
apt-get install nano -y


chmod +x edit-xmrig
chmod +x run-xmrig
chmod +x update
chmod +x ANSI_Shadow.flf
chmod +x backup
chmod +x restore
chmod +x install.txt

apt-get install python3 -y
apt-get install pip -y
apt-get install wget -y
apt-get install figlet -y
apt-get install python3-progress -y
apt-get install python3-requests -y

mv edit-xmrig ../../bin
mv run-xmrig ../../bin
mv update ../../bin
mv ANSI_Shadow.flf ../../usr/share/figlet
mv backup /data/data/com.termux/files/usr/bin
mv restore /data/data/com.termux/files/usr/bin
mv install.txt /storage/emulated/0/download

chmod +x miner

cd && cd ../etc
nano bash.bashrc

run-xmrig
