#!/bin/bash
echo Please enter shared video url
read link
user_ID=`curl -s $link | sed 's/.*user_id=\([0-9]*\).*/\1/' | awk '!seen[$0]++'`
echo "User ID :" $user_ID
echo "Link    : https://tiktok.com/@"$user_ID
