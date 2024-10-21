

import tkinter as tk
from tkinter import filedialog
import matplotlib.pyplot as plt
from color_analysis import get_dominant_colors, rgb_to_hex
import numpy as np  

def plot_color_pie_chart(colors, counts):
    """Создает круговую диаграмму для отображения основных цветов."""
    hex_codes = [rgb_to_hex(tuple(color)) for color in colors]
    sizes = counts / counts.sum() * 100  # Преобразуем к процентам
    plt.figure(figsize=(8, 6))
    wedges, _ = plt.pie(sizes, labels=None, 
                        colors=hex_codes, startangle=90, counterclock=False,
                        wedgeprops=dict(edgecolor='black'))

    for i, wedge in enumerate(wedges):
        angle = (wedge.theta1 + wedge.theta2) / 2
        x = (wedge.r + 0.15) * np.cos(np.radians(angle))
        y = (wedge.r + 0.15) * np.sin(np.radians(angle))
        
        percentage = sizes[i]
        plt.text(x, y, f"{hex_codes[i]} ({percentage:.1f}%)", ha='center', va='center', fontsize=10, color='black')

    plt.axis('equal')
    plt.title("Основные цвета")
    plt.show()

def load_image():
    """Загружает изображение и отображает основные цвета."""
    file_path = filedialog.askopenfilename(title="Выберите изображение", 
                                            filetypes=[("Image files", "*.jpg;*.jpeg;*.png;*.bmp;*.gif;*.tiff")])
    if file_path:
        dominant_colors, counts = get_dominant_colors(file_path, num_colors=5)
        if dominant_colors is not None:
            print("Основные цвета:", dominant_colors)
            plot_color_pie_chart(dominant_colors, counts)

def setup_gui():
    """Настраивает графический интерфейс."""
    root = tk.Tk()
    root.title("Определение основных цветов на фотографии")
    root.geometry("300x150")
    root.configure(bg="#f0f0f0")

    load_button = tk.Button(root, text="Загрузить изображение", command=load_image, 
                            bg="#4CAF50", fg="white", font=("Helvetica", 12), 
                            relief="flat", padx=10, pady=5)
    load_button.pack(expand=True)

    root.mainloop()

if __name__ == "__main__":
    setup_gui()