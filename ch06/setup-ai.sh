#!/bin/bash
# Raspberry OS with desktop 2020-05-27
# Reference:
# https://qiita.com/masaru/items/658b24b0806144cfeb1c

# install apt-get package
apt_get_install(){
	sudo apt-get update
	# sudo apt-get install -y libhdf5-dev libhdf5-serial-dev libhdf5-100
	sudo apt-get install -y libhdf5-dev libhdf5-103
	sudo apt-get install -y libqtgui4 libqtwebkit4 libqt4-test python3-pyqt5
	sudo apt-get install -y libatlas-base-dev
	sudo apt-get install -y libjasper-dev
}

install_tensorflow(){
	sudo pip3 install -U pip
	sudo pip3 install -U setuptools
	sudo pip3 install wrapt --upgrade --ignore-installed
	sudo pip3 install --default-timeout=1000 tensorflow==1.14.0
	sudo apt-get install -y python3-h5py
}

install_opencv(){
	sudo pip3 --default-timeout=1000 install opencv-python==3.4.6.27
}

START_TIME=`date +%s`

# change directory here
cd `dirname $0`

apt_get_install
install_tensorflow
install_opencv

END_TIME=`date +%s`

SS=`expr ${END_TIME} - ${START_TIME}`
HH=`expr ${SS} / 3600`
SS=`expr ${SS} % 3600`
MM=`expr ${SS} / 60`
SS=`expr ${SS} % 60`

echo "Total Time: ${HH}:${MM}:${SS} (h:m:s)"
