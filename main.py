import streamlit as st

st.title("tskka moji count")
input_text = st.text_area('asdf')

is_pushed = st.button("文字カウント")

if is_pushed:
    st.text(len(input_text))
else:
    pass