import streamlit as st
from PIL import Image
import os

# Define a dictionary with categories and corresponding images
categories = {
    'flower': 'path/to/flower_image.jpg',
    'vehicles': 'path/to/vehicle_image.jpg',
    'trees': 'path/to/tree_image.jpg',
    'mountains': 'path/to/mountain_image.jpg',
    'buildings': 'path/to/building_image.jpg'
}

# Initialize the Streamlit app
st.title('Image Search App')

# Create the search bar
search_term = st.text_input('Enter a search term:')

# Search logic: find the closest category from the search term
def find_closest_image(search_term):
    search_term = search_term.lower()
    if 'flower' in search_term or search_term in ['rose', 'tulip', 'daisy']:
        return categories['flower']
    elif 'vehicle' in search_term or search_term in ['car', 'tesla', 'truck']:
        return categories['vehicles']
    elif 'tree' in search_term or search_term in ['pine', 'oak', 'maple']:
        return categories['trees']
    elif 'mountain' in search_term or search_term in ['rainier', 'everest', 'kilimanjaro']:
        return categories['mountains']
    elif 'building' in search_term or search_term in ['skyscraper', 'house', 'paul allen center']:
        return categories['buildings']
    else:
        return None

# Display the closest image
if search_term:
    image_path = find_closest_image(search_term)
    if image_path:
        image = Image.open(image_path)
        st.image(image, use_column_width=True)
    else:
        st.write("No matching category found for the term: " + search_term)

# Run the following command in your terminal to install Streamlit if you haven't already:
# pip install streamlit

# To run the app, save this script as `app.py` and in the terminal run:
# streamlit run app.py
