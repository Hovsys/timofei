import streamlit as st
from PIL import Image

# Загрузка изображения
uploaded_file = st.file_uploader("Choose an image...", type="jpg")

# Флаг для отображения/скрытия изображения
show_image = False

# Создание пустого контейнера для кнопки "Show Image"
show_image_container = st.empty()

# Обновление контейнера с помощью метода container.button()
if show_image_container.button('Show Image', key='show_image_button') and uploaded_file is not None:
    show_image = True

# Отображение изображения, если флаг установлен в True
if show_image:
    image = Image.open(uploaded_file)
    st.image(image, caption='Uploaded Image', use_column_width=True)

    # Кнопка для скрытия изображения
    if st.button('Hide Image', key='hide_image_button'):
        show_image = False

    # Скрытие кнопки "Show Image", если изображение отображается
    show_image_container.empty()

# Показать кнопку "Show Image", если изображение не отображается
if not show_image and uploaded_file is not None:
    show_image_container.button('Show Image', key='show_image_button')
