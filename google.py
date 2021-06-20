from selenium import webdriver

driver = webdriver.Chrome()
driver.get('https://magazine.musinsa.com/index.php?m=street&_y=2021&_mon=06%2C05%2C04&style=001')
driver.find_elements_by_css_selector('.articleImg')[0].click() # 이미지 접속
url = driver.find_elements_by_css_selector('.lbox')[0].get_attribute('href') # 이미지 URL 따기
driver.get(url) # url 접속을 통한 다운로드