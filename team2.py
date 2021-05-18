import time
import selenium
from selenium import webdriver

n=int(input('수강 중인 과목수를 입력해주세요 >>>'))
a=202155187 #input("id>>>>")
b= 'ohyeah1!2' #input('passward>>>>')
URL= 'https://plato.pusan.ac.kr/calendar/view.php?view=upcoming'
cpath = 'C:\\Users\\angel\\Desktop\\python_code\\chromedriver.exe'
driver = webdriver.Chrome(cpath)
driver.get(url=URL)

login1=driver.find_element_by_name('username')
login2=driver.find_element_by_name('password')
login1.send_keys(a)
login2.send_keys(b+'\n')

todo=driver.find_element_by_class_name('header')
do=driver.find_elements_by_tag_name('p')
driver.find_elements_by_tag_name('option')
print(do[0])

driver.close()