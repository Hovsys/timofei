import cv2
import numpy as np
import streamlit as st
from PIL import Image
import time

def capture_image():
    st.subheader('Capture an image')
    start_button = st.button('Включить камеру')
    stop_button = st.button('Сделать снимок', key=f'stop_capture_{time.time()}', disabled=True)
    FRAME_WINDOW = st.image([])

    if start_button:
        stop_button.disabled = False
    
    if stop_button:
        # Здесь можно написать код для захвата изображения
        pass


# Функция для загрузки нескольких изображений
def upload_images():
    st.subheader('Convert images to English sentence')
    sentence_image_files = st.file_uploader('Select the ASL Images', ['jpg', 'png'], accept_multiple_files=True)

    if len(sentence_image_files) > 0:
        sentence = ''
        for image_file in sentence_image_files:
            image = Image.open(image_file).convert('L')
            image = np.array(image, dtype='float32')
            letter = preprocess_image(image, image_file, best_model, label_binarizer)
            sentence += letter
        st.write(f'The sentence is predicted as {sentence}')


# Создание веб-приложения
st.title('ASL Recognition App')
option = st.sidebar.selectbox('Select an option', ('Capture an image', 'Convert images to English sentence'))

if option == 'Capture an image':
     capture_image()
else:
    upload_images()
