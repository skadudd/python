import requests
from bs4 import BeautifulSoup

def filter_hot_articles(all_articles):
    print(all_articles)

def extract_data(data):
    title = data.find('td','title hotdeal_var8').find('a', {'class':None}).get_text(strip=True)
    replied = data.find('td','title hotdeal_var8').find('a', {'class':None}).next_sibling.next_sibling.get_text(strip=True)
    author = data.find('td','author').get_text(strip=True)
    date = data.find('td','time').get_text(strip=True)
    view = data.find('td','m_no').get_text(strip=True)
    recommended = data.find('td','m_no m_no_voted').get_text(strip=True)
    article_id = data.find('td','title hotdeal_var8').find('a')['href']
    return {
        'title' : title,
        'repied' : replied,
        'author' : author,
        'date' : date,
        'view' : view,
        'recommended' : recommended,
        'article_id' : article_id
    }

def do_scrap(url):
    result = requests.get(url)
    soup = BeautifulSoup(result.text, 'html.parser')
    article_list = soup.tbody
    list_1 = soup.find('tbody').find_all('tr',{'class':None})

    for data in list_1:
        all_articles = extract_data(data)
        filtered_hot_articles = filter_hot_articles(all_articles)

def scrapper(page_count):
    fmkorea = f'https://www.fmkorea.com/index.php?mid=humor&page='
    result = []
    for page in range(1, page_count):
        url = fmkorea + str(page)
        print(url)
        do_scrap(url)

def main():
    page_count = 50
    result = scrapper(page_count)
    print(result)

main()
