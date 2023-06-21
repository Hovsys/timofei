import streamlit as st
from PIL import Image
 
st.title('Photo Mode')

# Image upload
uploaded_files = st.sidebar.file_uploader("Choose images...", type=["jpg", "png"], accept_multiple_files=True, key='image_uploader')

# List of uploaded images
images = []
for uploaded_file in uploaded_files:
    image = Image.open(uploaded_file)
    images.append(image)
    
# Flag to show/hide image
show_image = False

# Create an empty container for the "Show Image" button
show_image_container = st.empty()

# Update the container using the container.button() method
if show_image_container.button(' On Camera', key='show_image_button_' + str(show_image)) and len(images) > 0:
    show_image = True

# Current image index
current_image_index = 0

# Display the image if the flag is set to True
if show_image:
    st.image(images[current_image_index], use_column_width=True)
    st.markdown('<p align="center">Take a photo of the gesture</p>', unsafe_allow_html=True)

    # Buttons to switch between images
    col1, col2, col3 = st.columns(3)
    if col2.button('Take Photo of Gesture', key='previous_button'):
        current_image_index = (current_image_index - 1) % len(images)
    if col2.button('Next Gesture', key='next_button'):
        current_image_index = (current_image_index + 1) % len(images)

    # Buttons to undo last letter and turn off camera
    if col3.button('Undo Last Letter', key='undo_button'):
        st.write('Undo Last Letter Button Clicked')
    if col3.button('Turn Off Photo Mode', key='camera_button'):
        st.write('Turn Off Camera Button Clicked')

    st.markdown('The predicted translation is: abk')
   
    # Hide the "Show Image" button if the image is displayed
    show_image_container.empty()
