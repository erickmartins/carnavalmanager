"""Example usage of MechanicalSoup to get the results from
DuckDuckGo."""

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import mechanicalsoup

chrome_options = Options()
chrome_options.add_argument("--headless")

chromer = webdriver.Chrome(chrome_options=chrome_options)
# Connect to duckduckgo
browser = mechanicalsoup.StatefulBrowser()
savedir = "/home/erick/Dropbox/erick/carnavalmanager/data/"

for ano in range(1935, 2018):
    link = "http://www.galeriadosamba.com.br/carnaval/" + str(ano) + "/"
    browser.open(link)
    for i in browser.links(url_regex='../carnavais/.*'):
        i.attrs['href'] = "../" + i.attrs['href']
        escola = i.attrs['href'].split("/")[3]
        filename = savedir + str(ano) + "_" + escola + ".txt"
        # browser.download_link(i, file=filename)
        browser.follow_link(i)
        chromer.get(browser.get_url())

        result = chromer.find_element_by_id("LES")
        f = open(filename, 'w')
        f.write(result.text)
        f.close()
        browser.open(link)
