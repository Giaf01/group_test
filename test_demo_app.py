# API Key: AIzaSyCYSlwK_6UxkKN1cavKJh-HvEFj_M01jy4

import streamlit as st

# Google Maps API key (replace with your own key)
API_KEY = 'AIzaSyCYSlwK_6UxkKN1cavKJh-HvEFj_M01jy4'

# Function to generate HTML code for Google Maps
def generate_map_html(latitude, longitude):
    return f"""
        <iframe
            width="600"
            height="450"
            frameborder="0" style="border:0"
            src="https://www.google.com/maps/embed/v1/place?key={API_KEY}&q={latitude},{longitude}" allowfullscreen>
        </iframe>
    """

# List of universities (replace with your own data)
universities = {
    'Harvard University': (42.3744, -71.1169),
    'Stanford University': (37.4275, -122.1697),
    'Massachusetts Institute of Technology (MIT)': (42.3601, -71.0942)
}

# streamlit app
def main():
    st.title('Uniswap Map')

    st.title('This is a test from Miguel')

    # Select university
    selected_university = st.selectbox('Select a university', list(universities.keys()))

    # Get coordinates of selected university
    latitude, longitude = universities[selected_university]

    # Generate HTML code for Google Maps
    map_html = generate_map_html(latitude, longitude)

    # Display Google Maps map
    st.components.v1.html(map_html, width=700, height=500)

if __name__ == '__main__':
    main()



