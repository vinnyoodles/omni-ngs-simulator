#!/bin/bash

# Arguments
# $1 update status (started or finished)
# $2 job id
# $3 command

if [ $1 -eq 1 ]; then
    curl "https://bench.cs.vt.edu/omningssimulator/api/jobs/started/$2" \
        -H "Accept: application/json" \
        -H "Content-Type:application/json" \
        -X POST \
        --data "{\"command\" :\"$3\"}"      
elif [ $1 -eq 2 ]; then
    curl "https://bench.cs.vt.edu/omningssimulator/api/jobs/finished/$2" -X POST
else
    exit
fi
