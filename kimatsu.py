import numpy as np
import pandas as pd
import streamlit as st
from skimage.io import imread
from PIL import Image

def histgram_show(im):
    """画素のRGB値をヒストグラムで表示

    Args:
        im (行列): データとなる画像
    """
    # show histgram of all colors
    hist_red, _ = np.histogram(im[:, :, 0], bins=64)
    hist_green, _ = np.histogram(im[:, :, 1], bins=64)
    hist_blue, _ = np.histogram(im[:, :, 2], bins=64)
    hist = np.stack((hist_red, hist_green, hist_blue), axis=1)

    df_hist = pd.DataFrame(hist, columns=['R', 'G', 'B'])
    st.bar_chart(df_hist)

    # choose one color
    color = st.radio(
        "choose R, G, or B",
        ('R', 'G', 'B'))
    if color == 'R':
        df_hist = pd.DataFrame(hist_red)
        st.bar_chart(df_hist)
    if color == 'G':
        df_hist = pd.DataFrame(hist_green)
        st.bar_chart(df_hist)
    if color == 'B':
        df_hist = pd.DataFrame(hist_blue)
        st.bar_chart(df_hist)


st.title("金村美玖のアーティスト写真")
# download the image
img_url_3 = 'https://cdn.hinatazaka46.com/images/14/259/9a7d8fd77ebc318caac9973badaed/600_600_102400.jpg'
im_3 = imread(img_url_3)
img_url_4 = 'https://cdn.hinatazaka46.com/images/14/2e0/25e0f9a005106467a6b24ecbe5eec/600_600_102400.jpg'
im_4 = imread(img_url_4)
img_url_10 = 'https://cdn.hinatazaka46.com/images/14/c37/b38a196f2a8709c417eebdf13d8fe/1000_1000_102400.jpg'
im_10 = imread(img_url_10)

# main
number = st.radio("choose single",('3', '4', '10'))
if number == '3':
    st.image(im_3, caption='3rd single - hinatazaka46',use_column_width=True)
    histgram_show(im_3)
if number == '4':
    st.image(im_4, caption='4th single - hinatazaka46',use_column_width=True)
    histgram_show(im_4)
if number == '10':
    st.image(im_10, caption='10th single - hinatazaka46',use_column_width=True)
    histgram_show(im_10)