import streamlit as st

st.title("tsukka文字数カウントアプリ")
input_text = st.text_area('文字を入力してください')

is_pushed = st.button("文字カウント")

if is_pushed:
    st.text(len(input_text))
else:
    pass