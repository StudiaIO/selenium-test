def deleteTest(driver):
    driver.get("http://localhost/projekt/public/main")
    driver.find_element_by_link_text("Opcje").click()
    driver.find_element_by_link_text("Edytuj użytkowników").click()
    assert "Zarządzanie użytkownikami" == driver.title
    driver.find_element_by_name("l132").click()
    driver.find_element_by_name("u132").click()
    print(driver.switch_to.alert.text)
    driver.switch_to.alert.accept()
    print("Succesfully deleted")

