import streamlit as st

HEADER = "Crime Dataset Captioning"

st.header(HEADER, anchor=None)
st.text("Testing 1")
st.info('Please upload your file below! Make sure it is an MP4 format!')
st.file_uploader(label, type=None, accept_multiple_files=False, key=None, help=None, on_change=None, args=None, kwargs=None, disabled=False)
