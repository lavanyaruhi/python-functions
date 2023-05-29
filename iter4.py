import itertools
import requests

# Infinite iterator to generate URLs
def url_generator():
    index = 1
    while True:
        yield f"https://api.example.com/data/{index}"
        index += 1

# Create the URL generator
url_iter = url_generator()

# Make requests to the URLs indefinitely
for url in itertools.islice(url_iter, 10):
    response = requests.get(url)
    print(f"Response from {url}: {response.status_code}")
