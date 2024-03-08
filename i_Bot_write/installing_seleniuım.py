# 1- pip install selenium
# 2- selenium kütüphanesi bir uygulamayı web sayfasını bir tarayıcı üzerinden açmalı ->(driver gerekiyor)
# 3- driver-> hangi tarayıcıyla çalısacagimizi belirten bir exe dosyası : driver1->chrome , driver2->firefox vs.
# Linkler: https://selenium-python.readthedocs.io/
#          https://selenium-python.readthedocs.io/installation.html#introduction

from selenium import webdriver

#driver = webdriver.Chrome()
driver = webdriver.Firefox()
url =  "https://sadikturan.com/"

driver.get(url)