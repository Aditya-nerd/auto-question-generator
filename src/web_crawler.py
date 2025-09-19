import requests
from bs4 import BeautifulSoup
import pandas as pd

url = "https://en.wikipedia.org/wiki/Machine_learning"

# Add headers to avoid being blocked
headers = {"User-Agent": "Mozilla/5.0"}

try:
    response = requests.get(url, headers=headers, timeout=10)
    print("Status Code:", response.status_code)

    if response.status_code == 200:
        soup = BeautifulSoup(response.text, "html.parser")
        paragraphs = [p.get_text() for p in soup.find_all("p")]

        df = pd.DataFrame(paragraphs, columns=["text"])
        df.to_csv("../data/crawled_data.csv", index=False, encoding="utf-8")
        print("✅ Data saved to data/crawled_data.csv")
    else:
        print("❌ Failed with status:", response.status_code)

except Exception as e:
    print("❌ Error:", e)
