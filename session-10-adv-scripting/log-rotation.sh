#!/bin/bash

Log_Dir="MyApp"

LOG_file="app.log"

Max_backups=5

# Log Rotation
#Example: app.log.1, app.log.2, app.log.3.gz etc become app.log.2, app.log.3, app.log.4.gz etc
for (( i=$Max_backups; i>=1; i-- )); do
    if [ -f "$Log_Dir/$LOG_file.$i.gz" ]; then
        if [ $i -eq $Max_backups ]; then
            rm -f "$Log_Dir/$LOG_file.$i.gz"
        else
            mv "$Log_Dir/$LOG_file.$i.gz" "$Log_Dir/$LOG_file.$((i+1)).gz"
        fi
    fi
done

## Compress the most recent uncompressed log file
if [ -f "$Log_Dir/$LOG_file" ]; then
    gzip "$Log_Dir/$LOG_file"
    mv "$Log_Dir/$LOG_file.gz" "$Log_Dir/$LOG_file.1.gz"
fi
# Rename existing compressed log files
for (( i=$Max_backups-1; i>=1; i-- )); do
    if [ -f "$Log_Dir/$LOG_file.$i.gz" ]; then
        mv "$Log_Dir/$LOG_file.$i.gz" "$Log_Dir/$LOG_file.$((i+1)).gz"
    fi  

#incase no file then create a new one
if [ ! -f "$Log_Dir/$LOG_file" ]; then
    touch "$Log_Dir/$LOG_file"
fi

## Delete the oldest uncompressed log file if it exists
if [ -f "$Log_Dir/$LOG_file.$((Max_backups+1))" ]; then 
    rm -f "$Log_Dir/$LOG_file.$((Max_backups+1))"
fi
done