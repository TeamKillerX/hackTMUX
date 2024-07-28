#!/bin/bash
# credits by @xtdevs

usage() {
    echo "Usage: $0 --ask <question>"
    exit 1
}

ASK=""
while [ "$1" != "" ]; do
    case $1 in
        --ask ) shift
                ASK=$1
                ;;
        * )     usage
    esac
    shift
done
if [ "$ASK" == "" ]; then
    usage
fi
URL="https://randydev-ryuzaki-api.hf.space/ryuzaki/chatgpt-old"
PAYLOAD=$(jq -n --arg query "$ASK" '{query: $query}')
RESPONSE=$(curl -s -X POST "$URL" \
     -H "Content-Type: application/json" \
     -d "$PAYLOAD")
MESSAGE=$(echo "$RESPONSE" | jq -r '.randydev.message')
if [ "$MESSAGE" != "null" ]; then
    echo "$MESSAGE"
else
    echo "Failed to extract message from the response."
fi
