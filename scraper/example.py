from selenium import webdriver
from selenium.webdriver.chrome.options import Options

chrome_options = Options()
chrome_options.add_argument("--headless")

browser = webdriver.Chrome(chrome_options=chrome_options)

browser.get("http://www.galeriadosamba.com.br/carnavais/estacao-primeira-de-mangueira/1932/2/")

nav = browser.find_element_by_id("LES")

print(nav.text)