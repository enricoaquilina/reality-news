from urllib.request import urlopen
import json


categories =[]
outlets = []

with urlopen('https://newsapi.org/v1/sources') as r:
    sources = json.loads(r.read().decode(r.headers.get_content_charset('utf-8')))

with urlopen('https://newsapi.org/v1/articles?source=the-next-web&sortBy=latest&apiKey=C303dee9bdb74212a31c245afca3b6e9') as r:
    news = json.loads(r.read().decode(r.headers.get_content_charset('utf-8')))


for source in sources['sources']:
    if (source['category'] not in str(categories)):
        categories.append(source['category'])
    if (source['id'] not in str(outlets)):
        outlets.append(source['id'])

for category in categories:
    print(category)

print('There are '+str(len(categories))+' categories')

for outlet in outlets:
    print(outlet)
print('There are ' + str(len(outlets)) + ' outlets')



    # for article in news:
#     print(article)