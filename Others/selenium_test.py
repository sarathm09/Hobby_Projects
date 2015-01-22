from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

d = webdriver.Firefox()
d.get("http://shorte.st/strackable/c47cc81d686730a6744c47d3097a783e/csebeta.x10.mx/1/1/http://csebeta.x10.mx/file.php?id=3c178522855b0381e57e2b3166204682")
wait = WebDriverWait(d, 7)
el = wait.until(expected_conditions.element_to_be_clickable(By.ID("skip_button")))
el = d.find_element_by_id("skip_button")
el.click()
d.switchTo().alert().accept()