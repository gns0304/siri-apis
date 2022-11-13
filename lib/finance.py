import re
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service

class Yahoo:

    @staticmethod
    def get_finance_data(code):
        # try:
        options = webdriver.ChromeOptions()
        options.add_argument('--headless')
        options.add_argument('--no-sandbox')
        options.add_argument('--disable-dev-shm-usage')
        driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)

        wait = WebDriverWait(driver, 5)

        driver.get("https://finance.yahoo.com/quote/{}".format(code))
        wait.until(EC.visibility_of_element_located((By.XPATH, '//*[@id="quote-header-info"]/div[3]/div[1]/div/fin-streamer[1]')))

        title = driver.find_element(By.XPATH, '//*[@id="quote-header-info"]/div[2]/div[1]/div[1]/h1').text
        quote = driver.find_element(By.XPATH, '//*[@id="quote-header-info"]/div[3]/div[1]/div/fin-streamer[1]').text
        point = driver.find_element(By.XPATH, '//*[@id="quote-header-info"]/div[3]/div[1]/div/fin-streamer[2]').text
        percent = driver.find_element(By.XPATH, '//*[@id="quote-header-info"]/div[3]/div[1]/div/fin-streamer[3]').text

        quote = float(re.sub(r'[^0-9.]', "", quote))
        point = float(point)
        percent = float(re.sub(r'[^0-9.+-]', '', percent))

        driver.close()

        return {
            "state": "Success",
            "data": {
                "instrument-name": title,
                "instrument-price-last": quote,
                "instrument-price_change-value": point,
                "instrument-price-change-percent": percent
            }
        }

        # except Exception as e:
        #
        #     return {
        #         "state": "Failed",
        #         "data": e
        #     }


if __name__ == '__main__':
    print(Yahoo.get_finance_data("^IXIC"))