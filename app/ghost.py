import time
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
import urllib3
import urllib.request
from PIL import Image, ImageTk


# driver = webdriver.Chrome(ChromeDriverManager().install())
# driver.get('https://python.org')
# html = driver.page_source
# print(html)
# input("sdsd")
# driver.quit()


driver = webdriver.PhantomJS()
driver.get('https://sci-hub.se/')
driver.set_window_size(1300, 550)
images = driver.find_elements_by_tag_name('img')

for image in images:
    src = image.get_attribute('src')    
    urllib.request.urlretrieve(src, "../imagens/image.png")
    im = Image.open("../imagens/image.png")
    im.show()    
    # print(src)
    

driver.quit()
