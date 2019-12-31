import json
import csv

# change file name
file_name="starwars_2116.har"

with open(file_name, 'r') as f:
    json_data = f.read()
    f.close()
parsed_json = json.loads(json_data)
entries_len = len(parsed_json['log']['entries'])
urls = []
for i in range(entries_len):
    url=parsed_json['log']['entries'][i]['request']['url']
    ref="https://www.rottentomatoes.com/napi/movie"
    if ref in url:
        urls.append(url)
print(len(urls))

import requests as re

csv_file = open('starwars_2.csv', mode='w')

F = True
i=1
for url in urls:
    response = re.get(url)
    if response:
        # write to csv
        if F: # add header
            fieldnames = list(response.json()['reviews'][0].keys())
            writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
            writer.writeheader()
            F = False

        for review in response.json()['reviews']:
            writer.writerow(review)
        print("adding page", i, '/', len(urls))
        i+=1
    else:
        print("Error")