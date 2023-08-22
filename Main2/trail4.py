import requests

def scrape_google_jobs(api_key, query_file_path):
    job_links = []

    with open(query_file_path, 'r') as file:
        queries = file.readlines()

    for query in queries:
        query = query.strip() + " job for freshers in India"

        try:
            # Prepare the API request URL
            url = f"https://jobs.googleapis.com/v1/search?key={api_key}&q={query}&country=IN&employment_type=FULL_TIME&num_jobs=5"

            # Send a GET request to the API
            response = requests.get(url)
            response.raise_for_status()

            # Parse the JSON response
            data = response.json()

            # Extract job titles and URLs from the response
            if 'jobs' in data:
                for job in data['jobs']:
                    title = job['title']
                    url = job['url']
                    job_links.append({'title': title, 'url': url})
        except requests.exceptions.HTTPError as e:
            print(f"HTTP Error: {e}")
        except requests.exceptions.RequestException as e:
            print(f"Request Exception: {e}")

    return job_links

# Example usage
api_key = 'AIzaSyBB5NOC1aCTGNj_1CTkBEaSWj3RhhDVZRs'  # Replace with your Google Jobs API key
query_file_path = 'static/uploads/Rskills.txt'  # Replace with the path to your query file

results = scrape_google_jobs(api_key, query_file_path)
for job in results:
    print(job['title'], job['url'])
