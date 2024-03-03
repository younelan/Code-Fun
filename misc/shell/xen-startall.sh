		#!/bin/sh

ARRAY=`xe vm-list tags="autostart" | grep uuid | awk '{ print $5 }'`

for f in $ARRAY
do
        VM_NAME=`xe vm-param-get uuid=$f param-name=name-label`
        echo "Starting $VM_NAME"
        /opt/xensource/bin/xe vm-start uuid=$f
done