from login import loginTest
from register import registerTest
from book import bookTest
from delete import deleteTest
from logout import logoutTest
import os
from selenium import webdriver


def main():
    path = os.path.abspath('webdriver/msedgedriver.exe')
    driver = webdriver.Edge(executable_path=path)
    loginName = "test1"
    password = "test1"

    print("Register; login; booking test...")
    registerTest("test1@test1.pl", loginName, "Test1 Test1", password, "223456789", driver)
    loginTest(loginName, password, driver)
    bookTest(driver)
    logoutTest(driver)

    print("Admin login, ")
    loginTest("admin", "admin", driver)
    deleteTest(driver)
    logoutTest(driver)


if __name__ == "__main__":
    main()
