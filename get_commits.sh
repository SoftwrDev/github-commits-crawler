#!/bin/sh

if [ ${#1} -eq 0 ]; then
	echo "Bucket name must be provided."
	exit 1
fi

python main.py
aws s3 cp commits.json s3://$1/commits.json
