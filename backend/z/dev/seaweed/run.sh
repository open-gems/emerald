#!/bin/bash

DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" && pwd )"

cd "$DIR"

COMMAND="docker compose"
BUCKET_NAME="documentos"

echo "Running SeaweedFS with $COMMAND from $DIR..."

$COMMAND up -d

echo "Seaweed launched"
