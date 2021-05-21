# Add thư viện
from selenium import webdriver
import time
from selenium.webdriver.common.action_chains import ActionChains
# Tắt thông báo từ chrome
chrome_options = webdriver.ChromeOptions()
prefs = {"profile.default_content_setting_values.notifications": 2}
chrome_options.add_experimental_option("prefs", prefs)
driver = webdriver.Chrome(chrome_options = chrome_options)
# Phóng to màn hình
driver.maximize_window()
# Vào facebook
driver.get("https://www.facebook.com/")
# Nhập email
driver.find_element_by_id("email").send_keys("")
time.sleep(2)
# Nhập mật khẩu
driver.find_element_by_id("pass").send_keys("")
time.sleep(2)
# Đăng nhập
driver.find_element_by_name("login").click()
time.sleep(2)
# Cuộn màn hình
driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
time.sleep(2)
# Lấy tất cả element của nút Like
likes = driver.find_elements_by_xpath("//div[@class='tvfksri0 ozuftl9m']//div[@aria-label='Thích']")
actions = ActionChains(driver)
print(len(likes))
time.sleep(2)
# Like 5 bài viết đầu tiên
for i in range(0, 5):
    actions.move_to_element(likes[i]).perform()
    driver.execute_script("arguments[0].click();", likes[i])
    time.sleep(2)

   #khi sửa trên này thì sẽ pull nó 
# Like 5 bài viết đầu tiên (bỏ bài số 1)
# for i in range(1, 5):
#     actions.move_to_element(likes[i]).perform()
#     driver.execute_script("arguments[0].click();", likes[i])
#     time.sleep(2)

driver.quit()
