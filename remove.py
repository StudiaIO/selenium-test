def removeTest(driver):
    driver.get("http://localhost/projekt/public/usersBooking")
    driver.find_element_by_link_text("Anuluj rezerwacje").click()
    print(driver.switch_to.alert.text)
    driver.switch_to.alert.accept()
    assert "Szukaj noclegu" == driver.title
    print("Succesfully removed")

