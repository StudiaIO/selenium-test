def registerTest(email, loginName, name, password, phone, driver):
    driver.get('http://localhost/projekt/public/')
    driver.find_element_by_name("rejestruj").click()
    title = driver.title
    assert 'Rejestracja' == title
    driver.find_element_by_name("email").send_keys(email)
    driver.find_element_by_name("login").send_keys(loginName)
    driver.find_element_by_name("name").send_keys(name)
    driver.find_element_by_name("password").send_keys(password)
    driver.find_element_by_name("mobile").send_keys(phone)
    driver.find_element_by_name("create").click()
    title = driver.title
    assert 'Zaloguj się' == title
    print("Succesfully registered", loginName)
