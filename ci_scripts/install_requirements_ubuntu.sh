#!/usr/bin/env bash

sudo apt-get update && sudo apt-get install --no-install-recommends -y \
    curl \
    zip \
    g++ \
    make \
    ninja-build \
    libxml2-dev \
    libxml2-utils \
    libxslt1-dev \
    libarchive-dev \
    libssl-dev \
    libcurl4-openssl-dev \
    cpio \
    man \
    file \
    dpkg-dev
