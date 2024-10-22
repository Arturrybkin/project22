import tkinter as tk
from tkinter import filedialog, messagebox
import plotly.graph_objects as go
from color_analysis import get_dominant_colors, rgb_to_hex
import numpy as np

def plot_color_pie_chart(colors, counts):
    """Создает интерактивную круговую диаграмму для отображения основных цветов."""
    hex_codes = [rgb_to_hex(tuple(color)) for color in colors]
    sizes = counts / counts.sum() * 100  # Преобразуем к процентам

    fig = go.Figure(data=[go.Pie(
        labels=[f'RGB({int(color[0])}, {int(color[1])}, {int(color[2])})' for color in colors],
        values=sizes,
        marker=dict(colors=hex_codes),
        textinfo='label+percent',
        hoverinfo='label+percent',
        textfont=dict(size=14),
        pull=[0.1] * len(colors)  # Немного выделяем каждый сектор
    )])

    fig.update_layout(title_text="Основные цвета", title_font_size=20)
    fig.show()

def load_image():
    """Загружает изображение и отображает основные цвета."""
    file_path = filedialog.askopenfilename(title="Выберите изображение", 
                                            filetypes=[("Image files", "*.jpg;*.jpeg;*.png;*.bmp;*.gif;*.tiff")])
    if file_path:
        try:
            dominant_colors, counts = get_dominant_colors(file_path, num_colors=5)
            if dominant_colors is not None:
                print("Основные цвета:", dominant_colors)
                plot_color_pie_chart(dominant_colors, counts)
            else:
                messagebox.showwarning("Предупреждение", "Не удалось извлечь основные цвета.")
        except Exception as e:
            messagebox.showerror("Ошибка", f"Произошла ошибка при обработке изображения:\n{e}")

def setup_gui():
    """Настраивает графический интерфейс."""
    root = tk.Tk()
    root.title("Определение основных цветов на фотографии")
    root.geometry("400x200")
    root.configure(bg="#f0f0f0")

    load_button = tk.Button(root, text="Загрузить изображение", command=load_image, 
                            bg="#4CAF50", fg="white", font=("Helvetica", 12), 
                            relief="flat", padx=10, pady=5)
    load_button.pack(expand=True)

    # Добавление информации о программе
    info_label = tk.Label(root, text="Выберите изображение для анализа основных цветов.", 
                           bg="#f0f0f0", font=("Helvetica", 10))
    info_label.pack(pady=10)

    root.mainloop()

if __name__ == "__main__":
    setup_gui()