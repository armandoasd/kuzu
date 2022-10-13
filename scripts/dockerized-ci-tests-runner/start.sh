#!/bin/bash

cd /actions-runner

# Get registration token
REG_TOKEN = $(curl \
    -X POST \
    -H "Accept: application/vnd.github+json" \
    -H "Authorization: Bearer ${GITHUB_ACCESS_TOKEN}" \
    https://api.github.com/repos/graphflowdb/graphflowdb/actions/runners/registration-token | jq .token --raw-output)

# Register runner
./config.sh --url https://github.com/graphflowdb/graphflowdb --token $REG_TOKEN --name --unattended --labels 'self-hosted-testing'

cleanup() {
    echo "Removing runner..."
    REMOVE_TOKEN = $(curl \
        -X POST \
        -H "Accept: application/vnd.github+json" \
        -H "Authorization: Bearer ${GITHUB_ACCESS_TOKEN}" \
        https://api.github.com/repos/graphflowdb/graphflowdb/actions/runners/remove-token | jq .token --raw-output)

    ./config.sh remove --token ${REMOVE_TOKEN}
}

trap 'cleanup; exit 130' INT
trap 'cleanup; exit 143' TERM

./run.sh & wait $!
