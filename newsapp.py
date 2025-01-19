import requests

query=input("what type of news you are interested?:")
url=f"https://newsapi.org/v2/everything?q{query}&from=2024-12-19&sortBy=publishedAt&apiKey=e7deeccc62434b919db438ab994547ee"
r=requests.get(url)
print(r.text)