import streamlit as st
import time
# import pandas as pd
# import numpy as np
# from data.create_data import create_table

def app():
    st.title('Home My Aplication')
    st.divider()
    if "photo" not in  st.session_state:
        st.session_state["photo"]="not done"

    col1, col2, col3 = st.columns([0.2, 0.7, 0.1])

    col1.markdown(" # Ambil Foto Anda ")
    col2.markdown("Disini informasi tentang aplikasi")

    def change_photo_state():
        st.session_state["photo"]="done"

    uploader_photo = col2.file_uploader("Upload Foto Anda ", on_change=change_photo_state)
    camera_photo = col2.camera_input("Senyum yang manis, Absensi Untuk 1 Minggu", on_change=change_photo_state)

    if  st.session_state["photo"] == "done":
        progress_bar = col2.progress(0)
        for persen_bar in range(100):
            time.sleep(0.05)
            progress_bar.progress(persen_bar + 1)
        col2.success("Upload Foto Succesfully !")
        col3.metric(label="Temperatur",value="29 C",delta="3 C ")
        with  st.expander("Click to read more Picture"):
            st.write("Mana yang lebih baik dari gambar anda")

            if uploader_photo is None:
                st.image(camera_photo)
            else:
                st.image(uploader_photo)

    # st.write("This is a sample home page in the mutliapp.")
    # st.write("See `apps/home.py` to know how to use it.")

    # st.markdown("### Sample Data")
    # df = create_table()
    # st.write(df)

    # st.write('Navigate to `Data Stats` page to visualize the data')


