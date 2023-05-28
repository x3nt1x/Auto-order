import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions

total_added = 0

options = Options()
options.add_argument('--headless')

driver = webdriver.Chrome(options=options)


def click_button():
    global total_added
    driver.get('https://www.telia.ee/lisamaht/order/8385')
    wait = WebDriverWait(driver, 10)
    button = wait.until(expected_conditions.element_to_be_clickable((By.CLASS_NAME, 'btn--order')))
    button.click()
    total_added += 15
    print("Added 15GB")


def exit_program():
    print(f"Total amount added: {total_added}GB\n")
    print(f"Exiting program...")
    driver.quit()
    exit(0)


if __name__ == '__main__':
    print("Press Ctrl + C to exit program\n")

    while True:
        try:
            click_button()
            print("Waiting 5 minutes...\n")
            time.sleep(300)
        except KeyboardInterrupt:
            exit_program()
