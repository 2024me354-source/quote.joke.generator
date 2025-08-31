import streamlit as st
import pandas as pd
import random

# -----------------------------
# Load Jokes Dataset
# -----------------------------
dad_jokes_file = "dad_jokes.csv"  # keep your jokes CSV in repo

@st.cache_data
def load_jokes():
    try:
        jokes_df = pd.read_csv(dad_jokes_file)
    except FileNotFoundError:
        st.error(f"Jokes file '{dad_jokes_file}' not found!")
        jokes_df = pd.DataFrame(columns=["joke"])
    return jokes_df

jokes_df = load_jokes()

# -----------------------------
# Built-in Quotes Dataset
# -----------------------------
quotes_list = [
    {"quote": "Be yourself; everyone else is already taken.", "author": "Oscar Wilde"},
    {"quote": "Two things are infinite: the universe and human stupidity; and I'm not sure about the universe.", "author": "Albert Einstein"},
    {"quote": "So many books, so little time.", "author": "Frank Zappa"},
    {"quote": "A room without books is like a body without a soul.", "author": "Marcus Tullius Cicero"},
    {"quote": "You only live once, but if you do it right, once is enough.", "author": "Mae West"},
    {"quote": "Be the change that you wish to see in the world.", "author": "Mahatma Gandhi"},
    {"quote": "In three words I can sum up everything I've learned about life: it goes on.", "author": "Robert Frost"},
    {"quote": "If you tell the truth, you don't have to remember anything.", "author": "Mark Twain"},
    {"quote": "A friend is someone who knows all about you and still loves you.", "author": "Elbert Hubbard"},
    {"quote": "Always forgive your enemies; nothing annoys them so much.", "author": "Oscar Wilde"},
    {"quote": "Live as if you were to die tomorrow. Learn as if you were to live forever.", "author": "Mahatma Gandhi"},
    {"quote": "To live is the rarest thing in the world. Most people exist, that is all.", "author": "Oscar Wilde"},
    {"quote": "Without music, life would be a mistake.", "author": "Friedrich Nietzsche"},
    {"quote": "We accept the love we think we deserve.", "author": "Stephen Chbosky"},
    {"quote": "It is better to be hated for what you are than to be loved for what you are not.", "author": "André Gide"},
    {"quote": "The man who does not read has no advantage over the man who cannot read.", "author": "Mark Twain"},
    {"quote": "It does not do to dwell on dreams and forget to live.", "author": "J.K. Rowling"},
    {"quote": "Good friends, good books, and a sleepy conscience: this is the ideal life.", "author": "Mark Twain"},
    {"quote": "Life is what happens to us while we are making other plans.", "author": "Allen Saunders"},
    {"quote": "Not all of us can do great things. But we can do small things with great love.", "author": "Mother Teresa"}
]

# -----------------------------
# Streamlit Config & Custom CSS
# -----------------------------
st.set_page_config(page_title="Joke & Quote Generator", page_icon="🎭", layout="centered")

st.markdown("""
    <style>
    body {
        background: linear-gradient(135deg, #1d2671, #c33764);
    }
    .main {
        background-color: transparent;
    }
    .stApp {
        background: linear-gradient(135deg, #1d2671, #c33764);
        color: white;
    }
    .card {
        background: white;
        border-radius: 20px;
        padding: 2rem;
        color: black;
        text-align: center;
        box-shadow: 0 10px 30px rgba(0,0,0,0.25);
        margin-top: 2rem;
    }
    .title {
        font-size: 2rem;
        color: #1d2671;
        margin-bottom: 1rem;
    }
    .btn {
        display: inline-block;
        padding: 0.7rem 1.3rem;
        border-radius: 12px;
        font-size: 1rem;
        font-weight: bold;
        cursor: pointer;
        color: white;
        margin: 0.5rem;
        text-decoration: none;
    }
    .joke-btn { background: #e63946; }
    .quote-btn { background: #2a9d8f; }
    </style>
""", unsafe_allow_html=True)

# -----------------------------
# UI Layout
# -----------------------------
st.markdown("<div class='card'>", unsafe_allow_html=True)
st.markdown("<div class='title'>🎭 Joke & Quote Generator</div>", unsafe_allow_html=True)
st.write("Need a laugh or some inspiration? Pick one below!")

col1, col2 = st.columns(2)

with col1:
    if st.button("🤣 Tell me a Joke", key="joke_btn"):
        valid_jokes = jokes_df["joke"].dropna().tolist()
        if valid_jokes:
            joke = random.choice(valid_jokes)
            st.success(joke)
        else:
            st.warning("No jokes found in the dataset!")

with col2:
    if st.button("💡 Give me a Quote", key="quote_btn"):
        quote = random.choice(quotes_list)
        st.info(quote["quote"])
        st.caption(f"— {quote['author']}")

st.markdown("</div>", unsafe_allow_html=True)

# -----------------------------
# Footer
# -----------------------------
st.markdown("<br><hr><center>Made with ❤️ using Streamlit</center>", unsafe_allow_html=True)


