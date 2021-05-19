
import time
import selenium
from selenium import webdriver

a = 202155187 # 당신의 아이디 입력
b = 'ohyeah1!2' # 당신의 비밀번호 입력
URL= 'https://plato.pusan.ac.kr/calendar/view.php?view=upcoming'
driver = webdriver.Chrome('chromedriver')
driver.get(url=URL)

login1=driver.find_element_by_name('username')
login2=driver.find_element_by_name('password')
login1.send_keys(a)
login2.send_keys(b+'\n')

list_todo=[]
list_a=[]
todo=driver.find_elements_by_class_name('event')

for do in todo:
    element=do.text
    list_todo.append(element)
    print(element)
    print()

