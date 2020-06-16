from bs4 import BeautifulSoup
import urllib.request

class Parser(object):

	raw_html = ''
	html = ''
	results = []

	def __init__(self, url, path):
		self.url = url
		self.path = path

	def get_html(self):
		req = urllib.request.urlopen(self.url)
		self.raw_html = req.read()
		self.html = BeautifulSoup(self.raw_html, 'html.parser')

	def parsing(self):
		news = self.html.find_all('p', class_='news-item')

		for item in news: 
			title = item.find('b').get_text()
			date = item.find('span', class_='news-date-time').get_text()
			href = item.a.get('href')

			self.results.append({
				'title': title, 
				'date': date,
				'href': href
				})

	def save(self):
		with open(self.path, 'w', encoding='utf-8') as f:
			i = 1
			for item in self.results:
				f.write(f'Новость №{i}\nНазвание: {item["title"]}\nДата: {item["date"]}\n\n**************************************\n')
				i += 1

	def run(self):
		self.get_html()
		self.parsing()
		self.save()