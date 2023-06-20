import io
import time
import requests
import json
import base64
import streamlit as st
from PIL import Image

# Запрос на получение изображения с камеры
def get_camera_image():
    url = 'http://<your-android-device-ip>:8080/shot.jpg'
    response = requests.get(url)
    img = response.content
    img = io.BytesIO(img)
    return img

# Функция для захвата изображения с камеры
def capture_image():
    st.subheader('Capture an image')
    run_button = st.button('Run')
    stop_button = st.button('Stop', key='stop_capture', visible=False)
    FRAME_WINDOW = st.image([])

    while run_button:
        img = get_camera_image()
        frame = Image.open(img)
        FRAME_WINDOW.image(frame)
        stop_button.visible = True
        run_button = st.button('Run', key='run_capture', visible=False)
    stop_button.visible = False
    run_button = st.button('Run', key='run_capture', visible=True)

# Создание веб-приложения
st.title('ASL Recognition App')
option = st.sidebar.selectbox('Select an option', ('Capture an image', 'Convert images to English sentence'))

if option == 'Capture an image':
    capture_image()
else:
    upload_images()
