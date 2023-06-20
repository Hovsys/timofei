import streamlit as st
from PIL import Image

# Загрузка изображений
uploaded_files = st.sidebar.file_uploader("Choose images...", type=["jpg", "png"], accept_multiple_files=True)

# Список с загруженными изображениями
images = []
if uploaded_files is not None:
    for uploaded_file in uploaded_files:
        try:
            image = Image.open(uploaded_file)
            images.append(image)
        except:
            st.warning(f"Could not load image {uploaded_file.name}")

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
if show_image and len(images) > 0:
    st.image(images[current_image_index], caption='Uploaded Image', use_column_width=True)

    # Кнопки для переключения между изображениями
    col1, col2, col3 = st.columns(3)
    if col2.button('Previous', key='previous_button'):
        current_image_index = (current_image_index - 1) % len(images)
    if col2.button('Next', key='next_button'):
        current_image_index = (current_image_index + 1) % len(images)
    if current_image_index != 0:
        show_image = True
    else:
        show_image = False

# Отображение кнопки "Show Image", если изображение скрыто
if not show_image and len(images) > 0:
    show_image_container.button('Show Image', key='show_image_button_' + str(show_image))

# Скрытие кнопки "Show Image", если изображение отображается
if show_image:
    show_image_container.empty()
