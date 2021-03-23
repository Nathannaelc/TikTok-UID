import re
import requests

#ask for user input
short_link = input("Please enter shared video url : ")
cookie_input = input("Cookies? s_v_web_id : (enter for none) ")

#Unshorten the link
r = requests.get(short_link, allow_redirects=False)
long_link = (r.headers['location'])

#grab the user_id
m = re.search('&user_id=(\d+)', long_link, re.IGNORECASE)
uid = m.group(1)

uid_link = ("https://tiktok.com/@" + uid)
print("Grabbing user info.... Please wait")
print(uid_link)

#Get User Info ( Username, name, following, followers, likes, description )
from bs4 import BeautifulSoup
cookies = dict(s_v_web_id="'" + cookie_input + "'")
r2 = requests.get(uid_link, cookies=cookies)
soup = BeautifulSoup(r2.content, 'html.parser')
username = soup.find_all("h2", class_="jsx-2997938848 share-title")[0].text
name = soup.find_all("h1", class_="share-sub-title")[0].text
following = soup.find_all("strong", title="Following")[0].text
followers = soup.find_all("strong", title="Followers")[0].text
likes = soup.find_all("strong", title="Likes")[0].text
description = soup.find_all("h2", class_="share-desc mt10")[0].text

#print datas
print("User ID   :", uid)
print("Username  :", username)
print("Name      :", name)
print("Following :", following)
print("Followers :", followers)
print("Likes     :", likes)
print("Bio       :", description)
