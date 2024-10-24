#!/bin/bash

# File to store the current container count
COUNT_FILE="container_count.txt"

# If the file doesn't exist, create it and start from 1
if [ ! -f $COUNT_FILE ]; then
    echo "001" > $COUNT_FILE
fi

# Read the current count
current_count=$(cat $COUNT_FILE)

# Run the container with an incremented name
container_name="py-code-${current_count}"

echo "Running container with name: $container_name"

# Run the Docker container
docker run --name $container_name -d python-coding-excercises

# Increment the count (zero-padded to 3 digits)
next_count=$(printf "%03d" $((10#$current_count + 1)))

# Update the count file
echo $next_count > $COUNT_FILE

