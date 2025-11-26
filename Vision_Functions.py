from matplotlib import pyplot as plt
import cv2

def plot(image,title):
    plt.imshow(cv2.cvtColor(image, cv2.COLOR_BGR2RGB))
    plt.axis('off')
    plt.title(title)
    plt.show()
    return