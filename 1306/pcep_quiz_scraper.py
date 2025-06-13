from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

driver = webdriver.Chrome()

driver.get("https://pcep-quiz-app-vercel.vercel.app/quiz/Grundlagen")
time.sleep(5)
question = driver.find_element(By.TAG_NAME, "p")
print(question.text)
driver.find_element(By.XPATH, "/html/body/div/div[2]/div/div/div[3]/div[1]/button").click()
time.sleep(1)
submit_button = driver.find_element(By.XPATH, "/html/body/div/div[2]/div/div/button")
submit_button.click()
next_question_button = driver.find_element(By.XPATH, "/html/body/div/div[2]/div/div/button")
next_question_button.click()
time.sleep(4)

driver.quit()
