#coding:utf-8

import re, shutil, webbrowser,os, requests
from bs4 import BeautifulSoup

books = []
def compareWithScore(book1, book2) :
	return int((book2['score'] - book1['score']) * 10)

def getBooksInfo(search_text, start=None) :
	if start :
		url = 'http://book.douban.com/subject_search?search_text=%s&start=%d' % (search_text, start)
	else:
		url = 'http://book.douban.com/subject_search?search_text=%s' % search_text

	r = requests.get(url)
	if 200 != r.status_code :
		return

	soup = BeautifulSoup(r.text)
	countstr = soup.findAll('div', 'trr')
	count = 0
	if len(countstr) > 0 and len(countstr[0]) > 0:
		counts = re.findall(r'([0-9]+)$', countstr[0].contents[0])
		if len(counts) > 0 :
			count = int(counts[0])
	print url, count
	if count > 0 :
		items = soup.findAll('li', 'subject-item')
		for item in items:
			#  get title
			titles = []
			info = item.findChild('div', 'info')

			for string in info.h2.strings :
			 	titles.append(string.encode('utf-8').replace('\r\n', '').replace('\n', '').strip(' ').strip('\t'))

			title = ''.join(titles)

			#  get score
			score = 0.0
			rating = item.findChild('span', 'rating_nums')
			if rating:
				score = float(rating.string)
				print score

			url = info.findChild('a')['href']

			book = {'score': score, 'name' : title, 'url' : url}
			books.append(book)

	return count

def write_data_to_html(search_text) :
	outputfile = './%s.html' % search_text
	shutil.copy("./data/template.html", outputfile)

	insertText = []
	for i, book in enumerate(books):
		insertText.append('<tr><td>%d</td><td>%.1f</td><td><a href="%s">%s</a></td></tr>' %(i + 1, book['score'], book['url'],  book['name'].decode('utf-8')))

	with open(outputfile, 'r') as fout :
		html = fout.read()
		fout.close()

		html = html.replace('{{title}}', search_text)
		html = html.replace('{{items}}', '\n'.join(insertText).encode('utf-8'))

		with open(outputfile, 'w') as fout :
			fout.write(html)
			fout.close()

			webbrowser.open(os.path.abspath(outputfile))

def sort_search_result(search_text) :

	# get books
	count = getBooksInfo(search_text)
	while len(books) < count:	
		getBooksInfo(search_text, len(books))
	# sort
	books.sort(cmp=compareWithScore)
	# write file
	write_data_to_html(search_text)

if __name__ == '__main__' :
	sort_search_result('python')