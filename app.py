import streamlit as st
from langchain_community.document_loaders import YoutubeLoader

st.title("🎥 YouTube Transcript Extractor (English Videos)")

video_url = st.text_input("Enter YouTube Video URL:")
if st.button("Get Transcript"):
    if video_url:
        loader = YoutubeLoader.from_youtube_url(video_url)
        docs = loader.load()
        transcript = docs[0].page_content
        st.text_area("Transcript:", transcript, height=300)
    else:
        st.error("⚠️ Please enter a valid YouTube URL")
