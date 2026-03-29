#!/bin/bash

DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" && pwd )"

cd "$DIR"

COMMAND="docker compose"

echo "Running Pulsar with $COMMAND from $DIR..."

sudo mkdir -p ./data/zookeeper ./data/bookkeeper
sudo chown -R 10000 data

docker exec -it broker bash bin/pulsar-admin namespaces create public/document
docker exec -it broker bash bin/pulsar-admin namespaces list public

docker exec -it broker bash bin/pulsar-admin topics create-partitioned-topic \
  persistent://public/document/folder \
  --partitions 8

docker exec -it broker bash bin/pulsar-admin topics create-partitioned-topic \
  persistent://public/document/document \
  --partitions 8

###########

docker exec -it broker bin/pulsar-admin topics create-partitioned-topic \
  persistent://public/document/history-topic --partitions 1

docker exec -it broker bin/pulsar-admin topics create-partitioned-topic \
  persistent://public/document/offset-topic --partitions 1

$COMMAND up -d

echo "Pulsar launched"