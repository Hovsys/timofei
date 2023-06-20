import cv2
import numpy as np
import streamlit as st
from PIL import Image

# Функция для загрузки нескольких изображений
def upload_images():
    st.subheader('')
    sentence_image_files = st.file_uploader('Select Images', ['jpg', 'png'], accept_multiple_files=True)

    if sentence_image_files is not None:
        for i, image_file in enumerate(sentence_image_files):
            st.subheader(f'Image {i+1}')
            image = Image.open(image_file).convert('RGB')
            st.image(image, use_column_width=True, caption=image_file.name)
            if st.button(f"View/Hide Image {i+1}"):
                st.image(image, use_column_width=True)
                st.write(f'Image {i+1} is displayed')
            else:
                st.write(f'Image {i+1} is hidden')

def capture_image():
    st.subheader('Просмотр изображения')
    start_button = st.button('Посмотреть изображение')
    stop_button = st.button('Скрыть изображение', key='stop_capture', disabled=True)
    FRAME_WINDOW = st.image([])

# Создание веб-приложения
st.title('')
option = st.sidebar.selectbox('Select an option', ('Просмотр изображения', 'Загрузка изображения'))

if option == 'Просмотр изображения':
    capture_image()
else:
    upload_images()
