all:
	cd src/im && make
	cd src/ims && make
	cd src/imr && make

dep:
	dep ensure -v

install:all
	rm -rf ./bin && mkdir ./bin
	cp ./src/im/im ./bin
	cp ./src/ims/ims ./bin
	cp ./src/imr/imr ./bin

clean:
	rm -f ./src/im/im  ./src/im/benchmark ./src/im/benchmark_group ./src/im/benchmark_connection ./src/im/benchmark_sender ./src/im/benchmark_storage ./src/im/benchmark_route ./src/ims/main.test ./src/ims/ims ./src/imr/imr

distclean: clean
	rm -rf bin
	rm -rf var

test:
	py.test -v ./tests

init:
	mkdir -p ./runtime/log/ims
	mkdir -p ./runtime/log/imr
	mkdir -p ./runtime/log/im
	mkdir -p ./runtime/tmp/im
	mkdir -p ./runtime/tmp/pending

start: init
	honcho start
