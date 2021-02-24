from selenium import webdriver
import time
from selenium.webdriver.common.action_chains import ActionChains
import os
from selenium.webdriver.common.keys import Keys

# Define Name and Pin

print("Kahoot Spammer V1.0 by Rabbitminers:")
print("Game Pin:")
pin = input("")
print("Name:")
name = input("")

# Define Loop Start Point

i = 0

# Start Driver

driver = webdriver.Chrome()
driverA = webdriver.Chrome()
driverB = webdriver.Chrome()
driverC = webdriver.Chrome()
driverD = webdriver.Chrome()


print("connecting bot 1...")

# Start Loop

driver.get('https://kahoot.it/')

time.sleep(1)

botNum = str(i)

PinEnter = driver.find_element_by_name("gameId")
PinEnter.send_keys(pin)

Join = driver.find_element_by_tag_name('button').click()

time.sleep(1)

NameEnter = driver.find_element_by_name("nickname")
NameEnter.send_keys(name)
NameEnter.send_keys("1")


Go = driver.find_element_by_tag_name('button').click()


time.sleep(1)

driverA.get('https://kahoot.it/')

print("connected bot 1...")
print("connecting bot 2...")

time.sleep(1)

PinEnterA = driverA.find_element_by_name("gameId")
PinEnterA.send_keys(pin)

JoinA = driverA.find_element_by_tag_name('button').click()

time.sleep(1)

NameEnter = driverA.find_element_by_name("nickname")
NameEnter.send_keys(name)
NameEnter.send_keys("2")

GoA = driverA.find_element_by_tag_name('button').click()

time.sleep(1)

print("connected bot 2...")
print("connecting bot 3...")


driverB.get('https://kahoot.it/')

time.sleep(1)

PinEnterB = driverB.find_element_by_name("gameId")
PinEnterB.send_keys(pin)

JoinB = driverB.find_element_by_tag_name('button').click()

time.sleep(1)

NameEnter = driverB.find_element_by_name("nickname")
NameEnter.send_keys(name)
NameEnter.send_keys("3")

GoB = driverB.find_element_by_tag_name('button').click()

time.sleep(1)

print("connected bot 3...")
print("connecting bot 4...")

driverC.get('https://kahoot.it/')

time.sleep(1)

PinEnterB = driverC.find_element_by_name("gameId")
PinEnterB.send_keys(pin)

JoinC = driverC.find_element_by_tag_name('button').click()

time.sleep(1)

NameEnter = driverC.find_element_by_name("nickname")
NameEnter.send_keys(name)
NameEnter.send_keys("4")

GoC = driverC.find_element_by_tag_name('button').click()

time.sleep(1)

print("connected bot 4...")
print("connecting bot 5...")

driverD.get('https://kahoot.it/')

time.sleep(1)

PinEnterD = driverD.find_element_by_name("gameId")
PinEnterD.send_keys(pin)

JoinD = driverD.find_element_by_tag_name('button').click()

time.sleep(1)

NameEnter = driverD.find_element_by_name("nickname")
NameEnter.send_keys(name)
NameEnter.send_keys("5")

GoD = driverD.find_element_by_tag_name('button').click()


print("connected bot 5...")

time.sleep(1)

print("Waiting for game to start...")











