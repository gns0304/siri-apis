import re
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class Investing:

    @staticmethod
    def get_finance_data(type, code):
        try:
            options = webdriver.ChromeOptions()
            options.add_argument('headless')
            options.add_argument('--no-sandbox')
            options.add_argument('--disable-dev-shm-usage')
            driver = webdriver.Chrome(ChromeDriverManager().install(), options=options)


            wait = WebDriverWait(driver, 5)
            driver.get("https://kr.investing.com/{}/{}".format(type, code))
            wait.until(EC.visibility_of_element_located((By.XPATH, '//*[@id="__next"]/div/div/div/div[2]/main/div/div[1]/div[1]/h1')))

            title = driver.find_element(By.XPATH, '//*[@id="__next"]/div/div/div/div[2]/main/div/div[1]/div[1]/h1').text
            quote = driver.find_element(By.XPATH, '//*[@id="__next"]/div/div/div/div[2]/main/div/div[1]/div[2]/div[1]/span').text
            point = driver.find_element(By.XPATH, '//*[@id="__next"]/div/div/div/div[2]/main/div/div[1]/div[2]/div[1]/div[2]/span[1]').text
            percent = driver.find_element(By.XPATH, '//*[@id="__next"]/div/div/div/div[2]/main/div/div[1]/div[2]/div[1]/div[2]/span[2]').text

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

        except Exception as e:

            return {
                "state": "Failed",
                "data": e
            }



if __name__ == '__main__':

    print(Investing.get_finance_data("https://kr.investing.com/currencies/usd-krw"))

