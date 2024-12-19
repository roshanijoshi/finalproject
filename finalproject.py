# Wikipedia 
# Data points:
    # Page title
    # Main content section
    # Infobox details (e.g., date of birth, location, etc.)
    # Categories
    # Links to related articles


import requests
from bs4 import BeautifulSoup
# from store import insert_wikipedia_data  

search_term = input("Enter the Wikipedia topic to search:\n").replace(" ", "_")  
url = f'https://en.wikipedia.org/wiki/{search_term}'
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
}

response = requests.get(url, headers=headers)

if response.status_code != 200:
    print(f"Sorry, no page found for '{search_term}'. Please check the topic.")
else:
    soup = BeautifulSoup(response.text, 'html.parser')
    print("Title of the website is : ")
    for title in soup.find_all('title'):
      print(title.get_text())
    
    # main_content=soup.find_all('div',id='mw-mf-page-center')
    # print(main_content)
    
    main_content=None
    for element in soup.select('div',id_='mw-mf-page-center'):
        if element.text.strip():
            main_content= element.text.strip()
            # print(main_content)
            break
    
