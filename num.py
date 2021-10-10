import cv2
import tkinter as tk
from tkinter import messagebox
import numpy as np
import time

a1 = [1, 3, 2, 5, 3, 1, 2]
aa1 = 0
tStart1 = time.time()
time.sleep(1)
#def ff():
for i in range(7):
    if(a1[i] >= 3):
        aa1 = aa1 + 1
tend1 = time.time()

a2 = np.array([1, 3, 2, 5, 3, 1, 2])
tStart2 = time.time()
time.sleep(1)
aa2 = np.sum(a2 >= 3)
tend2 = time.time()
print(tend1 - tStart1, aa1)
print(tend2 - tStart2, aa2)

a3 = [1, 3, 2, 5, 3, 1, 2]
tStart3 = time.time()
time.sleep(1)
for i in range(7):
    if(a3[i] < 3):
        a3[i] = 0
tend3 = time.time()

a4 = np.array([1, 3, 2, 5, 3, 1, 2])
tStart4 = time.time()
time.sleep(1)
a4[a4 < 3] = 0
tend4 = time.time()

print(tend3 - tStart3, a3)
print(tend4 - tStart4, a4)
