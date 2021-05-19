
import time
import selenium
from selenium import webdriver
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException,StaleElementReferenceException

<<<<<<< HEAD
# 데이터 URL에서 불러오기
a = input("id>>>")
b = input("passward>>>>")
=======
a = 202155187 # 당신의 아이디 입력
b = 'ohyeah1!2' # 당신의 비밀번호 입력
>>>>>>> b28f2d0f761bdee451f9a84b20a274df6605ed3f
URL= 'https://plato.pusan.ac.kr/calendar/view.php?view=upcoming'
driver = webdriver.Chrome('chromedriver')
driver.get(url=URL)

login1=driver.find_element_by_name('username')
login2=driver.find_element_by_name('password')
login1.send_keys(a)
login2.send_keys(b+'\n')

<<<<<<< HEAD
dict_todo={}

channel=driver.find_element_by_name('course')
click_channel=driver.find_elements_by_tag_name('option')
del click_channel[0]
n=len(click_channel)

for i in range(1, n+1):
    click_channel = driver.find_elements_by_tag_name('option')
    del click_channel[0]
    click_channel2 = Select(driver.find_elements_by_class_name('select')[0])
    name = click_channel[i - 1].get_attribute("innerHTML")

    click_channel2.select_by_index(i)
    time.sleep(3)
    todo = driver.find_elements_by_class_name('event')
    if len(todo) > 0:
        list_todo = []
        for do in todo:
            do = do.text
            list_todo.append(do)
        dict_todo[name]=list_todo

for i in dict_todo:
    print("<<<<{}>>>>".format(i))
    print()
    for  key in dict_todo[i]:
        print(key)
        print()
    print("-"*60)
=======
list_todo=[]
list_a=[]
todo=driver.find_elements_by_class_name('event')

for do in todo:
    element=do.text
    list_todo.append(element)
    print(element)
    print()

>>>>>>> b28f2d0f761bdee451f9a84b20a274df6605ed3f
