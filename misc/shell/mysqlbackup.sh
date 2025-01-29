#!/usr/bin/env bash

USER='root'
PASS='password'
DEST="/var/dbbackup"

mkdir -p $DEST

for dbname in $(mysql -N -u $USER -p$PASS -e "select distinct table_schema from information_schema.tables where table_schema not in ('INFORMATION_SCHEMA','mysql','PERFORMANCE_SCHEMA')  ")
do
	mysqldump -u $USER -p$PASS $dbname >"$DEST/$(date "+%a")_${dbname}.sql"
done
