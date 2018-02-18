#!/bin/bash

notifier_path=$(cat config.json | jq .path | sed -e 's/^"//' -e 's/"$//') 

export PATH=$PATH:$notifier_path/webdriver

exec > $notifier_path/SakaiUdlNotifier.log
exec 2>$notifier_path/SakaiUdlNotifier.err

echo "$(date '+%Y-%m-%d %H:%M:%S') - Starting SakaiUdlNotifier"

# Allow crontab to show notifications
username=$(cat config.json | jq .username | sed -e 's/^"//' -e 's/"$//')
password=$(cat config.json | jq .password | sed -e 's/^"//' -e 's/"$//')
exec_path=$notifier_path

python $exec_path/notifier.py $username $password

exit 0