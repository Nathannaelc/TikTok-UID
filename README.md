# TikTok-UID
Simple bash script to grab TikTok user id from the shared link.

# How?
TikTok appends the UID of the video sharer to the short link (vt.tiktok.com) as a parameter.
This bash script will curl to the link and take the user_id from the URL and echo it out.

# Why?
TikTok probably uses this for analytics purposes.
This script can help you to discover alt accounts.

# Whats Next?
- [x] Recode
- [ ] Grab user info

23/3 Recoded in python

# How to run
1. Clone to the repo ```git clone https://github.com/Nathannaelc/TikTok-UID/ ```
2. Change directory to TikTok-UID ```cd TikTok-UID```
3. Run the script
  - Bash ```bash start.sh```
  - Python 
  ```pip3 install requests``` <br/>
  ```python3 start.sh```
