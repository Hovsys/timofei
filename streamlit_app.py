mport streamlit as st

st.subheader('Convert Image to English letter')
image_file = st.file_uploader('Choose the ASL Image', ['jpg', 'png'])

if image_file is not None:
image = Image.open(image_file).convert('L')
image = np.array(image, dtype='float32')
letter = preprocess_image(image, image_file, best_model, label_binarizer)
st.write(f'The image is predicted as {letter}')

st.subheader('Convert images to English sentence')
sentence_image_files = st.file_uploader('Select the ASL Images', ['jpg', 'png'], accept_multiple_files = True)

if len(sentence_image_files) > 0:
sentence = ''
for image_file in sentence_image_files:
image = Image.open(image_file).convert('L')
image = np.array(image, dtype='float32')
letter = preprocess_image(image, image_file, best_model, label_binarizer)
sentence += letter
st.write(f'The sentence is predicted as {sentence}')
