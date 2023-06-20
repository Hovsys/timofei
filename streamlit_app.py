import streamlit as st
from PIL import Image

# Загрузка изображения
uploaded_file = st.file_uploader("Choose an image...", type="jpg")

# Отображение изображения
if uploaded_file is not None:
    image = Image.open(uploaded_file)
    st.image(image, caption='Uploaded Image', use_column_width=True)

# Кнопки для отображения/скрытия изображения
if st.button('Show Image'):
    st.image(image, caption='Uploaded Image', use_column_width=True)
if st.button('Hide Image'):
    st.empty()
   

