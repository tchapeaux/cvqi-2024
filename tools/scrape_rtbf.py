import json

import requests

# For some reason the JSON of each commune contains the full dataset
# So we just take the JSON of the first one and parse it
url = "https://www.rtbf.be/_next/data/rtbf/elections-2024/communales/resultats/anderlues-6150.json"

response = requests.get(url)

pageData = json.loads(response.text)
communes = []

for region in pageData["pageProps"]["widgets"][0]["props"]["results"]:
    for branch in region["branches"]:
        assert branch["type"] == "commune"
        communes.append(branch)

        # Check counting Percentage is 100 (to know if the data is final)
        if branch["results"]["percentageCounting"] != 100:
            print(branch["slug"], branch["results"]["percentageCounting"])

print("Parsed", len(communes), "communes")

with open("communes.json", "w") as f:
    json.dump(communes, f, indent=2)
