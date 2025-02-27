import chromedriver_autoinstaller
from selenium import webdriver
from selenium.webdriver.common.by import By

opt = webdriver.ChromeOptions()
chromedriver_autoinstaller.install()


def test_scores_service(app_url):
    driver = webdriver.Firefox()
    driver.get(app_url)
    findscore = driver.find_element(By.ID, "score").text
    driver.quit()
    if 1 <= int(findscore) <= 1000:
        return True
    else:
        return False


def main_function():
    flask_url = "http://127.0.0.1:5000"
    if test_scores_service(flask_url):
        exit()
    else:
        exit(-1)

