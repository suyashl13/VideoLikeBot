from selenium import webdriver
import time
from selenium.webdriver.common.keys import Keys

driver = webdriver.Edge(executable_path="./drivers/msedgedriver.exe")

print('Opening stackoverflow.com to perform external login...')
driver.get('https://stackoverflow.com/')
time.sleep(3)
login_btn = driver.find_element_by_xpath('/html/body/header/div/ol[2]/li[2]/a[1]').click()
time.sleep(3)
print('Performing wait of 3 seconds to create human login like scenario.')

print('Starting login process..')
google_login_btn = driver.find_element_by_xpath('/html/body/div[4]/div[2]/div/div[2]/button[1]').click()
time.sleep(2)
driver.find_element_by_xpath(
    '/html/body/div[1]/div[1]/div[2]/div/div[2]/div/div/div[2]/div/div[1]/div/form/span/section/div/div/div[1]/div/div[1]/div/div[1]/input').send_keys(
    'email')
time.sleep(3)
driver.find_element_by_xpath(
    '/html/body/div[1]/div[1]/div[2]/div/div[2]/div/div/div[2]/div/div[2]/div/div[1]/div/div/button/div[2]').click()

i = 5
print('Performing wait of 5 seconds to create humans login like scenario.')
while i > 0:
    print(i)
    time.sleep(1)
    i -= 1


print('Password Entered')
driver.find_element_by_xpath(
    '/html/body/div[1]/div[1]/div[2]/div/div[2]/div/div/div[2]/div/div[1]/div/form/span/section/div/div/div[1]/div[1]/div/div/div/div/div[1]/div/div[1]/input').send_keys(
    'password')
driver.find_element_by_xpath(
        '/html/body/div[1]/div[1]/div[2]/div/div[2]/div/div/div[2]/div/div[2]/div/div[1]/div/div/button/div[2]').click()
time.sleep(5)
print('Bot login Sucessfull...')


print('Redirecting to : https://www.youtube.com/c/HiteshChoudharydotcom/videos')
driver.get('https://www.youtube.com/c/HiteshChoudharydotcom/videos')
time.sleep(5)

print('Starting video like')

videos = 960
counter = 0
while True:
    driver.find_element_by_xpath(
        f'/html/body/ytd-app/div/ytd-page-manager/ytd-browse/ytd-two-column-browse-results-renderer/div[1]/ytd-section-list-renderer/div[2]/ytd-item-section-renderer/div[3]/ytd-grid-renderer/div[1]/ytd-grid-video-renderer[{counter+1}]').click()
    time.sleep(2)
    driver.find_element_by_xpath(
        '/html/body/ytd-app/div/ytd-page-manager/ytd-watch-flexy/div[4]/div[1]/div/div[7]/div[2]/ytd-video-primary-info-renderer/div/div/div[3]/div/ytd-menu-renderer/div/ytd-toggle-button-renderer[1]/a/yt-icon-button/button/yt-icon').click()
    driver.back()
    counter += 1
    print("Videos Liked : " + str(counter))
    if counter > 960:
        print('I Liked all Videos...')
        print('I am not a human...')
        break