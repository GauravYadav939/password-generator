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
    st.success("✅ Password generated successfully!")

    # Display password in code style box
    st.code(password, language="text")

    # Copy to clipboard button using HTML+JS
    copy_script = f"""
    <button onclick="navigator.clipboard.writeText('{password}')"
    style="
        background-color:#4CAF50;
        color:white;
        border:none;
        padding:8px 16px;
        margin-top:8px;
        border-radius:8px;
        cursor:pointer;
    ">
    📋 Copy to Clipboard
    </button>
    """
    st.markdown(copy_script, unsafe_allow_html=True)

    st.markdown("---")
    st.markdown("### 👋 Greetings!")
    st.write("Thank you for using this app — from **Gaurav Yadav** 💻")

