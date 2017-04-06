#!/bin/bash

cat HASH.log | awk -F "[ -]" '{print $9}'|awk -F ":" '{print $1}' \
| awk '{tmp[$0]++}END{for(x in tmp)print x"\t"tmp[x]}' | sort -nrk2 | head
