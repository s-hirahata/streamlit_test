# streamlit_app.py
import streamlit as st
from PIL import Image

# --- アプリの基本設定 ---
st.set_page_config(
    page_title="私の画像ギャラリー",
#   page_icon="???,
    layout="wide"
)

# --- ヘッダー ---
st.title("PNG画像公開アプリ")
st.write("StreamlitとGitHubを使って、株価情報をスクレイピングして作成した画像を公開してみました。")
st.divider()

# --- 画像の表示 ---
try:
    # PILライブラリで画像を開くと、エラーが起きにくくなります
    image1 = Image.open('image1.png')
    st.image(image1, caption='これは1枚目の画像です。',
# width=500)
use_container_width=True)
except FileNotFoundError:
    st.error("ファイル 'image1.png'が見つかりませんでした。")

try:
    image2 = Image.open('image2.png')
    st.image(image2, caption='これは2枚目の画像です。',
use_container_width=True)
except FileNotFoundError:
    st.error("ファイル 'image2.png'が見つかりませんでした。")

# --- フッター ---
st.divider()
st.write("作成者: (S.Hirahata)")
