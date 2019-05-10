from time import sleep
from selenium import webdriver
from scrapy import Selector

URL = "https://www.ifood.com.br/entrar-com-email"
EMAIL = "<EMAIL>"
PASSWORD = "<SENHA>"
URL_IFOOD_HOME = "https://www.ifood.com.br"

driver = webdriver.Chrome()
driver.maximize_window()
driver.get(URL)

selector_email = "//input[@class='form-input__field'][@label='Email']"
input_email = driver.find_element_by_xpath(selector_email)
input_email.send_keys(EMAIL)

selector_continuar = "//button[@type='submit']"
button_continuar = driver.find_element_by_xpath(selector_continuar)
button_continuar.click()

sleep(2)
selector_password = "//input[@name='password']" 
input_password = driver.find_element_by_xpath(selector_password)
input_password.send_keys(PASSWORD)

button_entrar = driver.find_element_by_xpath(selector_continuar)
button_entrar.click()

sleep(2)
selector_localizacao = "//button[@class='btn-address']/div/span[contains(., 'Usar minha')]/../.."
button_localizacao = driver.find_element_by_xpath(selector_localizacao)
button_localizacao.click()

sleep(4)
selector_pizza = "//a[@aria-label='Pizza'][@href]/@href"
href_pizza = Selector(text=driver.page_source.encode("utf-8")).xpath(selector_pizza).extract()[0]
driver.get(URL_IFOOD_HOME + href_pizza)
# button_pizza = driver.find_element_by_xpath(selector_pizza)
# button_pizza.click()

sleep(2)
selector_restaurantes = "//div[@class='restaurants-list__container']/a[@class='restaurant-card']/@href"
# for href_restaurante in Selector(text=driver.page_source.encode("utf-8")).xpath(selector_restaurantes).extract():
# 	link_restaurante = URL_IFOOD_HOME + href_restaurante
# 	print(link_restaurante)
link_restaurante = Selector(text=driver.page_source.encode("utf-8")).xpath(selector_restaurantes).extract()[0]
driver.get(URL_IFOOD_HOME + link_restaurante)

# driver.quit()