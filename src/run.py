import streamlit as st
from io import StringIO
import json
import seaborn as sns
import numpy as np
import matplotlib.pyplot as plt
from PIL import Image

# Login
login_option = st.sidebar.radio("Login/signup", {"Login", "Signup"})

if login_option == "Login":
    with st.sidebar.form("Login"):
        st.write("Login Here.")
        username = st.text_input("Username")
        password = st.text_input("Password", type="password")


        # Every form must have a submit button.
        submitted = st.form_submit_button("Login")
        if submitted:
            pass
else:
    with st.sidebar.form("Signup"):
        st.write("Signup Here.")
        username = st.text_input("Username")
        password = st.text_input("Password", type="password")
        email = st.text_input("Email")

        # Every form must have a submit button.
        submitted = st.form_submit_button("Signup")
        if submitted:
            pass

# Banner
banner = Image.open('./data/banner.png')
st.image(banner)
st.title(":zap: Telegram Group Dashboard")




# Metrics
st.metric(label="Group members", value="400",delta="+10")

# Statistics
with st.expander("statistics"):
    fig, ax = plt.subplots(1, 1, figsize=(10, 5))
    sns.histplot(np.random.randn(100), ax=ax)
    st.pyplot(fig)

# User Info
with st.expander("User"):
    col1, col2 = st.columns(2)
    col1.text_input("Name:")
    col2.text_input("location:")

    st.camera_input("Camera Input", key="camera_input")


