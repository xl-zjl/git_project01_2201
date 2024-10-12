import requests
import random

user_agents = [
    "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko)Chrome/90.0.4430.93 Safari/537.36",
    'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/535.1 (KHTML, like Gecko)Chrome/14.0.835.163 Safari/535.1',
    "Opera/9.80 (Windows NT 6.1; U; zh-cn) Presto/2.9.168 Version/11.50",
    "Mozilla/5.0 (Windows NT 6.1; WOW64; rv:6.0) Gecko/20100101 Firefox/6.0"
]
user_agent = random.choice(user_agents)
headers = {
    'User-Agent': user_agent
}
proxys = ['3.225.148.200:80', '113.100.209.184:3128', '93.157.12.248:8080']
proxies = {
    'http': 'https://{}'.format(random.choice(proxys)),
}
res = requests.get("https://httpbin.org/get", headers=headers, proxies=proxies)
res.encoding = 'UTF-8'
print(res.text)
