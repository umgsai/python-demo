#!/bin/bash

cat ./HASH.log | awk -F "[ -]" '{print $7}' | \
awk '{tmp[$0]++}END{for(x in tmp)print "magnet:?xt=urn:btih:"x"\t"tmp[x]}' | \
sort -nrk2 | head
