# -*- coding: utf-8 -*-

# Plik, w którym będą wywoływane funkcje z modułu RU (rejestracja użytkownika)
# na przeglądarkach: Chrome, Firefox i Edge.

from selenium import webdriver
from RU_01 import RU_01
from RU_02 import RU_02
from RU_03 import RU_03
from RU_04 import RU_04
from RU_05 import RU_05
from RU_06 import RU_06
from RU_07 import RU_07
from RU_10_15 import RU_10_15
from RU_16 import RU_16
from RU_17_20 import RU_17_20
from RU_21 import RU_21
from RU_22 import RU_22


# Test RU_01
print("Test RU_01 podsumowanie: \n")
print("Test RU_01 na przeglądarce Chrome zakończony wynikiem ", end='')
RU_01(webdriver.Chrome())
print("Test RU_01 na przeglądarce Firefox zakończony wynikiem ", end='')
RU_01(webdriver.Firefox())
print("Test RU_01 na przeglądarce Edge zakończony wynikiem ", end='')
RU_01(webdriver.Edge(), True)

# Test RU_02
print("\n Test RU_02 podsumowanie: \n")
print("Test RU_02 na przeglądarce Chrome zakończony wynikiem", end='')
RU_02(webdriver.Chrome())
print("Test RU_02 na przeglądarce Firefox zakończony wynikiem", end='')
RU_02(webdriver.Firefox())
print("Test RU_02 na przeglądarce Edge zakończony wynikiem", end='')
RU_02(webdriver.Edge(), True)

# Test RU_03
print("\n Test RU_03 podsumowanie: \n")
print("Test RU_03 na przeglądarce Chrome zakończony wynikiem", end='')
RU_03(webdriver.Chrome())
print("Test RU_03 na przeglądarce Firefox zakończony wynikiem", end='')
RU_03(webdriver.Firefox())
print("Test RU_03 na przeglądarce Edge zakończony wynikiem", end='')
RU_03(webdriver.Edge(), True)

# Test RU_04
print("\n Test RU_04 podsumowanie: \n")
print("Test RU_04 na przeglądarce Chrome zakończony wynikiem", end='')
RU_04(webdriver.Chrome())
print("Test RU_04 na przeglądarce Firefox zakończony wynikiem", end='')
RU_04(webdriver.Firefox())
print("Test RU_04 na przeglądarce Edge zakończony wynikiem", end='')
RU_04(webdriver.Edge(), True)

# Test RU_05
print("\n Test RU_05 podsumowanie: \n")
print("Test RU_05 na przeglądarce Chrome wynik:")
RU_05(webdriver.Chrome())
print("\n Test RU_05 na przeglądarce Firefox wynik:")
RU_05(webdriver.Firefox())
print("\n Test RU_05 na przeglądarce Edge wynik:")
RU_05(webdriver.Edge(), True)

# Test RU_06
print("\n Test RU_06 podsumowanie: \n")
print("Test RU_06 na przeglądarce Chrome zakończony wynikiem", end='')
RU_06(webdriver.Chrome())
print("Test RU_06 na przeglądarce Firefox zakończony wynikiem", end='')
RU_06(webdriver.Firefox())
print("Test RU_06 na przeglądarce Edge zakończony wynikiem", end='')
RU_06(webdriver.Edge(), True)

# Test RU_07
print("\n Test RU_07 podsumowanie: \n")
print("Test RU_07 na przeglądarce Chrome zakończony wynikiem", end='')
RU_07(webdriver.Chrome())
print("Test RU_07 na przeglądarce Firefox zakończony wynikiem", end='')
RU_07(webdriver.Firefox())
print("Test RU_07 na przeglądarce Edge zakończony wynikiem", end='')
RU_07(webdriver.Edge(), True)

# Test RU_10_15
print("\n Test RU_10_15 podsumowanie: \n")
print("Test RU_10_15 na przeglądarce Chrome zakończony wynikiem:")
RU_10_15(webdriver.Chrome())
print("\n Test RU_10_15 na przeglądarce Firefox zakończony wynikiem:")
RU_10_15(webdriver.Firefox())
print("\n Test RU_10_15 na przeglądarce Edge zakończony wynikiem:")
RU_10_15(webdriver.Edge(), True)

# Test RU_16
print("\n Test RU_16 podsumowanie: \n")
print("Test RU_16 na przeglądarce Chrome zakończony wynikiem ", end='')
RU_01(webdriver.Chrome())
print("Test RU_16 na przeglądarce Firefox zakończony wynikiem ", end='')
RU_01(webdriver.Firefox())
print("Test RU_16 na przeglądarce Edge zakończony wynikiem ", end='')
RU_01(webdriver.Edge(), True)

# Test RU_17_20
print("\n Test RU_17_21 podsumowanie: \n")
print("Test RU_17_21 na przeglądarce Chrome zakończony wynikiem:")
RU_17_20(webdriver.Chrome())
print("\n Test RU_17_21 na przeglądarce Firefox zakończony wynikiem:")
RU_17_20(webdriver.Firefox())
print("\n Test RU_17_21 na przeglądarce Edge zakończony wynikiem:")
RU_17_20(webdriver.Edge(), True)

# Test RU_21

print("\n Test RU_21 podsumowanie: \n")
print("Test RU_21 na przeglądarce Chrome zakończony wynikiem ", end='')
RU_21(webdriver.Chrome())
print("Test RU_21 na przeglądarce Firefox zakończony wynikiem ", end='')
RU_21(webdriver.Firefox())
print("Test RU_21 na przeglądarce Edge zakończony wynikiem ", end='')
RU_21(webdriver.Edge(), True)

# Test RU_22

print("\n Test RU_22 podsumowanie: \n")
print("Test RU_22 na przeglądarce Chrome wynik:")
RU_22(webdriver.Chrome())
print("\n Test RU_22 na przeglądarce Firefox wynik:")
RU_22(webdriver.Firefox())
print("\n Test RU_22 na przeglądarce Edge wynik:")
RU_22(webdriver.Edge(), True)