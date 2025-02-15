import time
from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.chrome.service import Service
def commondriver():
    servi=Service('C:/Users/m.ambujavasan/Downloads/chromedriver-win64/chromedriver-win64/chromedriver.exe')
    options=webdriver.ChromeOptions()
    options.add_argument("start-maximized")
    options.add_argument("no-sandbox")
    options.add_experimental_option("excludeSwitches",["enable-automation"])
    options.add_argument("disable-blink-features=AutomationControlled")
    driver = webdriver.Chrome(service=servi,options=options)
    return driver
def amazondata():
    driver=commondriver()
    driver.get("https://www.amazon.in/")
    search1=driver.find_element(by="xpath",value='//*[@id="twotabsearchtextbox"]')
    search1.send_keys("OnePlus Nord Buds 3")
    search1.send_keys(Keys.ENTER)
    product1=driver.find_element(by="xpath",value='/html/body/div[1]/div[1]/div[1]/div[1]/div/span[1]/div[1]/div[5]/div/div/span/div/div/div/div[2]/div/div/div[1]/a')
    product1.click()
    time.sleep(5)
    tabs = driver.window_handles
    driver.switch_to.window(tabs[1])
    driver.save_screenshot("Amazon_Buds_page.png")
    rate=driver.find_element(by="xpath",value='//*[@id="corePrice_feature_div"]/div/div/span[1]/span[2]/span[2]')
    var=rate.text
    return var
def flipkartdata():
    driver=commondriver()
    driver.get("https://www.flipkart.com/")
    searchproduct=driver.find_element(by="xpath",value='//*[@id="container"]/div/div[1]/div/div/div/div/div[1]/div/div/div/div[1]/div[1]/header/div[1]/div[2]/form/div/div/input')
    searchproduct.send_keys("OnePlus Nord Buds 3")
    searchproduct.send_keys(Keys.ENTER)
    product=driver.find_element(by="xpath",value='//*[@id="container"]/div/div[3]/div[1]/div[2]/div[2]/div/div[1]/div/a[2]')
    product.click()
    time.sleep(3)
    tabs = driver.window_handles
    driver.switch_to.window(tabs[1])
    amount=driver.find_element(by="xpath",value='//*[@id="container"]/div/div[3]/div[1]/div[2]/div[2]/div/div[4]/div[1]/div/div[1]')
    driver.save_screenshot("Flipkart_Buds_page.png")
    return amount.text
amazonrate=int(amazondata().replace(",",""))
flipkartrate=int(flipkartdata().replace("₹","").replace(",",""))
print("Rate of buds in Amazon is : ₹"+ str(amazonrate))
print("Rate of buds in Flipkart is : ₹"+ str(flipkartrate))
if amazonrate>flipkartrate:
    print("Its cheeper in Flipkart you may have a better price there")
elif amazonrate<flipkartrate:
    print("Its cheeper in Amazon you may have a better price there")
else:
    print("Its clear that both are selling in same price")