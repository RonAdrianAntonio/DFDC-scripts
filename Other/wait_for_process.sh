#!/bin/bash

while [ -e /proc/$1 ]
do
    echo waiting...
done
echo "Starting Next Program"
./$2
