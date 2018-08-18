# @Author  : ShiRui

import requests


class SendMessages(object):

	def __init__(self, receiver_hash):

		self.url = "https://www.zhihu.com/api/v4/messages"
		self.headers = {
			'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:60.0) Gecko/20100101 Firefox/60.0',
		}
		self.data = {
			'content': "我是it小白，能交个朋友吗？",
			'receiver_hash': receiver_hash,
			'type': "common"
		}
		self.cookie = {'cookie': '_zap=cd6fcf6a-aa6f-49e2-9b27-6f6ac3b85c22; d_c0="ADBgfOdXiQ2PToSrV0TT0UgX5CR_5U_zb84=|1525335257"; q_c1=3b3479209379413c9d71df3840c7ceb8|1533613649000|1523854021000; _xsrf=RSTqJqRGaXtXQpF3gOzyKFWpy2k7ekqH; l_cap_id="MGNmODk2Njk4NThhNDVkZTk1NjcxMWY4YTk3M2M1NDc=|1534401991|833dbda5e6baf614bc57ff3c2d88941371fcbec2"; r_cap_id="YWQ1OWM5MjUwODFmNDg4NGE0NTQ2MzAxZDQ5NmJkNDU=|1534401991|e03997db0448cf152c1ea06da77aa2fb9bbe4462"; cap_id="MTFlZDQ5NDg0YzE1NDMxMmIyMjkwNDkzMzU5YjdkYjU=|1534401991|bd907a01d08069910fc962b70246e41d6298e774"; capsion_ticket="2|1:0|10:1534498986|14:capsion_ticket|44:NmQ3MGQ3N2M1OWNlNGZiNjg5ZWMzNDVmODI3MTUzNWE=|15a145d52b220e223c7f70a8a81b19bfb53294bc0b264e0ce84b2b35bba54edf"; z_c0="2|1:0|10:1534499069|4:z_c0|92:Mi4xcHJBSkNBQUFBQUFBTUdCODUxZUpEU2NBQUFDRUFsVk5fU1dlV3dEcFdUWDZ4WWwyNy14S3dSM0JvXzVBd2c1WUJ3|6fa9a8b2149d7bbe660ebb918dec820d9bc9e6679d5d2caa397d5401bf67ad7b"; __utma=155987696.1071287102.1534514441.1534514441.1534514441.1; __utmz=155987696.1534514441.1.1.utmcsr=(direct)|utmccn=(direct)|utmcmd=(none); tgw_l7_route=c919f0a0115842464094a26115457122'}

	def send(self):

		try:
			requests.post(self.url, headers=self.headers, json=self.data, cookies=self.cookie)
			print("发送成功！")

		except:

			print("发送失败！")

if __name__ == "__main__":

	with open('id.txt') as f:

		for line in f:
			receiver_hash = line.strip()
			print(receiver_hash)
			sendmessage = SendMessages(receiver_hash)
			sendmessage.send()
