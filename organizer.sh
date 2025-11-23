#!/bin/bash

DIRECTORY="./archive"
LOG_FILE="organizer.log"

mkdir -p "$DIRECTORY"

# Check CSV files
csv_file=(*.csv)

if [ ! -f "${csv_file[0]}" ]; then
    echo "No CSV files available"
    exit 
fi

for file in $csv_file; do
    timestamp=$(date +"%Y-%m-%d_%H-%M-%S")
    new_filename="grade-${timestamp}.csv"

    {
        echo "Archiving Details: $file"
        echo "Time Archived: $timestamp"
        echo "New File Name: $new_filename"
        echo "Content:"
        cat "$file"
        echo ""
    } >> "$LOG_FILE"

    mv "$file" "$DIRECTORY/$new_filename"
done