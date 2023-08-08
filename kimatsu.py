import numpy as np
import pandas as pd
import streamlit as st
from skimage.io import imread


def binarize_im(im):
    """画像をグレー変換する

    Args:
        im (行列): 加工前の画像

    Returns:
        行列: グレー変換を行った画像
    """
    im = im.convert('L')

    return im


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


# download the image
img_url = 'https://upload.wikimedia.org/wikipedia/commons/thumb/d/df/Mount_Fuji_from_Mount_Aino.jpg/640px-Mount_Fuji_from_Mount_Aino.jpg'

im = imread(img_url)

st.image(im, caption='image from wikimedia commons',
         use_column_width=True)
histgram_show(im)

im_2 = im
im_2 = binarize_im(im_2)

st.image(im_2, caption='image gray_convert',
         use_column_width=True)
histgram_show(im_2)
