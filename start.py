import re
import requests

###!/bin/bash
##echo Please enter shared video url
##read link
short_link = input("Please enter shared video url : ")
##user_ID=`curl -s $link | sed 's/.*user_id=\([0-9]*\).*/\1/' | awk '!seen[$0]++'`
r = requests.get(short_link, allow_redirects=False)
long_link = (r.headers['location'])
m = re.search('&user_id=(\d+)', long_link, re.IGNORECASE)
uid = m.group(1)
##echo "User ID :" $user_ID
##echo "Link    : https://tiktok.com/@"$user_ID
print("User ID :", uid)
print("Link    : https://tiktok.com/@" + uid)
