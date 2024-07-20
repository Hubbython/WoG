from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def test_scores_service(app_url):
    try:
        driver = webdriver.Chrome()

        # Open the application URL
        driver.get(app_url)

        # Wait for page to load and find the score element
        WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, 'score')))
        score_element = driver.find_element(By.ID, 'score')

        # Get the score value and check if it's between 1 and 1000
        score = int(score_element.text.strip())
        is_valid_score = 1 <= score <= 1000

        return is_valid_score

    finally:
        driver.quit()


def main_function(app_url):
    if test_scores_service(app_url):
        print("Tests passed.")
        return 0  # Exit code 0 indicates success
    else:
        print("Tests failed.")
        return -1  # Exit code -1 indicates failure


main_function('http://flask-app:5000')

"""if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python e2e.py <application_url>")
        sys.exit(1)

    app_url = sys.argv[1]
    exit_code = main_function(app_url)
    sys.exit(exit_code)"""
#TODO understand and fix app_url / sys.argv