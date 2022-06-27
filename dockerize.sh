#!/bin/bash
#APP
docker build -f ./app.Dockerfile -t joshwill/scratch_api:latest .
docker tag joshwill/scratch_api:latest
docker push joshwill/scratch_api:latest

#Databse
docker build -f ./app.Dockerfile -t joshwill/scratch_db:latest .
docker tag joshwill/scratch_db:latest
docker push joshwill/scratch_db:latest