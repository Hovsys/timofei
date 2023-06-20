import streamlit as st
from PIL import Image

# Загрузка изображения
uploaded_file = st.file_uploader("Choose an image...", type="jpg")

# Переменная для отображения/скрытия изображения
show_image = False

# Отображение изображения после нажатия на кнопку "Show Image"
if st.button('Show Image'):
    show_image = True

# Отображение изображения, если флаг установлен в True
if show_image and uploaded_file is not None:
    image = Image.open(uploaded_file)
    st.image(image, caption='', use_column_width=True)

# Кнопка для скрытия изображения
if show_image and st.button('Hide Image'):
    show_image = False
