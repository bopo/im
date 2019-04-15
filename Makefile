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

clean-build:
	rm -fr build/
	rm -fr dist/
	rm -fr bin/
	rm -fr .eggs/
	rm -rf '*.tgz'
	find . -name '*.egg-info' -exec rm -fr {} +
	find . -name '*.egg' -exec rm -f {} +
	find . -name '*.log' -exec rm -f {} +
	find . -name '*.sql' -exec rm -f {} +

clean-others:
	rm -fr runtime/**/**
	rm -rf celerybeat-schedule
	rm -rf dump.rdb
	find . -name 'Thumbs.db' -exec rm -f {} +
	find . -name '*.tgz' -exec rm -f {} +
	find . -name 'dump.rdb' -exec rm -f {} +
	find . -name 'celery*.db' -exec rm -f {} +

clean-pyc:
	find . -name '*.pyc' -exec rm -f {} +
	find . -name '*.pyo' -exec rm -f {} +
	find . -name '*~' -exec rm -f {} +
	find . -name '__pycache__' -exec rm -fr {} +

clean-test:
	rm -rf nosetests.html
	rm -rf .coverage
	rm -rf htmlcov/
	rm -rf reports/
	rm -rf .tox/

distclean: clean clean-build clean-others clean-test clean-pyc
	rm -rf bin
	rm -rf runtime

clean_log:
	rm -rf runtime/log/**/*

test:
	py.test -v ./tests

init:
	mkdir -p ./runtime/log/ims
	mkdir -p ./runtime/log/imr
	mkdir -p ./runtime/log/im
	mkdir -p ./runtime/tmp/im
	mkdir -p ./runtime/tmp/pending

stop:
	killall im
	killall ims
	killall imr

start: init
	honcho start
