import requests
from bs4 import BeautifulSoup

# Specify the URL to scrape
url = "https://www.screener.in/screen/raw/?sort=&order=&source_id=144972&query=Sales+growth+%3E%3D+20%25+AND%0D%0ASales+growth+3Years+%3E%3D+20%25+AND%0D%0APrice+to+Earning+%3CIndustry+PE+AND%0D%0AChange+in+promoter+holding+3Years+%3E+0.0001+%0D%0A"

# Send a GET request to the website
response = requests.get(url)

# Check if the request was successful
if response.status_code == 200:
    # Parse the HTML content of the page
    soup = BeautifulSoup(response.content, 'html.parser')
    
    # Find all <tr> tags with the data-row-company-id attribute
    rows = soup.find_all('tr', attrs={'data-row-company-id': True})
    
    for tr in rows:
        # Find all the <td> tags in the current row
        tds = tr.find_all('td')
        
        # Check if there are at least two <td> tags
        if len(tds) > 1:
            # Find the <a> tag within the second <td> tag
            a_tag = tds[1].find('a')
            
            if a_tag:
                # Get the text of the <a> tag
                a_text = a_tag.get_text(strip=True)
                print(a_text)
else:
    print(f"Failed to retrieve the page. Status code: {response.status_code}")