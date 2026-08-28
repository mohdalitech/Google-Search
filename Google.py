from urllib.parse import quote
import streamlit as st
import requests
from playwright.sync_api import sync_playwright
st.title("Google Search")
topic=st.text_input("Enter your topic to search:",width=300)
sub_topic=st.text_input(f"Enter your subtopic of the {topic}:",width=300)
level=st.radio(
    f"Choose your current level in {topic}",
    ["Beginner","Intermediate","Advanced"],
    width=300
)
duration=st.number_input("Enter your preferred duration(in minutes):",width=300)
content_type=st.selectbox(
    "Choose your content type:",
    ["Tutorial","Course/Lecture","Explanation","Project","Practice"],
    width=300
    )
language=st.radio(
    "What is your preferred language?",
    ["English","Hindi","Hinglish","Any"],
    width=300
)
learning_preference=st.selectbox(
    "Which type of learning is mostly preferred by you?",
    ["Theory","Practical","Problem Solving","Project Based"],
    width=300
)
if st.button("Search",type="primary"):
    query=f"{topic} {sub_topic} {level} {content_type} {language} {learning_preference}"
    result=quote(query)
    url=f"https://www.google.com/search?q={result}"
    with sync_playwright() as p:
        browser=p.chromium.launch(headless=True)
        page=browser.new_page()
        input("Complete the Google verification, then press Enter...")
        results = page.locator("h3")

        for i in range(results.count()):
            title = results.nth(i).inner_text()
            url = results.nth(i).locator("xpath=..").get_attribute("href")

            st.write("Title:", title)
            st.link_button(f"Essential Resource {i+1}", url,type="primary")
            st.write("---")
