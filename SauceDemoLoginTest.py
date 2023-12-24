from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from time import sleep

class Sauce_Demo_Login_Test:
    
#Kullanıcı adı ve şifre alanları boş geçildiğinde uyarı mesajı olarak "Epic sadface: Username is required" gösterilmelidir    
    
    def test_passing_empty(self):
        driver = webdriver.Chrome()
        driver.get("https://www.saucedemo.com")
        driver.maximize_window() 
        sleep(2)
        usernameInput = driver.find_element(By.ID,"user-name")
        usernameInput.send_keys("")
        sleep(2)
        passwordInput = driver.find_element(By.ID,"password")
        passwordInput.send_keys("")
        sleep(2)
        loginButton = driver.find_element(By.ID,"login-button")
        loginButton.click()
        sleep(2)
        errorMessage = driver.find_element(By.XPATH,"//h3[@data-test='error']")
        testResult = errorMessage.text == "Epic sadface: Username is required"
        print(f"TEST SONUCU: {testResult}")

#Sadece şifre alanı boş geçildiğinde uyarı mesajı olarak "Epic sadface: Password is required" gösterilmelidir.
        
    def test_invalid_password(self):
        driver = webdriver.Chrome()
        driver.get("https://www.saucedemo.com")
        driver.maximize_window() 
        sleep(2)
        usernameInput = driver.find_element(By.ID,"user-name")
        usernameInput.send_keys("locked_out_user")
        sleep(2)
        passwordInput = driver.find_element(By.ID,"password")
        passwordInput.send_keys("")
        sleep(2)
        loginButton = driver.find_element(By.ID,"login-button")
        loginButton.click()
        sleep(2)
        errorMessage = driver.find_element(By.XPATH,"//h3[@data-test='error']")
        testResult = errorMessage.text == "Epic sadface: Password is required"
        print(f"TEST SONUCU: {testResult}")  

#Kullanıcı adı "locked_out_user" şifre alanı "secret_sauce" gönderildiğinde "Epic sadface: Sorry, this user has been locked out." mesajı gösterilmelidir.
        
    def test_invalid_login(self):
        driver = webdriver.Chrome()
        driver.get("https://www.saucedemo.com")
        driver.maximize_window() 
        sleep(2)
        usernameInput = driver.find_element(By.ID,"user-name")
        usernameInput.send_keys("locked_out_user")
        sleep(2)
        passwordInput = driver.find_element(By.ID,"password")
        passwordInput.send_keys("secret_sauce")
        sleep(2)
        loginButton = driver.find_element(By.ID,"login-button")
        loginButton.click()
        sleep(2)
        errorMessage = driver.find_element(By.XPATH,"//h3[@data-test='error']")
        testResult = errorMessage.text == "Epic sadface: Sorry, this user has been locked out."
        print(f"TEST SONUCU: {testResult}")  

#Kullanıcı adı "standard_user" şifre "secret_sauce" gönderildiğinde kullanıcı "/inventory.html" sayfasına gönderilmelidir. 
#Giriş yapıldıktan sonra kullanıcıya gösterilen ürün sayısı "6" adet olmalıdır. 
    
    def test_product_control(self):
        driver = webdriver.Chrome()
        driver.get("https://www.saucedemo.com")
        driver.maximize_window() 
        sleep(2)
        usernameInput = driver.find_element(By.ID,"user-name")
        usernameInput.send_keys("standard_user")
        sleep(2)
        passwordInput = driver.find_element(By.ID,"password")
        passwordInput.send_keys("secret_sauce")
        sleep(2)
        loginButton = driver.find_element(By.ID,"login-button")
        loginButton.click()
        sleep(2)
        current_url = driver.current_url 
        expected_url = "https://www.saucedemo.com/inventory.html"
        if (current_url == expected_url):
            first_test = True
        else:
            first_test = False
        product = driver.find_elements(By.CLASS_NAME,"inventory_item_description")
        second_test = len(product) == 6
        if (first_test == True and second_test == True):
            print("TEST SONUCU: True")
        else:
            print("TEST SONUCU: False")

#sitedeki seçtiğin ilk ürüne tıkladığında detay sayfasına gidiliyor mu?         
class Sauce_Demo_Product_Test:
    def test_product_details(self):
        driver = webdriver.Chrome()
        driver.get("https://www.saucedemo.com")
        driver.maximize_window() 
        sleep(2)
        usernameInput = driver.find_element(By.ID,"user-name")
        usernameInput.send_keys("standard_user")
        sleep(2)
        passwordInput = driver.find_element(By.ID,"password")
        passwordInput.send_keys("secret_sauce")
        sleep(2)
        loginButton = driver.find_element(By.ID,"login-button")
        loginButton.click()
        sleep(2)
        current_url = driver.current_url 
        expected_url = "https://www.saucedemo.com/inventory.html"
        if (current_url == expected_url):
            first_test = True
        else:
            first_test = False
        first_product = driver.find_element(By.ID,"item_4_title_link")
        first_product.click()
        sleep(2)
        current_url = "https://www.saucedemo.com/inventory.html"
        expected_url = "https://www.saucedemo.com/inventory-item.html?id=4"
        if (current_url == expected_url):
            first_test = True
        else:
            first_test = False

#Sayfada iki adet ürün seçildiğinde sepet ikonu üzerindeki 2 sayısıyla seçilen ürün adeti sayısı eşit mi?

    def test_product_quantity(self):
        driver = webdriver.Chrome()
        driver.get("https://www.saucedemo.com")
        driver.maximize_window() 
        sleep(2)
        usernameInput = driver.find_element(By.ID,"user-name")
        usernameInput.send_keys("standard_user")
        sleep(2)
        passwordInput = driver.find_element(By.ID,"password")
        passwordInput.send_keys("secret_sauce")
        sleep(2)
        loginButton = driver.find_element(By.ID,"login-button")
        loginButton.click()
        sleep(2)
        current_url = driver.current_url 
        expected_url = "https://www.saucedemo.com/inventory.html"
        if (current_url == expected_url):
            first_test = True
        else:
            first_test = False
        addToCart1 = driver.find_element(By.ID,"add-to-cart-sauce-labs-backpack")
        addToCart1.click()
        sleep(1)
        addToCart2 = driver.find_element(By.ID,"add-to-cart-sauce-labs-bike-light")
        addToCart2.click()
        sleep(1)
        addToCart3 = driver.find_element(By.ID,"add-to-cart-sauce-labs-bolt-t-shirt")
        addToCart3.click()
        sleep(1)
        products = driver.find_elements(By.CLASS_NAME,"btn btn_secondary btn_small btn_inventory")
        first_test = len(products) == 3
        cart_badge = driver.find_elements(By.CLASS_NAME,"shopping_cart_badge")
        second_test = len(cart_badge) == 3
        if (first_test == second_test):
            print("TEST SONUCU: True")
        else:
            print("TEST SONUCU: False")

#Siteden hatasız bir şekilde çıkış yapılıyor mu?     

class Sauce_Demo_Logout_Test:              
    def test_logout(self):
        driver = webdriver.Chrome()
        driver.get("https://www.saucedemo.com")
        driver.maximize_window() 
        sleep(2)
        usernameInput = driver.find_element(By.ID,"user-name")
        usernameInput.send_keys("standard_user")
        sleep(2)
        passwordInput = driver.find_element(By.ID,"password")
        passwordInput.send_keys("secret_sauce")
        sleep(2)
        loginButton = driver.find_element(By.ID,"login-button")
        loginButton.click()
        sleep(2)
        current_url = driver.current_url 
        expected_url = "https://www.saucedemo.com/inventory.html"
        if (current_url == expected_url):
            first_test = True
        else:
            first_test = False
        sleep(2) 
        menuButton = driver.find_element(By.ID,"react-burger-menu-btn")
        menuButton.click()
        sleep(2)
        logoutButton = driver.find_element(By.ID,"logout_sidebar_link")
        logoutButton.click()
        sleep(2)
        driver.get("https://www.saucedemo.com")
        
#Alfabetik sıraya göre filtreleme yapılıyor mu?
        
class Sauce_Demo_Filter_Test:
    def test_filter(self):
        driver = webdriver.Chrome()
        driver.get("https://www.saucedemo.com")
        driver.maximize_window() 
        sleep(2)
        usernameInput = driver.find_element(By.ID,"user-name")
        usernameInput.send_keys("standard_user")
        sleep(2)
        passwordInput = driver.find_element(By.ID,"password")
        passwordInput.send_keys("secret_sauce")
        sleep(2)
        loginButton = driver.find_element(By.ID,"login-button")
        loginButton.click()
        sleep(2)
        current_url = driver.current_url 
        expected_url = "https://www.saucedemo.com/inventory.html"
        if (current_url == expected_url):
            first_test = True
        else:
            first_test = False
        sleep(2) 
        filterButton = driver.find_element(By.CLASS_NAME,"product_sort_container")
        filterButton.click()
        sleep(2) 
        zToa = driver.find_element(By.XPATH,"/html/body/div/div/div/div[1]/div[2]/div/span/select/option[2]")
        zToa.click()
        sleep(2)
        first_product = driver.find_element(By.ID,"item_4_title_link")
        second_product = driver.find_element(By.ID,"item_0_title_link")
        third_product = driver.find_element(By.ID,"item_1_title_link")
        forth_product = driver.find_element(By.ID,"item_5_title_link")
        fifth_product = driver.find_element(By.ID,"item_2_title_link")
        sixth_product = driver.find_element(By.ID,"item_3_title_link")
        list = ['first_product', 'second_product', 'third_product', 'forth__product', 'fifth_product', 'sixth_product']
        reverse_list = sorted(list, reverse=True)
        print(reverse_list)
    
# testClass = Sauce_Demo_Login_Test()
# testClass.test_passing_empty()
# testClass.test_invalid_password()
# testClass.test_invalid_login()
# testClass.test_product_control()
# testClass = Sauce_Demo_Product_Test()
# testClass.test_product_details()
# testClass.test_product_quantity()
# testClass = Sauce_Demo_Logout_Test()
# testClass.test_logout()
testClass = Sauce_Demo_Filter_Test()
testClass.test_filter()