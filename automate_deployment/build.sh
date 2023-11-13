#!/bin/bash
docker login quay.io
docker build -t quay.io/olagoldhackxx/backend:v1 .
docker push quay.io/olagoldhackxx/backend:v1

