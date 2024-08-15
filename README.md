# Web Scraping Project

<h2>Project Overview</h2>

I created this web scraper project to efficiently filter movies from the top 100 list on Stacker.com. The list was long, and finding movies released in specific time periods manually would have taken considerable time.

To solve this, I developed two scripts:

1. **Filter Movies After 2000**: This script extracts movies from the list that were released after the year 2000.
2. **Filter Movies From 1990 to 1999**: This script extracts movies that were released between 1990 and 1999.

These scripts automate the process of identifying and filtering movies based on their release years, significantly speeding up the task.

<h2>Scripts</h2>

<h3><code>scrape_movies_2000s.py</code></h3>

This script scrapes and filters movies made after 2000.

<h3><code>scrape_movies_1990s.py</code></h3>

This script scrapes and filters movies made between 1990 and 1999.

<h2>How It Works</h2>

1. **Fetching the Webpage**: The scripts use the requests library to fetch the HTML content from the Stacker page.
2. **Parsing HTML**: The BeautifulSoup library is used to parse the HTML and locate movie titles and years.
3. **Filtering Data**: Based on the year, the scripts filter out movies that fall within the specified time periods.
4. **Saving Results**: The filtered movie data is saved to a CSV file using the pandas library.

<h2>Requirements</h2>

- requests
- beautifulsoup4
- pandas

You can install the required packages by running:

<pre><code>pip install -r requirements.txt</code></pre>

<h2>How to Run</h2>

To use the scripts:

1. **Run the Script for Movies After 2000**:
   <pre><code>python scripts/scrape_movies_2000s.py</code></pre>

2. **Run the Script for Movies From 1990 to 1999**:
   <pre><code>python scripts/scrape_movies_1990s.py</code></pre>

3. The results will be saved in the `<code>data/</code>` directory as CSV files.

<h2>Screenshots</h2>

![scrape](https://github.com/user-attachments/assets/57b4e060-f555-45db-be49-65d8da4d1628)

![scraep](https://github.com/user-attachments/assets/97ffc488-b451-4f8c-84cf-b91f7098b5e0)

![dat1](https://github.com/user-attachments/assets/2249c031-22e5-4e26-bba1-d0f1ec146c3a)

![dat2](https://github.com/user-attachments/assets/193c4cef-f71f-4cc8-bec9-b9026a35f85d)




