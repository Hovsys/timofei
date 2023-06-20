import streamlit as st
from PIL import Image

# Загрузка изображения
uploaded_file = st.file_uploader("Choose an image...", type="jpg")

# Флаг для отображения/скрытия изображения
show_image = False

# Отображение изображения после нажатия на кнопку "Show Image"
if st.button('Show Image', key='show_image_button') and uploaded_file is not None:
    show_image = True

# Отображение изображения, если флаг установлен в True
if show_image:
    image = Image.open(uploaded_file)
    st.image(image, caption='Uploaded Image', use_column_width=True)

# Кнопка для скрытия изображения
if show_image and st.button('Hide Image', key='hide_image_button'):
    show_image = False

# Скрытие кнопки "Show Image" после ее нажатия
if show_image is False and uploaded_file is not None:
    st.button('Show Image', key='show_image_button')
