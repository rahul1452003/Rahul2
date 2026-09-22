import streamlit as st

a=st.text_input("Enter your name")
if st.button("display"):
	st.success(a)


