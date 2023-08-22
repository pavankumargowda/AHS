import requests

def scrape_google_jobs(query):
    api_key = 'AIzaSyCaAxhGum_rvXgkHyulRcf8prMEkVxgqVU'  # Replace with your Google Search API key
    cx = 'a3b8b859565de45b5'  # Replace with your Custom Search Engine (CX) ID

    # Prepare the API request URL
    url = f"https://www.googleapis.com/customsearch/v1?key={api_key}&cx={cx}&q={query}&num=5"

    # Send a GET request to the API
    response = requests.get(url)
    response.raise_for_status()

    # Parse the JSON response
    data = response.json()

    # Extract job information from the response
    job_data = []
    if 'items' in data:
        for item in data['items']:
            title = item['title']
            url = item['link']
            description = item['snippet']

            job_data.append({'title': title, 'url': url, 'description': description})

    return job_data

# Example usage
query = "python developer jobs"
results = scrape_google_jobs(query)

# Print the scraped job data
for result in results:
    print(f"Title: {result['title']}")
    print(f"URL: {result['url']}")
    print(f"Description: {result['description']}")
    print()
