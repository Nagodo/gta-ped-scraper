#Fetch all images from the given URL and save them in a folder

BASE = "https://docs.fivem.net/peds/"
FORMAT = ".webp"

import requests
from pednames import NAMES 

for name in range(len(NAMES)):
    URL = BASE + NAMES[name] + FORMAT
    print(URL)
    response = requests.get(URL)
    file = open("images/" + NAMES[name] + FORMAT, "wb")
    file.write(response.content)
    file.close()
    print("Downloaded " + NAMES[name] + FORMAT)
    
print("All images downloaded successfully!")
