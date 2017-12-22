#!python3
#Accuweather weather locator
import bs4,lxml
import urllib.request
import requests

def main():
	#Header files
	headers = {}
	headers['User-Agent'] = "Mozilla/5.0 (X11; Linux i686) AppleWebKit/537.17 (KHTML, like Gecko) Chrome/24.0.1312.27 Safari/537.17"

	#Find the longitude and latitude then find location
	print ('Searching')
	url1 = 'https://www.google.co.in/search?client=firefox-b-ab&dcr=0&ei=TT48WtWUJcncvgTut6ngBA&q=what+is+my+location+now&oq=what+is+my+lo&gs_l=psy-ab.3.1.35i39k1j0l9.2581.7436.0.9279.13.13.0.0.0.0.297.2290.0j6j5.11.0....0...1.1.64.psy-ab..2.11.2281...0i67k1j0i131k1j0i20i263k1.0.7MUUrBtRDSc'
	req = urllib.request.Request(url1, headers = headers)
	resp = urllib.request.urlopen(req)

	soup = bs4.BeautifulSoup(resp,"lxml")

	location = soup.select('.vk_sh')
	loc = location[0].getText()
	print ('Location found')

	#Google Search the location
	url3 = 'https://www.google.co.in/search?q='+'accuweather '+''.join(loc)
	res = requests.get(url3)
	soup1 = bs4.BeautifulSoup(res.text,"lxml")

	#Get the link of the first search
	add_my = soup1.select('.r a')
	rest = add_my[0].get('href')

	#Accuweather part
	url2 = 'http://google.com'+rest

	req = urllib.request.Request(url2, headers = headers)
	resp = urllib.request.urlopen(req)

	soup = bs4.BeautifulSoup(resp,"lxml")

	#List to store the conditions
	my_list = []

	loc = soup.select('.current-city h1')
	my_list.append(loc[0].getText())

	temp = soup.select('.local-temp')
	my_list.append(temp[0].getText())

	cond = soup.select('.cond')
	my_list.append(cond[0].getText())

	print ('{} {} {}'.format(my_list[0],my_list[1],my_list[2]))

if __name__ == '__main__':
	main()
