import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

link = "https://cvetok39.ru/"

def test_calculator_1(browser):
    browser.get(link)

    # Ищем первую кнопку для выбора цвета букета
    button_choice_color = WebDriverWait(browser, 5).until(EC.element_to_be_clickable((By.XPATH, "(//button[@class='flower-params__trigger'])[1]")))
    button_choice_color.click()
    
    # Выбираем цвет - Белый
    button_name_color = WebDriverWait(browser, 5).until(EC.element_to_be_clickable((By.XPATH, "(//button[@class='flower-params__dropdown-button flower-params__dropdown-button_colors'])[2]")))
    text_parameter_flower_choice_color = button_name_color.text
    button_name_color.click()

    # Выбираем высоту - 50 см
    button_value_height = browser.find_element(By.XPATH, "(//button[@class='flower-params__dropdown-button'])[2]")
    text_parameter_flower_choice_height = button_value_height.text
    button_value_height.click()

    # Нажимаем на кнопку "Подарить"
    button_present = WebDriverWait(browser, 5).until(EC.element_to_be_clickable((By.XPATH, "//button[text()='Подарить']")))
    button_present.click()

    # Проверяем корректность цвета и высоты букета в корзине
    parameter_flower_color = WebDriverWait(browser, 15).until(EC.element_to_be_clickable((By.XPATH, "(//div[@class='order-structure__params-group default-text']/dd[@class='order-structure__params-value'])[2]")))
    text_height = parameter_flower_color.text
    assert text_height == text_parameter_flower_choice_color, "Значения разные"

    parameter_flower_height = WebDriverWait(browser, 15).until(EC.element_to_be_clickable((By.XPATH, "(//div[@class='order-structure__params-group default-text']/dd[@class='order-structure__params-value'])[1]")))
    text_height = parameter_flower_height.text
    assert text_height == text_parameter_flower_choice_height, "Значения разные"
