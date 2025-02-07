#!/bin/bash
docker build -t curlreceiver .
docker run -p 8000:8000 curlreceiver