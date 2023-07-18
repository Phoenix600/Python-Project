import requests 
from bs4 import BeautifulSoup 
import pandas as pd 

skills_input = str(input("[+]Enter skills to search job : ")).replace('\n','')
url = f"https://www.timesjobs.com/candidate/job-search.html?from=submit&actualTxtKeywords={'+'.join(skills_input.split(' '))}&searchBy=0&rdoOperator=OR&searchType=personalizedSearch&luceneResultSize=25&postWeek=60&txtKeywords={'+'.join(skills_input.split(' '))}&pDate=I&sequence=1&startPage=1"
print(url)
response = requests.get(url)
# print(response)

soup = BeautifulSoup(response.content,'lxml')

jobs_list = soup.find_all('li',class_='clearfix job-bx wht-shd-bx')

dataFrame = {
        'name'      :       [],
        'published_date' :  [],
        'skills'    :       [],
        'more_info' :       [],
        'description' :     []
        }

for job in jobs_list : 
    published_date = job.find('span',class_='sim-posted').text.strip()

    if 'few' in published_date : 

        skills = job.find('span',class_='srp-skills').text.replace(' ','').strip()
        dataFrame['name'].append(job.find('h2').text.replace('\n','').strip())
        dataFrame['published_date'].append(published_date)
        dataFrame['skills'].append(skills)
        dataFrame['more_info'].append(job.header.h2.a['href'])
        repsponse_description = requests.get(job.header.h2.a['href'])
        soup1 = BeautifulSoup(repsponse_description.content,'lxml')
        job_description = soup1.find('div',class_='jd-desc job-description-main').text.strip().replace('Job Description','').strip()
        dataFrame['description'].append(job_description)

pd.options.display.max_rows = 999
df = pd.DataFrame(dataFrame)
print(df)
df.to_csv('JobsAlert.csv',index=False)
