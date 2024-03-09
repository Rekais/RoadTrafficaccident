from google.colab import drive
import csv
import requests
from bs4 import BeautifulSoup

# Mount Google Drive
drive.mount('/content/drive')

# Replace 'your_url_here' with the actual URL of the webpage containing the table
url = 'your_url_here'

# Fetch the HTML content
response = requests.get(url)
html_content = response.text

# Parse the HTML content
soup = BeautifulSoup(html_content, 'html.parser')

# Find the table and extract data
table = soup.find('table')
headers = [header.text.strip() for header in table.find_all('th')]

data_rows = []
for row in table.find_all('tr')[1:]:
    data_row = [td.text.strip() for td in row.find_all('td')]
    data_rows.append(data_row)

# Save data to CSV file in Google Drive
csv_filename = '/content/drive/My Drive/data_table.csv'
with open(csv_filename, 'w', newline='') as csv_file:
    csv_writer = csv.writer(csv_file)
    csv_writer.writerow(headers)
    csv_writer.writerows(data_rows)

print(f'Data has been scraped from the webpage and saved to {csv_filename}.')
