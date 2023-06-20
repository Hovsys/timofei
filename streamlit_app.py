import cv2
import numpy as np
import streamlit as st
from PIL import Image

# Функция для обработки изображения
def preprocess_image(image, image_file, best_model, label_binarizer):
    # Обработка изображения и предсказание буквы
    # ...

# Функция для захвата изображения с камеры
def capture_image():
    st.subheader('Capture an image')
    FRAME_WINDOW = st.image([])
    camera = cv2.VideoCapture(0)
    while True:
        _, frame = camera.read()
        FRAME_WINDOW.image(frame)
        if st.button('Capture'):
            break
    camera.release()
    # Обработка изображения и вывод результата
    # Конвертация кадра в изображение Pillow
    image = Image.fromarray(cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY))
    # Обработка изображения и вывод результата
    letter = preprocess_image(np.array(image), None, best_model, label_binarizer)
    st.write(f'The image is predicted as {letter}')

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
