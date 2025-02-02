from tkinter import Button
import streamlit as st
import numpy as np
import keras
from tensorflow.keras.preprocessing.image import ImageDataGenerator, array_to_img, img_to_array, load_img
from keras.models import Sequential, load_model
from PIL import Image
import cv2
import time

st.set_page_config(page_title='تشخیص سرطان پوست - RoboAi', layout='centered', page_icon='🧪')

model = load_model('model.h5')

def show_page():
    st.write("<h3 style='text-align: center; color: blue;'>تشخیص سرطان پوست 🩺</h3>", unsafe_allow_html=True)
    st.write("<h6 style='text-align: center; color: black;'>Robo-Ai.ir طراحی و توسعه</h6>", unsafe_allow_html=True)
    st.link_button("Robo-Ai بازگشت به", "https://robo-ai.ir")
    container = st.container(border=True)
    container.write("<h6 style='text-align: right; color: gray;'>تشخیص سرطان پوست خوش خیم از بدخیم 🧫</h6>", unsafe_allow_html=True)
    st.write('')

    with st.sidebar:
        st.write("<h5 style='text-align: center; color: blcak;'>تشخیص سرطان پوست</h5>", unsafe_allow_html=True)
        st.write("<h5 style='text-align: center; color: gray;'>ساخته شده برای تشخیص استیج های 1 تا 4</h5>", unsafe_allow_html=True)
        st.divider()
        st.write("<h5 style='text-align: center; color: black;'>طراحی و توسعه</h5>", unsafe_allow_html=True)
        st.write("<h5 style='text-align: center; color: gray;'>حمیدرضا بهرامی</h5>", unsafe_allow_html=True)

    image = st.file_uploader('آپلود تصویر', type=['jpg', 'jpeg'])
    button = st.button('ارزیابی')       
    if image is not None:
        file_bytes = np.array(bytearray(image.read()), dtype= np.uint8)
        img = cv2.imdecode(file_bytes, 1)
        st.image(img, channels= 'BGR', use_container_width= True)
        if button: 
            x = cv2.resize(img, (100, 100))
            x1 = img_to_array(x)
            x1 = x1.reshape((1,) + x1.shape)
            y_pred = model.predict(x1)
            if y_pred == 1:
                text1 = 'بر اساس ارزیابی من ، سرطان پوست بدخیم در تصویر رویت شد'
                text2 = 'برای ارزیابی دقیق تر ، به پزشک مراجعه کنید'
                text3 = 'Based on my analysis, malignant skin cancer is detected in this image'
                text4 = 'Visit a specialist doctor as soon as possible'
                def stream_data1():
                    for word in text1.split(" "):
                        yield word + " "
                        time.sleep(0.09)
                st.write_stream(stream_data1)
                def stream_data2():
                    for word in text2.split(" "):
                        yield word + " "
                        time.sleep(0.09)
                st.write_stream(stream_data2)
                def stream_data3():
                    for word in text3.split(" "):
                        yield word + " "
                        time.sleep(0.09)
                st.write_stream(stream_data3)
                def stream_data4():
                    for word in text4.split(" "):
                        yield word + " "
                        time.sleep(0.09)
                st.write_stream(stream_data4)

            else:
                text5 = 'بر اساس ارزیابی من ، سرطان پوست خوش خیم در تصویر رویت شد'
                text6 = 'برای ارزیابی دقیق تر ، به پزشک مراجعه کنید'
                text7 = 'Based on my analysis, benign skin cancer is detected in this image'
                text8 = 'Visit a specialist doctor as soon as possible'
                def stream_data5():
                    for word in text5.split(" "):
                        yield word + " "
                        time.sleep(0.09)
                st.write_stream(stream_data5)
                def stream_data6():
                    for word in text6.split(" "):
                        yield word + " "
                        time.sleep(0.09)
                st.write_stream(stream_data6)
                def stream_data7():
                    for word in text7.split(" "):
                        yield word + " "
                        time.sleep(0.09)
                st.write_stream(stream_data7)
                def stream_data8():
                    for word in text8.split(" "):
                        yield word + " "
                        time.sleep(0.09)
                st.write_stream(stream_data8)

show_page()
