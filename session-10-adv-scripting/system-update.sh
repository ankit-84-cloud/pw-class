#!/bin/bash
echo "upaate packages"
sudo apt update -y
echo "upgrade packages"
sudo apt upgrade -y
echo "dist-upgrade packages"
sudo apt dist-upgrade -y
echo "autoremove packages"
sudo apt autoremove -y  