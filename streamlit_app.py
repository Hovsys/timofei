import cv2
import numpy as np
import streamlit as st
from PIL import Image


# Функция для захвата изображения с камеры
def capture_image():
    st.subheader('Capture an image')
    start_button = st.button('Включить камеру')
    stop_button = st.button('Сделать снимок', key='stop_capture', disabled=True)
    FRAME_WINDOW = st.image([])

    # Открыть первую доступную камеру
    camera = cv2.VideoCapture(0)
    if not camera.isOpened():
        st.error('Unable to Access Camera')
        return

    while start_button:
        _, frame = camera.read()
        frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        FRAME_WINDOW.image(frame)
        if stop_button is not None:
            stop_button.disabled = False
        start_button = st.button('Включить камеру', key='run_capture', disabled=True)
    camera.release()
    if stop_button is not None:
        stop_button.disabled = True
    start_button = st.button('Включить камеру', key='run_capture', disabled=False)


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
