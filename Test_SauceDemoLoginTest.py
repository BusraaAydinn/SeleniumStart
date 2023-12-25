from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from time import sleep
from selenium.webdriver.support.wait import WebDriverWait #ilgili driverı bekleten yapı
from selenium.webdriver.support import expected_conditions as ec #beklenen koşullar
import pytest

#Kullanıcı adı ve şifre alanları boş geçildiğinde uyarı mesajı olarak "Epic sadface: Username is required" gösterilmelidir  

class Test_Sauce_Demo_Login_Test:  
        #prefix => test_ 
    def setup_method(self): #her test başlangıcında çalışacak fonk
        self.driver = webdriver.Chrome()
        self.driver.get("https://www.saucedemo.com")
        self.driver.maximize_window() 
    
    def teardown_method(self): # her testinin bitiminde çalışacak fonk
        self.driver.quit()
    
    def test_passing_empty(self):
        usernameInput = WebDriverWait(self.driver,2).until(ec.visibility_of_element_located((By.ID,"user-name")))
        usernameInput.send_keys("")
        passwordInput = WebDriverWait(self.driver,2).until(ec.visibility_of_element_located((By.ID,"password")))
        passwordInput.send_keys("")
        loginButton = WebDriverWait(self.driver,2).until(ec.visibility_of_element_located((By.ID,"login-button")))
        loginButton.click()
        errorMessage = WebDriverWait(self.driver,2).until(ec.visibility_of_element_located((By.XPATH,"//h3[@data-test='error']")))
        assert errorMessage.text == "Epic sadface: Username is required"
        

#Sadece şifre alanı boş geçildiğinde uyarı mesajı olarak "Epic sadface: Password is required" gösterilmelidir.
        
    def test_invalid_password(self):
        usernameInput = WebDriverWait(self.driver,2).until(ec.visibility_of_element_located((By.ID,"user-name")))
        usernameInput.send_keys("locked_out_user")
        passwordInput = WebDriverWait(self.driver,2).until(ec.visibility_of_element_located((By.ID,"password")))
        passwordInput.send_keys("")
        loginButton = WebDriverWait(self.driver,2).until(ec.visibility_of_element_located((By.ID,"login-button")))
        loginButton.click()
        errorMessage = WebDriverWait(self.driver,2).until(ec.visibility_of_element_located((By.XPATH,"//h3[@data-test='error']")))
        assert errorMessage.text == "Epic sadface: Password is required"
        

#Kullanıcı adı "locked_out_user" şifre alanı "secret_sauce" gönderildiğinde "Epic sadface: Sorry, this user has been locked out." mesajı gösterilmelidir.
        
    def test_invalid_login(self):
        usernameInput = WebDriverWait(self.driver,2).until(ec.visibility_of_element_located((By.ID,"user-name")))
        usernameInput.send_keys("locked_out_user")
        passwordInput = WebDriverWait(self.driver,2).until(ec.visibility_of_element_located((By.ID,"password")))
        passwordInput.send_keys("secret_sauce")
        loginButton = WebDriverWait(self.driver,2).until(ec.visibility_of_element_located((By.ID,"login-button")))
        loginButton.click()
        errorMessage = WebDriverWait(self.driver,2).until(ec.visibility_of_element_located((By.XPATH,"//h3[@data-test='error']")))
        assert errorMessage.text == "Epic sadface: Sorry, this user has been locked out."
        

#Kullanıcı adı "standard_user" şifre "secret_sauce" gönderildiğinde kullanıcı "/inventory.html" sayfasına gönderilmelidir. 
#Giriş yapıldıktan sonra kullanıcıya gösterilen ürün sayısı "6" adet olmalıdır. 
    
    def test_product_control(self):
        usernameInput = WebDriverWait(self.driver,2).until(ec.visibility_of_element_located((By.ID,"user-name")))
        usernameInput.send_keys("standard_user")
        passwordInput = WebDriverWait(self.driver,2).until(ec.visibility_of_element_located((By.ID,"password")))
        passwordInput.send_keys("secret_sauce")
        loginButton = WebDriverWait(self.driver,2).until(ec.visibility_of_element_located((By.ID,"login-button")))
        loginButton.click()
        current_url = self.driver.current_url 
        expected_url = "https://www.saucedemo.com/inventory.html"
        if (current_url == expected_url):
            first_test = True
        else:
            first_test = False
        product = WebDriverWait(self.driver,2).until(ec.visibility_of_all_elements_located((By.CLASS_NAME,"inventory_item_description")))
        second_test = len(product) == 6
        if (first_test == True and second_test == True):
            assert True
        else:
            assert False

#Sitedeki seçtiğin ilk ürüne tıkladığında detay sayfasına gidiliyor mu?  
                   
class Test_Sauce_Demo_Product_Test:
        #prefix => test_ 
    def setup_method(self): #her test başlangıcında çalışacak fonk
        self.driver = webdriver.Chrome()
        self.driver.get("https://www.saucedemo.com")
        self.driver.maximize_window() 
    
    def teardown_method(self): # her testinin bitiminde çalışacak fonk
        self.driver.quit()
    
    def test_product_details(self):
        usernameInput = WebDriverWait(self.driver,2).until(ec.visibility_of_element_located((By.ID,"user-name")))
        usernameInput.send_keys("standard_user")
        passwordInput = WebDriverWait(self.driver,2).until(ec.visibility_of_element_located((By.ID,"password")))
        passwordInput.send_keys("secret_sauce")
        loginButton = WebDriverWait(self.driver,2).until(ec.visibility_of_element_located((By.ID,"login-button")))
        loginButton.click()
        current_url = self.driver.current_url 
        expected_url = "https://www.saucedemo.com/inventory.html"
        if (current_url == expected_url):
            first_test = True
        else:
            first_test = False
        first_product = WebDriverWait(self.driver,2).until(ec.visibility_of_element_located((By.ID,"item_4_title_link")))
        first_product.click()
        current_url = self.driver.current_url 
        expected_url = "https://www.saucedemo.com/inventory-item.html?id=4"
        if (current_url == expected_url):
            assert True
        else:
            assert False

#Sayfada üç adet ürün seçildiğinde sepet ikonu üzerindeki üç sayısıyla seçilen ürün adeti sayısı eşit mi?

    def test_product_quantity(self):
        usernameInput = WebDriverWait(self.driver,2).until(ec.visibility_of_element_located((By.ID,"user-name")))
        usernameInput.send_keys("standard_user")
        passwordInput = WebDriverWait(self.driver,2).until(ec.visibility_of_element_located((By.ID,"password")))
        passwordInput.send_keys("secret_sauce")
        loginButton = WebDriverWait(self.driver,2).until(ec.visibility_of_element_located((By.ID,"login-button")))
        loginButton.click()

        current_url = self.driver.current_url 
        expected_url = "https://www.saucedemo.com/inventory.html"
        if (current_url == expected_url):
            assert True
        else:
            assert False
        addToCart1 = WebDriverWait(self.driver,2).until(ec.visibility_of_element_located((By.ID,"add-to-cart-sauce-labs-backpack")))
        addToCart1.click()
        addToCart2 = WebDriverWait(self.driver,2).until(ec.visibility_of_element_located((By.ID,"add-to-cart-sauce-labs-bike-light")))
        addToCart2.click()
        addToCart3 = WebDriverWait(self.driver,2).until(ec.visibility_of_element_located((By.ID,"add-to-cart-sauce-labs-bolt-t-shirt")))
        addToCart3.click()
        # products = WebDriverWait(self.driver,2).until(ec.visibility_of_element_located((By.CLASS_NAME,"btn btn_secondary btn_small btn_inventory")))
        # first_test = len(products) == 3
        cart_badge = WebDriverWait(self.driver,2).until(ec.visibility_of_element_located((By.CLASS_NAME,"shopping_cart_badge"))).text
        if (cart_badge =="3"):
            assert True
        else:
            assert False
        

#Siteden hatasız bir şekilde çıkış yapılıyor mu?     

class Test_Sauce_Demo_Logout_Test:              
        #prefix => test_ 
    def setup_method(self): #her test başlangıcında çalışacak fonk
        self.driver = webdriver.Chrome()
        self.driver.get("https://www.saucedemo.com")
        self.driver.maximize_window() 
    
    def teardown_method(self): # her testinin bitiminde çalışacak fonk
        self.driver.quit()
    
    def test_logout(self):
        usernameInput = WebDriverWait(self.driver,2).until(ec.visibility_of_element_located((By.ID,"user-name")))
        usernameInput.send_keys("standard_user")
        passwordInput = WebDriverWait(self.driver,2).until(ec.visibility_of_element_located((By.ID,"password")))
        passwordInput.send_keys("secret_sauce")
        loginButton = WebDriverWait(self.driver,2).until(ec.visibility_of_element_located((By.ID,"login-button")))
        loginButton.click()
        current_url = self.driver.current_url 
        expected_url = "https://www.saucedemo.com/inventory.html"
        if (current_url == expected_url):
            first_test = True
        else:
            first_test = False
        menuButton = WebDriverWait(self.driver,2).until(ec.visibility_of_element_located((By.ID,"react-burger-menu-btn")))
        menuButton.click()
        logoutButton = WebDriverWait(self.driver,2).until(ec.visibility_of_element_located((By.ID,"logout_sidebar_link")))
        logoutButton.click()
        current_url_2 = self.driver.current_url
        expected_url = "https://www.saucedemo.com/" 
        assert current_url_2 == expected_url
        
#Alfabetik sıraya göre filtreleme yapılıyor mu?
        
class Test_Sauce_Demo_Filter_Test:
        #prefix => test_ 
    def setup_method(self): #her test başlangıcında çalışacak fonk
        self.driver = webdriver.Chrome()
        self.driver.get("https://www.saucedemo.com")
        self.driver.maximize_window() 
    
    def teardown_method(self): # her testinin bitiminde çalışacak fonk
        self.driver.quit()
    
    def test_filter(self):
        usernameInput = WebDriverWait(self.driver,2).until(ec.visibility_of_element_located((By.ID,"user-name")))
        usernameInput.send_keys("standard_user")
        passwordInput = WebDriverWait(self.driver,2).until(ec.visibility_of_element_located((By.ID,"password")))
        passwordInput.send_keys("secret_sauce")
        loginButton = WebDriverWait(self.driver,2).until(ec.visibility_of_element_located((By.ID,"login-button")))
        loginButton.click()
        current_url = self.driver.current_url 
        expected_url = "https://www.saucedemo.com/inventory.html"
        if (current_url == expected_url):
            assert True
        else:
            assert False
        filterButton = WebDriverWait(self.driver,2).until(ec.visibility_of_element_located((By.CLASS_NAME,"product_sort_container")))
        filterButton.click()
        zToa = WebDriverWait(self.driver,2).until(ec.visibility_of_element_located((By.XPATH,"/html/body/div/div/div/div[1]/div[2]/div/span/select/option[2]")))
        zToa.click()
        first_product = WebDriverWait(self.driver,2).until(ec.visibility_of_element_located((By.ID,"item_4_title_link"))).text
        second_product = WebDriverWait(self.driver,2).until(ec.visibility_of_element_located((By.ID,"item_0_title_link"))).text
        third_product = WebDriverWait(self.driver,2).until(ec.visibility_of_element_located((By.ID,"item_1_title_link"))).text
        forth_product = WebDriverWait(self.driver,2).until(ec.visibility_of_element_located((By.ID,"item_5_title_link"))).text
        fifth_product = WebDriverWait(self.driver,2).until(ec.visibility_of_element_located((By.ID,"item_2_title_link"))).text
        sixth_product = WebDriverWait(self.driver,2).until(ec.visibility_of_element_located((By.ID,"item_3_title_link"))).text
        list = [first_product, second_product, third_product, forth_product, fifth_product, sixth_product]
        reverse_list = sorted(list, reverse=True)
        assert reverse_list
    
# testClass = Sauce_Demo_Login_Test()
# testClass.test_passing_empty()
# testClass.test_invalid_password()
# testClass.test_invalid_login()
# testClass.test_product_control()
# ProductTest = Sauce_Demo_Product_Test()
# ProductTest.test_product_details()
# ProductTest.test_product_quantity()
# LogoutTest = Sauce_Demo_Logout_Test()
# LogoutTest.test_logout()
# FilterTest = Sauce_Demo_Filter_Test()
# FilterTest.test_filter()
