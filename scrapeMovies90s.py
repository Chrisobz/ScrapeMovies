import requests
from bs4 import BeautifulSoup
import pandas as pd
from datetime import datetime
import os

# URL of the Stacker Best Movies of All Time page
url = "https://stacker.com/movies/100-best-movies-all-time"

# Send a GET request to the URL
response = requests.get(url)

# Check if the request was successful
if response.status_code == 200:
    page_content = response.text
else:
    print(f"Failed to retrieve the webpage. Status code: {response.status_code}")
    exit()

# Parse the page content with BeautifulSoup
soup = BeautifulSoup(page_content, "html.parser")

# List to store the movie data
movies_data = []

# Find all movie containers
# Using the provided selector for title and year
movie_items = soup.find_all("h2", class_="ct-slideshow__slide__text-container__caption")

for item in movie_items:
    div = item.find("div")
    if div:
        text = div.get_text(strip=True)
        # Extract the year from the text
        # Assuming the format is "#99. Title (Year)"
        if "(" in text and ")" in text:
            title_year = text.split("(")
            title = title_year[0].strip()
            year = title_year[1].strip(")")
            
            try:
                year = int(year)
            except ValueError:
                year = None

            # Filter out movies made between 1990 and 1999
            if year and 1990 <= year <= 1999:
                movies_data.append({
                    "Title": title,
                    "Year": year
                })

# Convert to DataFrame
movies_df = pd.DataFrame(movies_data)

# Display the DataFrame
print("Movies made between 1990 and 1999:")
print(movies_df)

# Save the results to a CSV file
if not os.path.exists("data"):
    os.makedirs("data")

filename = f"data/stacker_movies_1990s_{datetime.now().strftime('%Y%m%d_%H%M%S')}.csv"
movies_df.to_csv(filename, index=False)

print(f"\nData saved to {filename}")
