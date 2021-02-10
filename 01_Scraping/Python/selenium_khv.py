from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException

if __name__ == "__main__":
    driver = webdriver.Chrome()
    try:
        driver.get('https://todaykhv.ru')

        WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, '.itemNewsWrap .itemNewsHead > a')))

        newsHeads = driver.find_elements_by_css_selector('.itemNewsWrap .itemNewsHead > a')
        firstHeadText = newsHeads[0].text

        print('Главная, заголовков:', len(newsHeads))
        print('Заголовок первого элемента:', firstHeadText)

    except TimeoutException:
        print('Error')
    driver.quit()
