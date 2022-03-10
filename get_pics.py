from curses.ascii import BS
import requests
from bs4 import BeautifulSoup as bs
import os

# Website with quote images
url = 'https://www.pinterest.co.uk/inspirationfeed/motivational-picture-quotes/'

# Download page for parsing
page = requests.get(url)
soup = bs(page.text,'html.parser')

# Locating all elements with image tags
img_tags = soup.findAll('img')

# Creating directory for quote images
if not os.path.exists('quotes'):
    os.makedirs('quotes')

# Moving to new directory
os.chdir('quotes')

#  Image file name variable
x=0

# Writing images
for image in img_tags:
    try:
        url=image['src']
        source = requests.get(url)
        if(source.status_code == 200):
            with open ('quote - '+ str(x)+'.jpg','wb') as f:
                f.write(requests.get(url).content)
                f.close()
                x+=1
    except:
        pass
