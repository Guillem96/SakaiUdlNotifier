#!/bin/bash

exec > /home/guillem/SakaiUdlNotifier.log
exec 2>/home/guillem/SakaiUdlNotifier.err

echo "$(date '+%Y-%m-%d %H:%M:%S') - Starting SakaiUdlNotifier"

eval "export $(egrep -z DBUS_SESSION_BUS_ADDRESS /proc/$(pgrep -u $LOGNAME gnome-session)/environ)"
/home/guillem/SakaiUdlNotifier/notifier.py
