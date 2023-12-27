import streamlit as st
import requests
st.set_page_config(
    page_title="Dictionary",
    page_icon=":chart_with_upwards_trend:",
    layout="centered",
    initial_sidebar_state="expanded",
)
def loadcss(filename):
    with open(filename) as f:
        st.markdown(f"<style>{f.read()}</style>",unsafe_allow_html=True)
loadcss('styles/style.css')
st.markdown('## Welcome to the Dictionary App')
st.markdown('### Search for meanings of English words')

# Include a brief introduction
st.markdown('''
    This app allows you to search for the meanings of English words. Enter a word in the search box and click 'Search' to get Meanings/definitions.
    ''')
def fetch_meaning(word):
    url=f'https://api.dictionaryapi.dev/api/v2/entries/en/{word}'
    res=requests.get(url)
    if res.status_code==200:
        data=res.json()
        return data 
    return None
    
search_query=st.text_input("Enter the query")

if st.button("Search"):
    if search_query:
        meaning_data=fetch_meaning(search_query)
        if meaning_data:
            # Display the meanings retrieved from the API
            st.write(f"Meanings of '{search_query}':")
            for meaning in meaning_data:
                for part_of_speech in meaning['meanings']:
                    pos = part_of_speech['partOfSpeech']
                    definitions = part_of_speech.get('definitions', [])
                    st.write(f"- Part of Speech: {pos}")
                    if definitions:
                        for definition in definitions:
                            st.write(f"  - Definition: {definition.get('definition', 'N/A')}")
        else:
            st.write("Word not found or API request failed.")
    else:
        st.write("Please enter a word.")
        
