import streamlit as st
from PIL import Image

# Загрузка изображений
uploaded_files = st.sidebar.file_uploader("Choose images...", type=["jpg", "png"], accept_multiple_files=True, key='image_uploader')

# Список с загруженными изображениями
images = []
for uploaded_file in uploaded_files:
    image = Image.open(uploaded_file)
    images.append(image)

# Флаг для отображения/скрытия изображения
show_image = False

# Создание пустого контейнера для кнопки "Show Image"
show_image_container = st.empty()

# Обновление контейнера с помощью метода container.button()
if show_image_container.button('Show Image', key='show_image_button_' + str(show_image)) and len(images) > 0:
    show_image = True

# Индекс текущего изображения
current_image_index = 0

# Отображение изображения, если флаг установлен в True
if show_image:
    st.image(images[current_image_index], caption='Uploaded Image', use_column_width=True)

    # Кнопки для переключения между изображениями
    col1, col2, col3 = st.columns(3)
    if col2.button('Сделать фото', key='previous_button'):
        current_image_index = (current_image_index - 1) % len(images)
    if col2.button('следующий жест', key='next_button'):
        current_image_index = (current_image_index + 1) % len(images)

    # Кнопки для отмены последней буквы и выключения камеры
    if col3.button('Undo Last Letter', key='undo_button'):
        st.write('Undo Last Letter Button Clicked')
    if col3.button('Turn Off Camera', key='camera_button'):
        st.write('Turn Off Camera Button Clicked')

    # Скрытие кнопки "Show Image", если изображение отображается
    show_image_container.empty()
