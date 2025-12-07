# Access github and get the output and convert it to Dictionary 

#import requests

#response = requests.get("https://api.github.com/repos/kubernetes/kubernetes/pulls")

#pr_details = response.json()

#for users in range(len(pr_details)):
#    print(pr_details[users]["user"]["login"])

import requests

url = "https://api.github.com/repos/kubernetes/kubernetes/pulls"

response = requests.get(url)

if response.status_code == 200:

    pull_requests = response.json()

    pr_creators = {}

    for pull in pull_requests:
        creator = pull["user"]["login"]
        if creator in pr_creators:
            pr_creators[creator] += 1
        else:
            pr_creators[creator] = 1

    print("PR Creators and Count:")
    for creator, count in pr_creators.items():
        print(creator, count, "PR(s)")
else:
    print(f"Failed to fetch data. Status code: {response.status_code}")



