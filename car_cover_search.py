import requests
from bs4 import BeautifulSoup

# URL for "Car Cover" listings on OLX
url = "https://www.olx.in/items/q-car-cover"

# Send GET request
headers = {
    "User-Agent": "Mozilla/5.0"
}
response = requests.get(url, headers=headers)

# Parse the page
soup = BeautifulSoup(response.content, "html.parser")

# Find all listings (based on OLX structure, this may vary)
results = []
for item in soup.find_all("a", href=True):
    title = item.get_text(strip=True)
    link = item['href']
    if "car cover" in title.lower():
        results.append(f"{title}\n{link}\n")

# Save to a file
with open("car_covers.txt", "w", encoding="utf-8") as file:
    file.writelines(results)

print("Search results saved to car_covers.txt")
