import streamlit as st
import pandas as pd
import random

# -----------------------------
# Load Jokes Dataset
# -----------------------------
dad_jokes_file = "dad_jokes.csv"

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
    {"quote": "Without music, life would be a mistake.", "author": "Friedrich Nietzsche"},
]

# -----------------------------
# Streamlit Page Config
# -----------------------------
st.set_page_config(page_title="Joke & Quote Generator", page_icon="🎭", layout="centered")

# -----------------------------
# Custom CSS
# -----------------------------
st.markdown("""
    <style>
    /* Background Gradient */
    .stApp {
        background: linear-gradient(135deg, #1e3c72, #2a5298, #f12711, #f5af19);
        background-size: 400% 400%;
        animation: gradientBG 12s ease infinite;
        color: white;
    }

    @keyframes gradientBG {
        0% {background-position: 0% 50%;}
        50% {background-position: 100% 50%;}
        100% {background-position: 0% 50%;}
    }

    /* Title */
    h1 {
        text-align: center;
        font-size: 3rem;
        color: #fff;
        text-shadow: 2px 2px 4px #00000055;
    }

    /* Buttons */
    div.stButton > button {
        background-color: #ff7b00;
        color: white;
        border-radius: 12px;
        padding: 12px 24px;
        font-size: 18px;
        font-weight: bold;
        box-shadow: 0px 4px 6px rgba(0,0,0,0.3);
        transition: 0.3s;
    }
    div.stButton > button:hover {
        background-color: #ff9500;
        transform: scale(1.05);
    }

    /* Output card */
    .st-success, .st-info {
        background: rgba(255, 255, 255, 0.15);
        padding: 20px;
        border-radius: 15px;
        font-size: 1.2rem;
        text-align: center;
        color: #fff;
        border: 1px solid #ffffff55;
    }

    /* Footer */
    footer {
        text-align: center;
        color: #fff;
        margin-top: 40px;
    }
    </style>
""", unsafe_allow_html=True)

# -----------------------------
# App UI
# -----------------------------
st.title("🎭 Joke & Quote Generator")
st.write("Need a **laugh** or some **inspiration**? Pick one below 👇")

col1, col2 = st.columns(2)

with col1:
    if st.button("🤣 Tell me a Joke"):
        valid_jokes = jokes_df["joke"].dropna().tolist()
        if valid_jokes:
            joke = random.choice(valid_jokes)
            st.success(joke)
        else:
            st.warning("⚠️ No jokes found in the dataset!")

with col2:
    if st.button("💡 Inspire Me"):
        quote = random.choice(quotes_list)
        st.info(f"“{quote['quote']}”\n\n— {quote['author']}")

# -----------------------------
# Footer
# -----------------------------
st.markdown("<footer>✨ Made with ❤️ using Streamlit ✨</footer>", unsafe_allow_html=True)




