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
]

# -----------------------------
# Streamlit UI
# -----------------------------
st.set_page_config(page_title="Joke & Quote Generator", page_icon="🎭", layout="centered")

# Custom CSS Styling
st.markdown("""
    <style>
        /* Background Gradient */
        .stApp {
            background: linear-gradient(135deg, #1e3c72, #2a5298);
            color: white;
        }

        /* Title */
        h1 {
            text-align: center;
            font-size: 3rem;
            color: #ffcc00;
            text-shadow: 2px 2px 8px #000;
        }

        /* Buttons */
        div.stButton > button {
            background: #ff7b00;
            color: white;
            font-size: 1.2rem;
            border-radius: 12px;
            padding: 12px 20px;
            border: none;
            box-shadow: 2px 4px 10px rgba(0,0,0,0.4);
            transition: 0.3s;
        }
        div.stButton > button:hover {
            background: #ff9500;
            transform: scale(1.05);
        }

        /* Output card - jokes */
        .joke-box {
            background: rgba(0, 0, 0, 0.85);
            padding: 20px;
            border-radius: 15px;
            font-size: 1.3rem;
            text-align: center;
            color: #00ffcc;
            border: 2px solid #00ffcc;
            box-shadow: 0px 0px 12px rgba(0, 255, 204, 0.6);
            font-weight: bold;
            margin-top: 20px;
        }

        /* Output card - quotes */
        .quote-box {
            background: rgba(0, 0, 0, 0.85);
            padding: 20px;
            border-radius: 15px;
            font-size: 1.3rem;
            text-align: center;
            color: #ffcc00;
            border: 2px solid #ffcc00;
            box-shadow: 0px 0px 12px rgba(255, 204, 0, 0.6);
            font-weight: bold;
            margin-top: 20px;
        }

        /* Author styling */
        .author {
            margin-top: 10px;
            font-size: 1rem;
            color: #ffffff;
            font-style: italic;
        }

        /* Footer */
        .footer {
            text-align: center;
            margin-top: 50px;
            color: #ddd;
            font-size: 0.9rem;
        }
    </style>
""", unsafe_allow_html=True)

# Title
st.markdown("<h1>🎭 Joke & Quote Generator</h1>", unsafe_allow_html=True)
st.write("<p style='text-align:center;'>Need a laugh or some inspiration? Pick one below!</p>", unsafe_allow_html=True)

col1, col2 = st.columns(2)

# -----------------------------
# Jokes Section
# -----------------------------
with col1:
    if st.button("🤣 Tell me a Joke"):
        valid_jokes = jokes_df["joke"].dropna().tolist()
        if valid_jokes:
            joke = random.choice(valid_jokes)
            st.markdown(f"<div class='joke-box'>{joke}</div>", unsafe_allow_html=True)
        else:
            st.warning("No jokes found in the dataset!")

# -----------------------------
# Quotes Section
# -----------------------------
with col2:
    if st.button("💡 Give me a Quote"):
        quote = random.choice(quotes_list)
        st.markdown(f"<div class='quote-box'>{quote['quote']}<div class='author'>- {quote['author']}</div></div>", unsafe_allow_html=True)

# -----------------------------
# Footer
# -----------------------------
st.markdown("<div class='footer'>Made with ❤️ using Streamlit</div>", unsafe_allow_html=True)





