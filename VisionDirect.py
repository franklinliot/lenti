from bs4 import BeautifulSoup
import requests 
import pandas as pd

html_text = requests.get("https://www.visiondirect.fr/lentilles-de-contact/lentilles-journalieres/").text
soup = BeautifulSoup(html_text, 'lxml')
jobs = soup.find_all("div", class_ ="products-list__name same-height__name")

npo_jobs = {}
jobs_no = 0

for index, job in enumerate(jobs):
    company_name = job.text.replace("</div>", "" )
    print(company_name.strip())
    jobs_no += 1
    npo_jobs[jobs_no] = [company_name.strip()]

npo_jobs_df = pd.DataFrame.from_dict(npo_jobs, orient='index', columns=['Nom'])

npo_jobs_df.to_csv('csv/VisionDirectDaily.csv')