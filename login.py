def loginTest(loginName, password, driver):
    driver.get('http://localhost/projekt/public/')
    driver.find_element_by_name("loguj").click()
    title = driver.title
    assert 'Zaloguj się' == title
    driver.find_element_by_name("login").send_keys(loginName)
    driver.find_element_by_name("password").send_keys(password)
    driver.find_element_by_name("zaloguj").click()
    title = driver.title
    assert 'Szukaj noclegu' == title
    print(loginName, "succesfully logged in")
