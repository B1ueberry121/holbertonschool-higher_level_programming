#!/bin/bash
# curl JSON
curl -sX POST "$1" -H "Content-Type: appication/json" -d "`cat $2`"
