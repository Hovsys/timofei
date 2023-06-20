import cv2
import numpy as np
import streamlit as st
from PIL import Image
import permissions


# Функция для захвата изображения с камеры
def capture_image():
    st.subheader('Capture an image')
    run_button = st.button('Run')
    stop_button = st.button('Stop', key='stop_capture', disabled=True)
    FRAME_WINDOW = st.image([])
    
    # Запрос на доступ к камере
    try:
        permissions.Camera()
    except permissions.PermissionError:
        st.error('Permission to access camera was not granted')
        return
    
    camera_indexes = [i for i in range(10)]
    cameras = [cv2.VideoCapture(index, cv2.CAP_DSHOW) for index in camera_indexes]
    available_cameras = [index for index, camera in enumerate(cameras) if camera.isOpened()]
    if len(available_cameras) == 0:
        st.error('No cameras available')
        return
    camera_index = st.selectbox('Select a camera', available_cameras)
    camera = cameras[camera_index]
    while run_button:
        _, frame = camera.read()
        frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        FRAME_WINDOW.image(frame)
        if stop_button is not None:
            stop_button.disabled = False
        run_button = st.button('Run', key='run_capture', disabled=True)
    camera.release()
    for camera in cameras:
        camera.release()
    if stop_button is not None:
        stop_button.disabled = True
    run_button = st.button('Run', key='run_capture', disabled=False)

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
