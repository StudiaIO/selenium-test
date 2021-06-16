def logoutTest(driver):
    driver.get("http://localhost/projekt/public/main")
    driver.find_element_by_link_text("Opcje").click()
    driver.find_element_by_link_text("Wyloguj").click()
    assert "Noclegi" == driver.title
    print("Logout succesfully")
