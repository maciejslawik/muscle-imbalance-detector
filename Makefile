install:
	git clone git@github.com:CMU-Perceptual-Computing-Lab/openpose.git openpose
	git clone git@github.com:CMU-Perceptual-Computing-Lab/caffe.git openpose/3rdparty/caffe/
	git clone git@github.com:pybind/pybind11.git openpose/3rdparty/pybind11/

build:
	cd openpose/build
	make -j `nproc`