import cv2
import numpy as np
import streamlit as st
from PIL import Image


def capture_image():
    st.subheader('1')
    start_button = st.button('Посмотреть изображения')
    stop_button = st.button('Скрыть изображения', key='stop_capture', disabled=True)
    FRAME_WINDOW = st.image([])

 

# Функция для загрузки нескольких изображений
def upload_images():
    st.subheader('2')

    
    sentence_image_files = st.file_uploader('Select Images', ['jpg', 'png'], accept_multiple_files=True)

    if len(sentence_image_files) > 0:
        sentence = ''
        for image_file in sentence_image_files:
            image = Image.open(image_file).convert('L')
            image = np.array(image, dtype='float32')
            letter = preprocess_image(image, image_file, best_model, label_binarizer)
            sentence += letter
        st.write(f'The sentence is predicted as {sentence}')


# Создание веб-приложения
st.title('')
option = st.sidebar.selectbox('Select an option', ('1', '2'))

if option == 'Capture an image':
    capture_image()
else:
    upload_images()
