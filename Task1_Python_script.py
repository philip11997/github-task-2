# Python script to scrape an article given the url of the article and store the extracted text in a file
# Url: https://medium.com/@subashgandyer/papa-what-is-a-neural-network-c5e5cc427c7

import os
import requests
import re
# Code here - Import BeautifulSoup library
from bs4 import BeautifulSoup
# Code ends here

# function to get the html source text of the medium article
def get_page():
	global url
	
	# Code here - Ask the user to input "Enter url of a medium article: " and collect it in url
	# url is a global variable containing the url of the medium article
	url = input("Enter url of a medium article: ")
	# Code ends here
	
	# handling possible error
	if not re.match(r'https?://medium.com/',url):
		print('Please enter a valid website, or make sure it is a medium article')
		sys.exit(1)

	# Code here - Call get method in requests object, pass url and collect it in res
	res = requests.get(url)
	# Code ends here

	res.raise_for_status()
	soup = BeautifulSoup(res.text, 'html.parser')
	return soup

# function to remove all the html tags and replace some with specific strings
def clean(text):
        rep = {"<br>": "\n", "<br/>": "\n", "<li>":  "\n"}
        rep = dict((re.escape(k), v) for k, v in rep.items()) 
        pattern = re.compile("|".join(rep.keys()))
        text = pattern.sub(lambda m: rep[re.escape(m.group(0))], text)
        text = re.sub('\<(.*?)\>', '', text)
        return text


def collect_text(soup):
        text = f'url: {url}\n\n'
        para_text = soup.find_all('p')
        print(f"paragraphs text = \n {para_text}")
        for para in para_text:
                text += f"{para.text}\n\n"
        return text

# function to save file in the current directory
def save_file(text):
        if not os.path.exists('./scraped_articles'):
                os.mkdir('./scraped_articles')
        name = url.split("/")[-1]
        print(name)
        fname = f'scraped_articles/{name}.txt'
	
	# Code here - write a file using with (2 lines)
	# A new folder "scraped_articles" will exist
	# and the .txt should be in that folder
	# Therefore, use os.path.join to set the path of the .txt
	# and the name of the article should be: papa-what-is-a-neural-network-c5e5cc427c7
        file = open(os.path.join('./scraped_articles', name+".txt"), "w")
        file.write(text)
	# Code ends here
        # The path should be: ./scraped_articles/papa-what-is-a-neural-network-c5e5cc427c7
        print(f'File saved in directory {fname}')


if __name__ == '__main__':
	text = collect_text(get_page())
	save_file(text)
	# Instructions to Run this python code
	# Give url as https://medium.com/@subashgandyer/papa-what-is-a-neural-network-c5e5cc427c7
