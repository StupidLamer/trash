from bs4 import BeautifulSoup
import urllib.request

req = urllib.request.urlopen('https://leninsk-kuz.ru/news/')
html = req.read()

soup = BeautifulSoup(html, 'html.parser')
news = soup.find_all('p', class_='news-item')

results = []

for item in news: 
	title = item.find('b').get_text()
	date = item.find('span', class_='news-date-time').get_text()
	href = item.a.get('href')

	results.append({
		'title': title, 
		'date': date,
		'href': href
		})

print(results[:3])

with open('news.txt', 'w', encoding='utf-8') as f:
	i = 1
	for item in results:
		f.write(f'Новость №{i}\nНазвание: {item["title"]}\nДата: {item["date"]}\n\n**************************************\n')
		i += 1
