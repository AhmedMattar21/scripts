#!/bin/bash

# Define the target host and port
host="my.edgeconncloud.com"
port="80"

# Define the number of retries
max_retries=100

# Define the timeout in seconds
timeout=10

# Function to perform telnet connection
perform_telnet() {
    telnet $host $port
}

# Loop with retries
retries=0
while [ $retries -lt $max_retries ]; do
    echo "Attempting telnet connection (Attempt: $((retries+1)))..."
    perform_telnet && {
        echo "Telnet connection successful."
        break
    }
    echo "Telnet connection failed."
    retries=$((retries+1))
done

# Check if all retries failed
if [ $retries -eq $max_retries ]; then
    echo "All telnet connection attempts failed."
fi
