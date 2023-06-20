import streamlit as st
import cv2
from PIL import Image
import numpy as np

# Функция для загрузки изображения
def load_image(image_file):
    img = Image.open(image_file)
    return img

# Функция для обработки изображения и получения результата
def preprocess_image(image, model, binarizer):
    # ... код обработки изображения ...
    return result

# Загружаем модель и бинаризатор
model = load_model()
binarizer = load_binarizer()

# Загружаем страницу
def app():
    st.title('ASL to English Translation')

    # Добавляем возможность загрузки изображения с компьютера
    st.subheader('Translate ASL Image to English Letter')
    image_file = st.file_uploader('Choose the ASL Image', ['jpg', 'jpeg', 'png'])
    if image_file is not None:
        image = load_image(image_file)
        image = np.array(image, dtype='float32')
        letter = preprocess_image(image, model, binarizer)
        st.write(f'The image is predicted as {letter}')

    # Добавляем возможность получения изображения с веб-камеры
    st.subheader('Capture Image from Webcam')
    run = st.checkbox('Run')
    FRAME_WINDOW = st.image([])
    camera = cv2.VideoCapture(0)
    while run:
        _, frame = camera.read()
        frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        FRAME_WINDOW.image(frame)
        if st.button("Capture"):
            cv2.imwrite('captured_image.png', frame)
            image = load_image('captured_image.png')
            image = np.array(image, dtype='float32')
            letter = preprocess_image(image, model, binarizer)
            st.write(f'The image is predicted as {letter}')
            st.success("Image captured!")
        if st.button("Quit"):
            run = False
    camera.release()

if __name__ == '__main__':
    app()
