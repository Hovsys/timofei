import streamlit as st
from PIL import Image

# Загрузка изображений
uploaded_files = st.sidebar.file_uploader("Choose images...", type=["jpg", "png"], accept_multiple_files=True)

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
show_image_button_key = 'show_image_button_' + str(show_image) + '_0'
if show_image_container.button('Show Image', key=show_image_button_key) and len(images) > 0:
    show_image = True

# Индекс текущего изображения
current_image_index = 0

# Флаг для определения, было ли изменено текущее изображение
image_changed = False

# Отображение изображения, если флаг установлен в True
if show_image:
    st.image(images[current_image_index], caption='Uploaded Image', use_column_width=True)

    # Кнопки для переключения между изображениями
    col1, col2, col3 = st.columns(3)
    if col2.button('Previous', key='previous_button'):
        current_image_index = (current_image_index - 1) % len(images)
        image_changed = True
    if col2.button('Next', key='next_button'):
        current_image_index = (current_image_index + 1) % len(images)
        image_changed = True

    # Если изображение было изменено, установить флаг show_image в True
    if image_changed:
        show_image = True

# Отображение кнопки "Show Image", если изображение скрыто
if not show_image and len(images) > 0:
    show_image_button_key = 'show_image_button_' + str(show_image) + '_1'
    show_image_container.button('Show Image', key=show_image_button_key)

# Скрытие кнопки "Show Image", если изображение отображается
if show_image:
    show_image_container.empty()
