#!/usr/bin/env bash
#backup all databases individually, appending day of the week to have 7 rotating days

USER='root'
PASS=''
DEST=""

mkdir -p $DEST

#similar to:
#mysqldump -u root -pradnelac --lock-tables=false --triggers --all-databases>all-20161106.sql

for dbname in $(mysql -N -u $USER -p$PASS -e "select distinct table_schema from information_schema.tables where table_schema not in ('INFORMATION_SCHEMA','mysql','PERFORMANCE_SCHEMA')  ")
do
    mysqldump -u $USER -p$PASS $dbname >$DEST/$dbname_$(date "+%a").sql
done

