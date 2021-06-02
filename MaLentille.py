from bs4 import BeautifulSoup
import requests 
import pandas as pd

html_text = requests.get("https://www.malentille.com/36-journaliere-36").text
soup = BeautifulSoup(html_text, 'lxml')
jobs = soup.find_all("h3")

npo_jobs = {}
jobs_no = 0

for index, job in enumerate(jobs):
    company_name = job.text.replace("</a>", "" )
    print(company_name.strip())
    jobs_no += 1
    npo_jobs[jobs_no] = [company_name.strip()]

npo_jobs_df = pd.DataFrame.from_dict(npo_jobs, orient='index', columns=['Nom'])

npo_jobs_df.to_csv('csv/MalentilleDaily.csv')
