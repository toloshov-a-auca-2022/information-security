#!/bin/bash
if [ $# -ne 1 ]; then
  echo "Usage: $0 <directory>"
  exit 1
fi
dir=$1
if [ ! -d "$dir" ]; then
  echo "Error: $dir is not a directory."
  exit 1
fi
for file in "$dir"/*; do
  if [ -f "$file" ] && [ ! -s "$file" ]; then
    echo "Deleting empty file: $file"
    rm "$file"
  fi
done
