import streamlit as st
import pandas as pd
import random

# -----------------------------
# Load Jokes Dataset
# -----------------------------
dad_jokes_file = "dad_jokes.csv"  # CSV should have a "joke" column

@st.cache_data
def load_jokes():
    try:
        jokes_df = pd.read_csv(dad_jokes_file)
    except FileNotFoundError:
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
]

# -----------------------------
# Streamlit UI Setup
# -----------------------------
st.set_page_config(page_title="🎭 Joke & Quote Generator", page_icon="🎭", layout="wide")

# Custom CSS
st.markdown("""
    <style>
    body {
        background: linear-gradient(135deg, #667eea, #764ba2);
        color: white;
    }
    .main-title {
        text-align: center;
        font-size: 40px;
        font-weight: bold;
        color: #fdfdfd;
        margin-bottom: 20px;
    }
    .card {
        background-color: white;
        color: black;
        padding: 20px;
        border-radius: 15px;
        box-shadow: 2px 4px 15px rgba(0,0,0,0.2);
        text-align: center;
    }
    .footer {
        text-align: center;
        color: #eee;
        margin-top: 50px;
        font-size: 14px;
    }
    </style>
""", unsafe_allow_html=True)

# Title
st.markdown("<div class='main-title'>🎭 Joke & Quote Generator</div>", unsafe_allow_html=True)
st.write("Need a laugh or some inspiration? Both are here 👇")

# -----------------------------
# Layout: Two columns
# -----------------------------
col1, col2 = st.columns(2)

# ---- Jokes Card ----
with col1:
    st.markdown("<div class='card'>", unsafe_allow_html=True)
    st.subheader("🤣 Random Joke")
    if st.button("Tell me a Joke!"):
        valid_jokes = jokes_df["joke"].dropna().tolist()
        if valid_jokes:
            joke = random.choice(valid_jokes)
            st.success(joke)
        else:
            st.warning("No jokes found in dataset!")
    st.markdown("</div>", unsafe_allow_html=True)

# ---- Quotes Card ----
with col2:
    st.markdown("<div class='card'>", unsafe_allow_html=True)
    st.subheader("💡 Inspiring Quote")
    if st.button("Give me a Quote!"):
        quote = random.choice(quotes_list)
        st.info(f"“{quote['quote']}”")
        st.caption(f"— {quote['author']}")
    st.markdown("</div>", unsafe_allow_html=True)

# Footer
st.markdown("<div class='footer'>Made with ❤️ using Streamlit</div>", unsafe_allow_html=True)



