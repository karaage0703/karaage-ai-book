#!/bin/bash

curl -sc /tmp/cookie "https://drive.google.com/uc?export=download&id=1M1qcogcN8NTCXoyEDRVoBfE7e5DxxN56" > /dev/null
CODE="$(awk '/_warning_/ {print $NF}' /tmp/cookie)"
curl -Lb /tmp/cookie "https://drive.google.com/uc?export=download&confirm=${CODE}&id=1M1qcogcN8NTCXoyEDRVoBfE7e5DxxN56" -o my_model_aug.h5

echo Download finished.

