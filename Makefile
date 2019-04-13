all:im_bin ims_bin imr_bin 

dep:
	dep ensure -v

im_bin:
	cd src/im && make

ims_bin:
	cd src/ims && make

imr_bin:
	cd src/imr && make


build:all
	rm -rf ./bin && mkdir ./bin
	cp ./src/im/im ./bin
	cp ./src/ims/ims ./bin
	cp ./src/imr/imr ./bin

clean:
	rm -rf ./bin
	rm -f ./src/im/im  ./src/im/benchmark ./src/im/benchmark_group ./src/im/benchmark_connection ./src/im/benchmark_sender ./src/im/benchmark_storage ./src/im/benchmark_route ./src/ims/main.test ./src/ims/ims ./src/imr/imr
