import time
from selenium import webdriver
import pyautogui



noidung=input("What yourcontent ? ")
driver = webdriver.Chrome('C:\\Users\\Khanh\\Desktop\\chromedriver.exe')  # Optional argument, if not specified will search path.
driver.get('https://m.facebook.com/');
# time.sleep(5) # Let the user actually see something!
print('Login success!')
# Nhập email
email = driver.find_element_by_xpath("//input[@id='email' or @name='email']")
email.send_keys('minhphuongvk@ymail.com')
print("Email Id entered...")
# Nhập mật khẩu
password = driver.find_element_by_xpath("//input[@id='m_login_password']")
password.send_keys('Billgator13071997okeh')
print("Password entered...")
# ấn nút đăng nhập
button = driver.find_element_by_xpath("//button[@id='u_0_5']")
button.click()
print("FB opened")
time.sleep(5)

# ấn vào nút đăng bài
time.sleep(1)
driver.get('https://facebook.com/');
time.sleep(3)
pyautogui.press('esc')
# Nhấn vào đăng bài
time.sleep(5)
# Ấn vào nút bảng tin
into1 = driver.find_element_by_css_selector("._1cx1 ._1hx ._3en1")
into1.click()
into1.send_keys(noidung)
time.sleep(5)
post=driver.find_element_by_css_selector("._36bx ._2dck ._1mf7")
post.click()

# Nhấn vào thanh tìm kiếm
# into1 = driver.find_element_by_css_selector("#facebook ._-kb button, #facebook ._-kb input, #facebook ._-kb label, #facebook ._-kb select, #facebook ._-kb td, #facebook ._-kb textarea")
# into1.click()
# ấn vào nút oke
# into = driver.find_element_by_class_name("_2pis")
# into.click()
# # Vào trang cá nhân
# dangbai = driver.find_element_by_class_name("_5xu4")
# dangbai.click()




# search_box = driver.find_element_by_name('q')
# search_box.send_keys('ChromeDriver')
# search_box.submit()


# time.sleep(5) # Let the user actually see something!
# driver.quit()
