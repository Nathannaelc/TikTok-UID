# TikTok-UID
~Simple bash script to grab TikTok user id from the shared link.~
Started as a bash script, ended as a python code

# How?
TikTok appends the UID of the video sharer to the short link (vt.tiktok.com) as a parameter.
~This bash script will curl to the link and take the user_id from the URL and echo it out.~
The python code uses request, re, and beautifulsoup to get the user info.

# Why?
TikTok probably uses this for analytics purposes.
This script can help you to discover alt accounts.

# Whats Next?
- [x] Recode
- [x] Grab user info
- [ ] Optimizations


23/3 Recoded in python
23/3 Grabbing user info via beautifulsoup

# How to run
1. Clone to the repo ```git clone https://github.com/Nathannaelc/TikTok-UID/ ```
2. Change directory to TikTok-UID ```cd TikTok-UID```
3. Run the script
  - Bash ```bash start.sh``` (not recommended) 
  - Python <br/>
  ```pip3 install requests``` <br/>
  ```pip3 install beautifulsoup4``` <br/>
  ```python3 start.py```

