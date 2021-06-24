from PIL import Image
import requests
import bs4
from bs4 import BeautifulSoup
import requests
import matplotlib.pyplot as plt
import matplotlib.image as mpim
import shutil
import pandas as pd
from IPython.display import Image, HTML

npo_jobs = {}
jobs_no = 0

row=[]

html_text = requests.get(
    "https://www.lentillesmoinscheres.com/lentilles-de-contact/journalieres/").text
soup = BeautifulSoup(html_text, 'lxml')
jobs = soup.find_all("li", class_="type-LENS")

for job in jobs:
    Images = job.find("img")

    full_url = Images.attrs['data-frz-src']
    r = requests.get(full_url, stream=True)

    jobs_no += 1
    npo_jobs[jobs_no] = [Images, full_url]

print (full_url)
