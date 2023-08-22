from flask import Blueprint,render_template
from serpapi import GoogleSearch
import requests


second = Blueprint("second",__name__,static_folder="static",template_folder="templates")
@second.route("/",methods=["POST","GET"])


def home():
    
    file1=open('static/uploads/Rskills.txt','r')
    lines=file1.readlines()
    count=0
    for line in lines:
        query=line+"job for freshers in India"
        count+=1
        api_key = 'AIzaSyCaAxhGum_rvXgkHyulRcf8prMEkVxgqVU'  # Replace with your Google Search API key
        cx = 'a3b8b859565de45b5'  # Replace with your Custom Search Engine (CX) ID

    # Prepare the API request URL
        url = f"https://www.googleapis.com/customsearch/v1?key={api_key}&cx={cx}&q={query}&num=2"

    # Send a GET request to the API
        response = requests.get(url)
        response.raise_for_status()

    # Parse the JSON response
        data = response.json()

    # Extract job information from the response
        job_data = []
        try:
            if 'items' in data:
                for item in data['items']:
                    title = item['title']
                    url = item['link']
                description = item['snippet']

                job_data.append({'title': title, 'url': url, 'description': description})
        except:
           pass
    titles_and_links = []
    with open('static/uploads/TandL.txt', 'r') as f:
        for line in f:
            try:
                title, url = line.strip().split(',',1)
                titles_and_links.append((title, url))
            except ValueError:
                pass
    results = home()
    for result in results:
        print(f"Title: {result['title']}")
    print(f"URL: {result['url']}")
    print(f"Description: {result['description']}")
    print()
    return job_data

