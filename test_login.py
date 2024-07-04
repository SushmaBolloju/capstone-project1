import time
import pytest
from selenium import webdriver
from selenium.common import NoSuchElementException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.support import expected_conditions as EC


def test_01():
    service = ChromeService(executable_path=ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service)
    driver.implicitly_wait(5)
    driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
    driver.implicitly_wait(5)
    time.sleep(3)
    driver.maximize_window()
    time.sleep(3)
    try:
        input_field = driver.find_element(By.NAME, "username")
        input_field.send_keys("Admin")
        input_field1 = driver.find_element(By.NAME, value="password")
        input_field1.send_keys("admin123")
        driver.implicitly_wait(10)
        driver.find_element(By.XPATH, value="//button[@type='submit']").click()
        print("Entered the valid login credentials")
        time.sleep(5)

    except NoSuchElementException as e:
        # Handle the case where the element is not found
        print(f"Element not found: {e}")

    except Exception as e:
        # Handle other exceptions (TimeoutException, WebDriverException, etc.)
        print(f"An error occurred: {e}")

    finally:
        # Optional: Perform cleanup or close the WebDriver instance
        driver.quit()


def test_02():
    service = ChromeService(executable_path=ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service)
    driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
    time.sleep(3)
    driver.maximize_window()
    time.sleep(3)
    driver.implicitly_wait(10)
    try:
        input_field = driver.find_element(By.NAME, "username")
        input_field.send_keys("Admin")
        input_field1 = driver.find_element(By.NAME, value="password")
        input_field1.send_keys("edmin123")
        driver.implicitly_wait(10)
        driver.find_element(By.XPATH, value="//button[@type='submit']").click()
        print("Entered the invalid login credentials")
        time.sleep(5)
    except NoSuchElementException as e:
        # Handle the case where the element is not found
        print(f"Element not found: {e}")

    except Exception as e:
        # Handle other exceptions (TimeoutException, WebDriverException, etc.)
        print(f"An error occurred: {e}")

    finally:
        # Optional: Perform cleanup or close the WebDriver instance
        driver.quit()


def test_03():
    service = ChromeService(executable_path=ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service)
    driver.implicitly_wait(5)
    driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
    driver.implicitly_wait(5)
    time.sleep(3)
    driver.maximize_window()
    time.sleep(3)
    try:
        # Wait for the username field to be visible
        username_field = WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.NAME, "username")))
        username_field.send_keys("Admin")

        # Locate and enter password
        password_field = driver.find_element(By.NAME, value="password")
        password_field.send_keys("admin123")

        # Click on the login button
        login_button = driver.find_element(By.XPATH, value="//button[@type='submit']")
        login_button.click()

        # Wait for the PIM module link to be clickable and click it
        pim_module_link = driver.find_element(By.XPATH, '//*[@id="app"]/div[1]/div[1]/aside/nav/div[2]/ul/li[2]/a')
        pim_module_link.click()

        # Click on the Add button to add a new employee
        add_employee_btn = driver.find_element(By.XPATH, '//*[@id="app"]/div[1]/div[2]/div[2]/div/div[2]/div[1]/button')
        add_employee_btn.click()
        time.sleep(3)

        # Fill in employee details
        fname = driver.find_element(By.XPATH,
                                    '//*[@id="app"]/div[1]/div[2]/div[2]/div/div/form/div[1]/div[2]/div[1]/div[1]/div/div/div[2]/div[1]/div[2]/input')
        fname.send_keys("lilly")
        Lname = driver.find_element(By.XPATH,
                                    '//*[@id="app"]/div[1]/div[2]/div[2]/div/div/form/div[1]/div[2]/div[1]/div[1]/div/div/div[2]/div[3]/div[2]/input')
        Lname.send_keys("Rosy")
        empid = driver.find_element(By.XPATH,
                                    '//*[@id="app"]/div[1]/div[2]/div[2]/div/div/form/div[1]/div[2]/div[1]/div[2]/div/div/div[2]/input')
        empid.send_keys("3456")

        # Save the employee details
        save = driver.find_element(By.XPATH, '/html/body/div/div[1]/div[2]/div[2]/div/div/form/div[2]/button[2]')
        save.click()
        time.sleep(5)
        personal_detail = driver.find_element(By.XPATH,
                                              '//*[@id="app"]/div[1]/div[2]/div[2]/div/div/div/div[1]/div[2]/div[1]/a')
        personal_detail.click()
        time.sleep(5)
        nationality = driver.find_element(By.XPATH,
                                          '//*[@id="app"]/div[1]/div[2]/div[2]/div/div/div/div[2]/div[1]/form/div[3]/div[1]/div[1]/div/div[2]/div/div/div[2]/i')
        nationality.click()
        time.sleep(5)
        n1 = driver.find_element(By.XPATH,
                                 '//*[@id="app"]/div[1]/div[2]/div[2]/div/div/div/div[2]/div[1]/form/div[3]/div[1]/div[1]/div/div[2]/div/div/div[1]')
        n1.send_keys("Namibian")
        time.sleep(5)
        n2 = driver.find_element(By.XPATH,
                                 '//*[@id="app"]/div[1]/div[2]/div[2]/div/div/div/div[2]/div[1]/form/div[3]/div[1]/div[1]/div/div[2]/div/div/div[2]/i')
        n2.click()
        time.sleep(2)

        marital_status = driver.find_element(By.XPATH,
                                             '//*[@id="app"]/div[1]/div[2]/div[2]/div/div/div/div[2]/div[1]/form/div[3]/div[1]/div[2]/div/div[2]/div/div/div[2]/i')
        marital_status.click()
        time.sleep(5)
        m1 = driver.find_element(By.XPATH,
                                 '//*[@id="app"]/div[1]/div[2]/div[2]/div/div/div/div[2]/div[1]/form/div[3]/div[1]/div[2]/div/div[2]/div/div/div[1]')
        m1.send_keys("married")
        time.sleep(5)

        otherid = driver.find_element(By.XPATH,
                                      "/html[1]/body[1]/div[1]/div[1]/div[2]/div[2]/div[1]/div[1]/div[1]/div[2]/div[1]/form[1]/div[2]/div[1]/div[2]/div[1]/div[2]/input[1]")
        otherid.send_keys("7864")
        time.sleep(2)
        licence = driver.find_element(By.XPATH,
                                      "/html[1]/body[1]/div[1]/div[1]/div[2]/div[2]/div[1]/div[1]/div[1]/div[2]/div[1]/form[1]/div[2]/div[2]/div[1]/div[1]/div[2]/input[1]")
        licence.send_keys("7941")
        time.sleep(3)
        expiry_date = driver.find_element(By.XPATH,
                                          "/html[1]/body[1]/div[1]/div[1]/div[2]/div[2]/div[1]/div[1]/div[1]/div[2]/div[1]/form[1]/div[2]/div[2]/div[2]/div[1]/div[2]/div[1]/div[1]/input[1]")
        expiry_date.send_keys("2024-04-05")
        time.sleep(5)
        birth_date = driver.find_element(By.XPATH,
                                         "/html[1]/body[1]/div[1]/div[1]/div[2]/div[2]/div[1]/div[1]/div[1]/div[2]/div[1]/form[1]/div[3]/div[2]/div[1]/div[1]/div[2]/div[1]/div[1]/input[1]")
        birth_date.send_keys("1992-10-12")
        time.sleep(2)
        gender = driver.find_element(By.XPATH,
                                     "//label[normalize-space()='Male']//span[@class='oxd-radio-input oxd-radio-input--active --label-right oxd-radio-input']")
        gender.click()

        time.sleep(2)
        # saving the details
        driver.find_element(By.XPATH,
                            "//div[@class='orangehrm-horizontal-padding orangehrm-vertical-padding']//button[@type='submit'][normalize-space()='Save']").click()
        time.sleep(3)


    except NoSuchElementException as e:
        print(f"Element not found: {e}")
        raise  # Re-raise the exception

    except Exception as e:
        print(f"An error occurred during login: {e}")
        raise  # Re-raise the exception
    finally:
        # Optional: Perform cleanup or close the WebDriver instance
        driver.quit()


def test_04():
    service = ChromeService(executable_path=ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service)
    driver.get("https://opensource-demo.orangehrmlive.com/")
    time.sleep(3)
    driver.maximize_window()
    time.sleep(3)
    try:
        driver.find_element(By.NAME, value="username").send_keys("Admin")
        time.sleep(2)
        driver.find_element(By.NAME, value="password").send_keys("admin123")
        time.sleep(2)
        driver.find_element(By.XPATH, value="//button[@type='submit']").click()
        time.sleep(4)
        driver.find_element(By.LINK_TEXT, value="PIM").click()
        time.sleep(5)
        driver.find_element(By.LINK_TEXT, value="Employee List").click()
        time.sleep(5)
        driver.find_element(By.XPATH, value="(//i[@class='oxd-icon bi-pencil-fill'])[1]").click()
        time.sleep(5)
        driver.find_element(By.NAME, value="firstName").clear()
        time.sleep(5)
        driver.find_element(By.NAME, value="firstName").send_keys("Priyanka")
        time.sleep(5)
        driver.find_element(By.NAME, value="middleName").clear()
        time.sleep(3)
        driver.find_element(By.NAME, value="middleName").send_keys("Magesh")
        time.sleep(3)
        driver.find_element(By.NAME, value="lastName").clear()
        time.sleep(2)
        driver.find_element(By.NAME, value="lastName").send_keys("K")
        time.sleep(2)
        driver.find_element(By.XPATH, "(//button[@type='submit'])[1]").click()
        time.sleep(2)
        driver.find_element(By.XPATH, "(//button[@type='submit'])[2]").click()


    except NoSuchElementException as e:
        print(f"Element not found: {e}")
        raise  # Re-raise the exception

    except Exception as e:
        print(f"An error occurred during login: {e}")
        raise  # Re-raise the exception
    finally:
        # Optional: Perform cleanup or close the WebDriver instance
        driver.quit()


def test_05():
    service = ChromeService(executable_path=ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service)
    driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
    time.sleep(3)
    driver.maximize_window()
    time.sleep(3)
    try:
        driver.find_element(By.NAME, value="username").send_keys("Admin")
        time.sleep(2)
        driver.find_element(By.NAME, value="password").send_keys("admin123")
        time.sleep(2)
        driver.find_element(By.XPATH, value="//button[@type='submit']").click()
        time.sleep(4)
        driver.find_element(By.LINK_TEXT, value="PIM").click()
        time.sleep(5)
        driver.find_element(By.LINK_TEXT, value="Employee List").click()
        time.sleep(5)
        driver.find_element(By.XPATH, value="(//i[@class='oxd-icon bi-trash'])[1]").click()
        time.sleep(5)
        driver.find_element(By.XPATH,value="//button[@class='oxd-button oxd-button--medium oxd-button--label-danger orangehrm-button-margin']").click()
        time.sleep(5)


    except NoSuchElementException as e:
        print(f"Element not found: {e}")
        raise  # Re-raise the exception

    except Exception as e:
        print(f"An error occurred during login: {e}")
        raise  # Re-raise the exception
    finally:
        # Optional: Perform cleanup or close the WebDriver instance
        driver.quit()