from bs4 import BeautifulSoup
import requests
import time

#want to get rid of skills the user lacks
print("Add skills you are unfamiliar with:")
unfamiliar_skill = input('<')
print(f'Filtering out: {unfamiliar_skill}')
#get specific info from website + add .text so that you do not get status code
def find_jobs():
    html_text = requests.get('https://www.timesjobs.com/candidate/job-search.html?searchType=personalizedSearch&from=submit&txtKeywords=python&txtLocation=').text
    #print(html_text)
    soup = BeautifulSoup(html_text,'lxml')

    jobs = soup.find_all('li',class_ = 'clearfix job-bx wht-shd-bx')
    #want to search for the name of the company only so use job.find instead of trying to use an h3 tag
    #use replace method to replace blank space with nothing
    #enumerate allows us to iterate over the jobs list as well as the jobs content
    #index acts as the counter over which you are iterating
    #job variable will be with beautiful soup object itself
    for index, job in enumerate(jobs):
        #to ensure that only the jobs posted a few days ago is there put date_posted as the first line and run a if condition
        date_posted = job.find('span',class_='sim-posted').span.text
        if 'few' in date_posted: 
            company_name = job.find('h3',class_= 'joblist-comp-name').text.replace(' ','')
            skills = job.find('span',class_='srp-skills').text.replace(' ','')
            #want to get details from the job description ie. the link to reach to that space where more info is found.
            #go to job -> header tag -> h2 -> a the link is present
            more_info = job.header.h2.a['href']
    #print(company_name)
    #print(skills)
            #since skill is a long string just put a condition:
            if unfamiliar_skill not in skills:
                #to post the data into a particular file in text format
                with open(f'D:\Book Recommendation system/{index}.txt','w') as f:
                    #this block is to write in a text file
                    f.write(f"Company Name : {company_name.strip()} \n")
                    f.write(f"Required Skills : {skills.strip()} \n")
                    f.write(f"More Info : {more_info} \n")
                print(f'File Saved : {index}')
                    
                
                #use strip to get rid of blank space
                #this block is simple print
                    #print(f"Company Name : {company_name.strip()}")
                    #print(f"Required Skills : {skills.strip()}")
                    #print(f"More Info : {more_info}")

                    #print('')

if __name__  == '__main__':
    while True:
        find_jobs()
        #to make the prohram wait
        time_wait = 10
        print(f'Waiting {time_wait} minutes...')
        #for ten minutes: 60*10(60 seconds, 10 minutes) you want to fetch the data:
        time.sleep(time_wait * 60 )