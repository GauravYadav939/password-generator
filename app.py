import streamlit as st
import random
import string

st.title("🔐 Password Generator")

length = st.slider("Select password length", 6, 32, 12)
include_digits = st.checkbox("Include digits", True)
include_symbols = st.checkbox("Include symbols", True)

chars = string.ascii_letters
if include_digits:
    chars += string.digits
if include_symbols:
    chars += string.punctuation

if st.button("Generate Password"):
    password = ''.join(random.choice(chars) for _ in range(length))
    st.success(password)
    st.markdown("---")
    st.markdown("### 👋 Greetings!")
    st.write("Thank you for using this app — from **Gaurav Yadav** 💻")
