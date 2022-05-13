from selenium import webdriver
from bs4 import BeautifulSoup
from selenium.webdriver.common.by import By
from time import sleep

navegador = webdriver.Chrome()
navegador.maximize_window()
navegador.get("https://www.tripadvisor.com.br/")

sleep(8)

btn = navegador.find_element(By.ID,"onetrust-accept-btn-handler")
btn.click()

navegador.execute_script('window.scroll(0, 300)')

input_place = navegador.find_element(By.CSS_SELECTOR, '#lithium-root > main > div.dqRmR.dcDXR.dJjeH > div > div > div.weiIG.Z0.Wh.fRhqZ > form > input.fhEMT._G.B-.z._J.Cj.R0')
input_place.click()
input_place.send_keys('Congresso Nacional - Brasília')

sleep(5)

place = navegador.find_element(By.CSS_SELECTOR, '#typeahead_results > a:nth-child(6)')
place.click()

sleep(8)

site_content = navegador.page_source
soup = BeautifulSoup(site_content, 'html.parser')

avaliacoes = soup.find('section', id = 'tab-data-WebPresentation_PoiReviewsAndQAWeb').find('div', id = 'tab-data-qa-reviews-0').find('div', class_ = 'fbjOn').find('div', class_ = 'WlYyy cPsXC fksET cMKSg').text
num_avaliacoes = soup.find('section', id = 'tab-data-WebPresentation_PoiReviewsAndQAWeb').find('div', id = 'tab-data-qa-reviews-0').find('div', class_ = 'fbjOn').find('div', class_ = 'bHUDR f u j').find('div', class_ = 'RTVWf o W f u w eeCyE').text

print("## Resultado da coleta de dados ##")
print("Avaliação do local: "+ avaliacoes +" de "+ num_avaliacoes)