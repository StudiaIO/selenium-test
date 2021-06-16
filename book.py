from selenium import webdriver


def bookTest(driver):
    driver.get('http://localhost/projekt/public/panel')
    assert "Szukaj noclegu" == driver.title
    driver.find_element_by_link_text("Zarezerwuj").click()
    driver.find_element_by_name("chceck_in_date").click()
    driver.find_element_by_name("chceck_in_date").send_keys("20062021")
    driver.find_element_by_name("chceck_out_date").click()
    driver.find_element_by_name("chceck_out_date").send_keys("25062021")
    driver.find_element_by_xpath("//input[@type='submit' and @value='Rezerwuj']").click()
    driver.get('http://localhost/projekt/public/usersBooking')
    driver.find_element_by_link_text("Zobacz").click()
    assert "Miejsce" in driver.title
    print("Booked succesfully")
