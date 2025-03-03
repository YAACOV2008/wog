#!/bin/sh

# Check if /app/scores.txt is a directory
if [ -d "/app/scores.txt" ]; then
    echo "/app/scores.txt is a directory, removing it..."
    rm -rf /app/scores.txt

# Run the application
exec "$@"
