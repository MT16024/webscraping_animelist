from bs4 import BeautifulSoup 
import requests
from openpyxl import Workbook

HEADERS = {
    "Accept": "application/json, */*",
    "Accept-encoding": "gzip, deflate, br, zstd",
    "Accept-language": "en-US,en;q=0.9",
    "User-agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/128.0.0.0 Safari/537.36"
}

def scrape_top_anime(url):
    response = requests.get(url, headers=HEADERS)
    soup = BeautifulSoup(response.text, "html.parser")
    
    anime_list = []
    for anime in soup.select('tr.ranking-list'):
        rank = anime.select_one('td.rank span').text.strip()
        title = anime.select_one('div.di-ib h3 a').text.strip()
        score = anime.select_one('td.score span').text.strip()
        
        anime_list.append({
            'rank': rank,
            'title': title,
            'score': score
        })
    
    return anime_list

def save_to_excel(anime_list, filename):
    wb = Workbook()
    ws = wb.active
    ws.title = "Top Anime"
    
    ws.append(['Rank', 'Title', 'Score'])
    for anime in anime_list:
        ws.append([anime['rank'], anime['title'], anime['score']])
    
    wb.save(filename)

if __name__ == "__main__":
    source = 'https://myanimelist.net/topanime.php'
    top_anime = scrape_top_anime(source)
    
    for anime in top_anime:
        print(f"Rank: {anime['rank']}, Title: {anime['title']}, Score: {anime['score']}")
    
    save_to_excel(top_anime, 'top_50_anime.xlsx')
