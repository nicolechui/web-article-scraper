import newspaper
from newspaper.api import languages

#assign url

# url = 'https://www.linkedin.com/pulse/15-common-coding-mistakes-beginners-mr-vishal' 
url = 'https://www.linkedin.com/pulse/after-publishing-50-articles-linkedin-ive-learned-tom-popomaronis'

#extract data
url_extract = newspaper.Article(url="%s" % (url), language='en')
url_extract.download()
url_extract.parse()

#display the extracted data
print(url_extract.text)
 
