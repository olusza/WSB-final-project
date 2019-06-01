# -*- coding: utf-8 -*-

# Plik, w którym będą wywoływane funkcje z testami modułu LG (logowanie) 
# na przeglądarkach: Chrome, Firefox i Edge.

from selenium import webdriver
from LG_01 import LG_01
from LG_02 import LG_02
from LG_03 import LG_03
from LG_04 import LG_04
from LG_05 import LG_05

# Test LG_01
print("\n Test LG_01 podsumowanie: \n")
print("Test LG_01 na przeglądarce Chrome zakończony wynikiem", end='')
LG_01(webdriver.Chrome())
print("Test LG_01 na przeglądarce Firefox zakończony wynikiem", end='')
LG_01(webdriver.Firefox())
print("Test LG_01 na przeglądarce Edge zakończony wynikiem", end='')
LG_01(webdriver.Edge())

# Test LG_02
print("\n Test LG_02 podsumowanie: \n")
print("Test LG_02 na przeglądarce Chrome zakończony wynikiem", end='')
LG_02(webdriver.Chrome())
print("Test LG_02 na przeglądarce Firefox zakończony wynikiem", end='')
LG_02(webdriver.Firefox())
print("Test LG_02 na przeglądarce Edge zakończony wynikiem", end='')
LG_02(webdriver.Edge())

# Test LG_03
print("\n Test LG_03 podsumowanie: \n")
print("Test LG_03 na przeglądarce Chrome zakończony wynikiem", end='')
LG_03(webdriver.Chrome())
print("Test LG_03 na przeglądarce Firefox zakończony wynikiem", end='')
LG_03(webdriver.Firefox())
print("Test LG_03 na przeglądarce Edge zakończony wynikiem", end='')
LG_03(webdriver.Edge())

# Test LG_04
print("\n Test LG_02 podsumowanie: \n")
print("Test LG_02 na przeglądarce Chrome zakończony wynikiem", end='')
LG_04(webdriver.Chrome())
print("Test LG_02 na przeglądarce Firefox zakończony wynikiem", end='')
LG_04(webdriver.Firefox())
print("Test LG_02 na przeglądarce Edge zakończony wynikiem", end='')
LG_04(webdriver.Edge())

# Test LG_05
print("\n Test LG_05 podsumowanie: \n")
print("Test LG_05 na przeglądarce Chrome zakończony wynikiem", end='')
LG_05(webdriver.Chrome())
print("Test LG_05 na przeglądarce Firefox zakończony wynikiem", end='')
LG_05(webdriver.Firefox(), True)
print("Test LG_05 na przeglądarce Edge zakończony wynikiem", end='')
LG_05(webdriver.Edge(), True)