#!/bin/bash

# Move to the directory of your app on the server
cd /home/team002/workspace/server_test

# Activate the python3 virtual env
source venv/bin/activate

# Show arguments
echo $@

# Run the code with arguments
python3 test-1.py $@

