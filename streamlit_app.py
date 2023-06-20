import cv2
import numpy as np
import streamlit as st
from PIL import Image

def capture_image():
    st.subheader('Capture an image')
    FRAME_WINDOW = st.image([])
    camera = cv2.VideoCapture(0)
    while True:
        _, frame = camera.read()
        frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        FRAME_WINDOW.image(frame)
        if st.button('Capture'):
            break
    camera.release()

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

st.title('ASL Recognition App')
option = st.sidebar.selectbox('Select an option', ('Capture an image', 'Convert images to English sentence'))

if option == 'Capture an image':
    capture_image()
else:
    upload_images()
