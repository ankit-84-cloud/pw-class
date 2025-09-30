Source_Dir="D:\st pw dev\session-10-adv-scripting\myapp"
Backup_Dir="D:\st pw dev\session-10-adv-scripting\myapp\backup"
date=$(date +%Y%m%d_%H%M%S)
Backup_File="backup_$date.tar.gz"
#!/bin/bash
# Create backup directory if it doesn't exist
if [ ! -d "$Backup_Dir" ]; then
  mkdir -p "$Backup_Dir"
fi
