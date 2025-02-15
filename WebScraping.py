import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
def scrapper():
    servi=Service('C:/Users/m.ambujavasan/Downloads/chromedriver-win64/chromedriver-win64/chromedriver.exe')
    options=webdriver.ChromeOptions()
    options.add_argument("start-maximized")
    options.add_argument("no-sandbox")
    options.add_experimental_option("excludeSwitches",["enable-automation"])
    options.add_argument("disable-blink-features=AutomationControlled")
    driver = webdriver.Chrome(service=servi,options=options)
    driver.get("https://automated.pythonanywhere.com/")
    return driver
def numberparser(text):
    output=float(text.split(": ")[1])
    return output
def main():
    driver=scrapper()
    my_list=[]
    for x in range(5):
        text = driver.find_element(by="xpath",value="/html/body/div[1]/div/h1[2]")
        time.sleep(2)
        my_list.insert(x,numberparser(text.text))
    return my_list
my_list=list(main())
print(my_list)
with open("Output.txt","w") as file:
    for i in my_list:
        file.write(str(i)+ "\n")
    file.write("Thats it bro..!")