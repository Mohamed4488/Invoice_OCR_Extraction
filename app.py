import streamlit as st
from PIL import Image
from ocr import get_invoice_data
import os


# Image uploader
uploaded_file = st.file_uploader("Upload the image", type=["png", "jpg", "jpeg"])

if uploaded_file is not None:
    # Display the image
    image = Image.open(uploaded_file)
    st.image(image, caption="The displayed image", use_container_width=True)
    
    # Save the image to disk
    save_path = os.path.join("uploaded_images", uploaded_file.name)
    os.makedirs(os.path.dirname(save_path), exist_ok=True)
    image.save(save_path)
    st.success(f"The image has been saved: {save_path}")
    
    invoice_data = get_invoice_data(save_path)
    st.subheader("Ocr Result:")
    st.write(invoice_data)

