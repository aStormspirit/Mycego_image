from PIL import Image
import os
import math

folders = ['1388_2']  # список папок
images = []  # список для хранения объектов изображений

# Перебираем все папки
for folder in folders:
    # Проверяем, что это папка
    if os.path.isdir(folder):
        # Перебираем все файлы в папке
        for filename in os.listdir(folder):
            # Если это изображение
            if filename.endswith('.jpg') or filename.endswith('.png') or filename.endswith('.tif'):
                # Открываем файл изображения и конвертируем в RGB
                img = Image.open(os.path.join(folder, filename))
                rgb_img = img.convert('RGB')
                # Добавляем в список
                images.append(rgb_img)

def get_width():
    width = 0

    if len(images) > 4:
        for i in range(4):
            width = width + (images[i].size[0])
    else:
        for i in range(len(images)):
            width = width + (images[i].size[0])

    return width + 300

def get_height():
    height = 0

    if len(images) > 4:
        for i in range(math.ceil(len(images) / 4)):
            height = height + (images[i].size[1])
    else:
        return images[0].size[1] + 300

    return height + 300


def get_coords(i, step):
    if i < 4:
        x = 100 + i * step
        y = 100
    else:
        x = 100 + (i % 4) * step
        y = 100 + math.floor(i / 4) * step
    return (x, y)

# Проверяем, что список изображений не пустой
if images:
    # Сохраняем все изображения в одном файле tiff
    new_image = Image.new('RGB', (get_width(), get_height()), (250, 250, 250))
    for i in range(len(images)):
        new_image.paste(images[i], get_coords(i, images[0].size[0] + 25))
    new_image.save('Result.tiff')
else:
    print("Не найдено изображений для сохранения.")

