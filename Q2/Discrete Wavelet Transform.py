import numpy as np
import matplotlib.pyplot as plt
import pywt
import cv2
# Load image
original = cv2.imread("C:/Users/ksais/OneDrive/Documents/Coding/Computer Vision/computer-vision-hands-on/Q4/dataset/Image3.jpg")

# Wavelet transform of image, and plot approximation and details
titles = ['Approximation', ' Horizontal detail',
          'Vertical detail', 'Diagonal detail']
coeffs2 = pywt.dwt2(original, 'bior1.3')
#print(coeffs2)
LL, (LH, HL, HH) = coeffs2
fig = plt.figure(figsize=(12, 3))
for i, a in enumerate([LL, LH, HL, HH]):
    ax = fig.add_subplot(1, 4, i + 1)
    ax.imshow(a, interpolation="nearest", cmap=plt.cm.gray)
    ax.set_title(titles[i], fontsize=10)
    ax.set_xticks([])
    ax.set_yticks([])

fig.tight_layout()
plt.show()

# Reference : https://pywavelets.readthedocs.io/en/latest/