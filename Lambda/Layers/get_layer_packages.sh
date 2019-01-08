#!/bin/bash

export PKG_DIR="SLS-Serverless-layer/python"

rm -rf ${PKG_DIR} && mkdir -p ${PKG_DIR}

docker run --rm -v $(pwd):/foo -w /foo lambci/lambda:build-python3.6 \
    pip install -r requirements.txt --no-deps -t ${PKG_DIR}

cp common.py ${PKG_DIR}
