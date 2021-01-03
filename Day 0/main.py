import os
import requests
import pprint
from dotenv import load_dotenv
import pandas as pd

load_dotenv()

api_key = os.getenv("API_KEY")
token = os.getenv("BEARER_TOKEN")

api_version = 3
app_base_url = f"https://api.themoviedb.org/{api_version}"
endpoint_path = f"/search/movie"
query = "The Matrix"
endpoint = f"{app_base_url}{endpoint_path}?query={query}"
headers = {"Authorization": f"Bearer {token}", "Content-Type": "application/json;charset=utf-8"}

output = 'movies.csv'
movie_data = []
r = requests.get(endpoint, headers=headers)
if r.status_code in range(200, 299):
    data = r.json()
    results = data['results']
    if len(results) > 0:
        movie_ids = set()
        for result in results:
            _id = result['id']
            movie_ids.add(_id)
        for movie_id in movie_ids:
            endpoint_path = f"/movie/{movie_id}"
            endpoint = f"{app_base_url}{endpoint_path}"
            r = requests.get(endpoint, headers=headers)
            if r.status_code in range(200, 299):
                data = r.json()
                movie_data.append(data)

df = pd.DataFrame(movie_data)
print(df.head)
df.to_csv(output, index=False)