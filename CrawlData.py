# @Author  : ShiRui

import requests


class CrawlData(object):

	# 1.获取url
	def __init__(self):

		self.urls = []
		self.headers = {
			'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:60.0) Gecko/20100101 Firefox/60.0',
		}
		for i in range(0, 10, 2):

			self.url = "https://www.zhihu.com/api/v4/members/WaJueJiPrince/followers?include=data%5B*%5D.answer_count%2Carticles_count%2Cgender%2Cfollower_count%2Cis_followed%2Cis_following%2Cbadge%5B%3F(type%3Dbest_answerer)%5D.topics&offset={}&limit=20".format(i*10)  # 翻页会把offset值改变，大家可以自己观察。
			self.urls.append(self.url)

	# 2.获取页面信息。

	def start(self):

		for url in self.urls:

			html = requests.get(url, headers=self.headers)
			for info in html.json()['data']:

				name = info['id']
				self.saveinfo(name)

	# 存储数据
	@staticmethod
	def saveinfo(name):

		with open('id.txt', 'a') as f:
			f.write(name)
			f.write('\n')

if __name__ == "__main__":

	crawldata = CrawlData()
	crawldata.start()
