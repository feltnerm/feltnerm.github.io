#!/usr/bin/env bash

docker run -it --rm \
    -v $(pwd)/output:/usr/src/site/output \
    feltnerm.github.io
