from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
import io

driver = webdriver.Chrome("/usr/lib/chromium-browser/chromedriver");
driver.get("https://www.sec.gov/cgi-bin/browse-edgar?action=getcurrent")
#html_tag = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, "/html/body/div/table[2]/tbody/tr[3]/td[2]/a[1]")));
time.sleep(1)
html_tag = driver.find_element_by_xpath('/html/body/div/table[2]/tbody/tr[3]/td[2]/a[1]')
html_tag.click();
time.sleep(1)
file = driver.find_element_by_xpath('//*[@id="formDiv"]/div/table/tbody/tr[2]/td[3]/a')
#except:
#    file = driver.find_element_by_xpath('//*[@id="formDiv"]/div/table/tbody/tr[3]/td[3]/a')

file.click();
time.sleep(1)
f = io.open('myfile.html', 'w', encoding='utf8')
content = driver.find_element_by_xpath('/html/body')
#f.write(content.get_attribute('outerHTML'))


#f = io.open('myfile.html', 'w', encoding='utf8')
#content = driver.find_element_by_xpath('/html/body')
f.write(content.get_attribute('outerHTML'))
time.sleep(8)
f.close()

driver.close()
