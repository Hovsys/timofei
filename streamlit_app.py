import streamlit as st
from PIL import Image
from hashlib import blake2b
from types import SimpleNamespace

# Класс для сохранения переменных между запросами Streamlit
class SessionState:
    def __init__(self, **kwargs):
        self.hash_funcs = {_CodeHasher: lambda code: None}
        self.namespace = SimpleNamespace(**kwargs)

    def __getattr__(self, name):
        return getattr(self.namespace, name)

    def __setattr__(self, name, value):
        setattr(self.namespace, name, value)


# Инициализация SessionState
state = SessionState(show_image=False)

# Загрузка изображений
uploaded_files = st.sidebar.file_uploader("Choose images...", type=["jpg", "png"], accept_multiple_files=True)

# Список с загруженными изображениями
images = []
for uploaded_file in uploaded_files:
    image = Image.open(uploaded_file)
    images.append(image)

# Создание пустого контейнера для кнопки "Show Image" и "Hide Image"
show_image_container, hide_image_container = st.columns(2)

# Обновление контейнера с помощью метода container.button()
if show_image_container.button('Show Image', key='show_image_button', help='Show the uploaded images') and len(images) > 0:
    state.show_image = True

# Отображение изображения, если флаг установлен в True
if state.show_image:
    col1, col2, col3 = st.columns(3)

    # Отображение текущего изображения
    st.image(images[state.current_image_index], caption='Uploaded Image', use_column_width=True)

    # Кнопки для переключения между изображениями
    if col2.button('Previous', key='previous_button', help='Go to the previous image'):
        state.current_image_index = (state.current_image_index - 1) % len(images)
    if col2.button('Next', key='next_button', help='Go to the next image'):
        state.current_image_index = (state.current_image_index + 1) % len(images)

    # Кнопка для скрытия изображения
    if hide_image_container.button('Hide Image', key='hide_image_button', help='Hide the uploaded images'):
        state.show_image = False

# Скрытие кнопки "Show Image", если изображение отображается
if state.show_image:
    show_image_container.empty()
else:
    hide_image_container.empty()
