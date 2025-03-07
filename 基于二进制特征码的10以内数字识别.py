"""
    author@L1quidBounce
    URL: https://github.com/L1quidBounce
    屎山代码要出现了
"""

import numpy as np
from PIL import Image
from sklearn.cluster import KMeans
from tkinter import Tk, filedialog

def get_main_colors(img, n_colors=2):
    pixels = np.array(img).reshape(-1, 3)
    if len(pixels) > 10000: #降采样加速处理
        np.random.shuffle(pixels)
        pixels = pixels[:10000]
    #操你妈草泥马草泥马真难写
    kmeans = KMeans(n_clusters=n_colors, random_state=0).fit(pixels)
    counts = np.bincount(kmeans.labels_)
    sorted_indices = np.argsort(-counts)
    return kmeans.cluster_centers_[sorted_indices].astype(int)

#将图片转换为二进制特征码
def img_to_erjinzhi(image_path, grid_size, coloe_threshold=50):
    img + Image.open(image_path).convert('RGB')
    img = img.resize((300, 200))


