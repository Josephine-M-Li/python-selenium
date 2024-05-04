"""連續登入10次"""

import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


urls = ["http://test.hixcare.tw/login/signIn"]
s = Service(
    r"C:\Users\rayli\Desktop\test\Lib\site-packages\chromedriver\chromedriver.exe"
)


for url in urls:
    driver = webdriver.Chrome(service=s)
    driver.get(url)
  
wait = WebDriverWait(driver, 10, 2)
wait.until(EC.url_matches("http://test.hixcare.tw/login/signIn"))  # 判断url是否存在

for i in range(10):

    #判断username、password是否存在        
    wait.until(EC.visibility_of_element_located((By.ID, "username")))
    wait.until(EC.visibility_of_element_located((By.ID, "password")))
    wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, r"#app>div>div>div:nth-child(2)>div>div:nth-child(4)>select")))

    # 取得 id 為 ausername 的網頁元素 --> 使用者名稱( 請輸入員工工號 )
    a = driver.find_element(
        By.ID, "username")
    
    # 取得 id 為 password 的網頁元素 --> 密碼
    b = driver.find_element(By.ID, "password")  
    
    # 輸入帳密
    a.send_keys("hixadmin")
    b.send_keys("Hix1234")

    # 登入按鈕
    button = driver.find_element(
        By.CSS_SELECTOR, r"#app > div>div:nth-child(1)>div:nth-child(2)>div>button"
    )  
    button.click()
   
    # 判断主頁url是否存在
    wait.until(EC.url_matches("http://test.hixcare.tw/dashboard"))  

    # 判断profile按鈕是否存在   
    locator_sysadmin = (By.CSS_SELECTOR, r'#app>div>div:nth-child(1)>div:nth-child(1)>div:nth-child(3)>div:nth-child(5)>button')
    wait.until(EC.visibility_of_element_located(locator_sysadmin))    

    # profile按鈕
    e=driver.find_element(*locator_sysadmin)
    e.click()
    
    locator_logout = (By.CSS_SELECTOR, r'#app>div>div>div>div:nth-child(3)>div:nth-child(5)>div:nth-child(2)>button:nth-child(5)')
    
    # 判断登出按鈕是否存在
    #locator_logout = (By.CSS_SELECTOR, r'#app > div > div.px-5.bg-gray-200.dark\:bg-gray-900.hix-header-v2-height > div.flex.justify-between.items-center > div.flex.justify-end.items-center > div:nth-child(5) > div > button.bg-gray-200.my-1.py-1.w-full.font-semibold.text-center.text-gray-800.rounded.hover\:bg-gray-300')
    wait.until(EC.visibility_of_element_located(locator_logout))    
    
    # 登出
    f=driver.find_element(*locator_logout)
    f.click()

    # 回到登入頁(判断登入頁url是否存在)
    wait.until(EC.url_matches("http://test.hixcare.tw/login/signIn"))  

    print(i)

time.sleep(10)
driver.quit()



