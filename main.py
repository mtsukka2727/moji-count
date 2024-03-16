import streamlit as st

st.title("tsukka文字数カウントアプリ")

if 'tsukka_memo' not in st.session_state:
    st.session_state['tsukka_memo'] =list()

input_text = st.text_area('文字を入力してください')

is_pushed = st.button("文字カウント")

if is_pushed:
    st.text(f"{len(input_text)}字")
else:
    pass

if st.button("保存する"):
    st.session_state['tsukka_memo'].append(input_text)


for _ in st.session_state['tsukka_memo']:
    st.text(_)
    st.text(f"{len(_)}字")
    st.divider()
    st.button()
