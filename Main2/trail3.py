import requests
from flask import Flask, render_template
#api_key = 'AIzaSyCaAxhGum_rvXgkHyulRcf8prMEkVxgqVU' AIzaSyBB5NOC1aCTGNj_1CTkBEaSWj3RhhDVZRs
    #api_key=' AIzaSyB71sDPT52PM-i56XVGoYGxc7ww0_n1dMM'# Replace with your Google Search API key
    #cx = 'a4e6f0023459c4d48'
    #cx='a3b8b859565de45b5' 56d3541d224974d0c

def scrape_google_jobs(query):
    api_key = 'AIzaSyB71sDPT52PM-i56XVGoYGxc7ww0_n1dMM'  # Replace with your Google Search API key
    cx = 'a4e6f0023459c4d48'  # Replace with your Custom Search Engine (CX) ID

    # Prepare the API request URL
    url = f"https://www.googleapis.com/customsearch/v1?key={api_key}&cx={cx}&q={query}&num=5"

    # Send a GET request to the API
    response = requests.get(url)
    response.raise_for_status()

    # Parse the JSON response
    data = response.json()

    # Extract job links from the response
    job_links = []
    if 'items' in data:
        for item in data['items']:
            url = item['link']
            job_links.append(url)

    return job_links

def home():
    file_path = 'static/uploads/Rskills.txt'
    
    with open(file_path, 'r') as file:
        queries = file.readlines()
    
    job_links = []
    
    for query in queries:
        query = query.strip() + " job for freshers in India"
        
        results = scrape_google_jobs(query)
        job_links.extend(results)

    return render_template('job_links.html', links=job_links)
