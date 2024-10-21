

from PIL import Image
import numpy as np 
from sklearn.cluster import KMeans

def get_dominant_colors(image_path, num_colors=5):
    """Получает основные цвета из изображения."""
    image = Image.open(image_path)
    image = image.convert('RGB')
    image.thumbnail((100, 100), Image.LANCZOS)
    image_data = np.array(image)

    if image_data.ndim == 3 and image_data.shape[2] == 3:
        pixels = image_data.reshape(-1, 3)
        kmeans = KMeans(n_clusters=num_colors)
        kmeans.fit(pixels)
        dominant_colors = kmeans.cluster_centers_.astype(int)
        labels = kmeans.labels_
        counts = np.bincount(labels)
        return dominant_colors, counts
    else:
        print("Изображение должно быть цветным (RGB).")
        return None, None

def rgb_to_hex(rgb):
    """Преобразует RGB в HEX-код."""
    return '#{:02x}{:02x}{:02x}'.format(rgb[0], rgb[1], rgb[2])