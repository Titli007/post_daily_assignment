import streamlit as st
import requests

# Set the title of the app
st.title("NewsGuard.AI : Stay Informed")

# Add custom CSS
custom_css = """
<style>
    .heading {
        color: white; 
        font-size: 29px; 
        margin: 30px;
    }
    .title {
        color: #4CAF50; 
        font-size: 36px; 
        text-align: center; 
    }
    .query-input {
        margin: 10px 0; 
        padding: 10px; 
        font-size: 16px; 
        border: 1px solid #ccc; 
        border-radius: 5px; 
    }
    .success {
        color: #4CAF50; 
    }
    .error {
        color: #f44336; 
    }
    .markdown-text {
        font-size: 18px; 
        line-height: 1.6; 
    }
</style>
"""
st.markdown(custom_css, unsafe_allow_html=True)

# Input for query and email
query = st.text_input("Enter your query:", placeholder="e.g., Weather in Bangalore")
email = st.text_input("Enter your email (optional):", placeholder="e.g., example@example.com")

if st.button("Fetch News"):
    # Call the backend API
    url = "http://localhost:5000/news"  # Adjust the URL as needed
    payload = {'query': query}
    if email:
        payload['email'] = email
    
    response = requests.post(url, json=payload)
    
    if response.status_code == 200:
        st.success("News fetched successfully!", icon="✅")
        data = response.json()

        st.markdown(f"<div class='markdown-text'>\n{data['message'][0]}</div>", unsafe_allow_html=True)
        st.image(data["message"][3])
        st.markdown(f'<a href={data["message"][2]}>Click here to read the full news: </a>', unsafe_allow_html=True)
        st.markdown(f"<div><b>Source : </b>{data["message"][1]}</div>", unsafe_allow_html=True)
    else:
        st.error("Error fetching news.", icon="🚫")
