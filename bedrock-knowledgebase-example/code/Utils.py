import streamlit as st

def remove_duplicates(data):
    """Removes duplicates from a list of dictionaries based on the 's3Location' key.

      Args:
          data: A list of dictionaries.

      Returns:
      A new list with duplicates removed.
    """
    seen = set()
    unique_data = []
    for item in data:
        s3_location = item['s3Location']['uri']
        if s3_location not in seen:
          seen.add(s3_location)
          unique_data.append(item)
    location=[]
    for aa in unique_data:
        print(aa['s3Location']['uri'])
        location.append(aa['s3Location']['uri'])
        ', '.join(location)
    return location

def display_local_image(image_path, max_width=None, caption=None):
    """Displays a local image on the Streamlit UI with customization options.

    Args:
        image_path (str): The path to the local image file.
        max_width (int, optional): The maximum width for the image. Defaults to None.
        caption (str, optional): A caption for the image. Defaults to None.
    """

    try:
        with open(image_path, 'rb') as f:
            image_data = f.read()
            st.image(image_data, caption=caption, width=max_width)
    except FileNotFoundError:
        st.error(f"Image not found: {image_path}")
    except Exception as e:
        st.error(f"An error occurred displaying the image: {e}")