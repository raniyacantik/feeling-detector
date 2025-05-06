import streamlit as st 
from textblob import TextBlob 
st.title("Raniya Cantik Sekaliii rawr")
text = st.text_area("Enter lah lek: ")
if st.button("Analyze"):
    blob = TextBlob(text)
    polarity = blob.sentiment.polarity

    if polarity > 0:
        st.success("Sentiment: Positive 😘")
    elif polarity < 0:
        st.error("Sentiment: Negative 😒")
    else:
        st.info("Sentiment: Neutral 🐱‍👤")