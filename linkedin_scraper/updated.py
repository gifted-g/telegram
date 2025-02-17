from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
import time
import os

# Get the directory of the current file
current_dir = os.path.dirname(os.path.abspath(__file__))
CHROME_DRIVER_PATH = os.path.join(current_dir, "chromedriver.exe")

# Set up Selenium WebDriver
options = Options()
options.headless = True  # Run browser in headless mode
driver = webdriver.Chrome(service=Service(CHROME_DRIVER_PATH), options=options)

# Function to log in to LinkedIn
def linkedin_login(username, password):
    driver.get("https://www.linkedin.com/login")
    time.sleep(8)  # Wait for the login page to load
    email_field = driver.find_element(By.ID, "username")
    password_field = driver.find_element(By.ID, "password")
    login_button = driver.find_element(By.XPATH, "//button[@aria-label='Sign in' and @type='submit']")

    email_field.send_keys(username)
    password_field.send_keys(password)
    login_button.click()
    time.sleep(5)  # Wait for the login to complete

# Function to extract job URLs
def extract_job_urls(company_url):
    driver.get(company_url)
    time.sleep(5)  # Wait for the page to load

    job_links = []

    # Locate job cards
    job_cards = driver.find_elements(By.CSS_SELECTOR, 'a.job-card-square__link')
    
    for card in job_cards:
        job_url = card.get_attribute('href')
        if job_url:
            job_links.append(job_url)

    # Check for pagination and extract links from all pages
    try:
        while True:
            next_button = driver.find_element(By.XPATH, "//button[@aria-label='Next']")
            if next_button:
                next_button.click()
                time.sleep(5)  # Wait for the next page to load
                job_cards = driver.find_elements(By.CSS_SELECTOR, 'a.job-card-square__link')
                for card in job_cards:
                    job_url = card.get_attribute('href')
                    if job_url:
                        job_links.append(job_url)
            else:
                break
    except Exception:
        pass  # No pagination or error in pagination handling

    return job_links

# Example usage
if __name__ == "__main__":
    linkedin_username = "your_email@example.com"
    linkedin_password = "your_password"

    linkedin_login(linkedin_username, linkedin_password)

    company_jobs_url = "https://www.linkedin.com/company/bellwoodconsulting/jobs/"
    job_post_urls = extract_job_urls(company_jobs_url)
    print("Extracted Job URLs:")
    for url in job_post_urls:
        print(url)

    # Close the browser
    driver.quit()
