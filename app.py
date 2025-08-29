import streamlit as st
import pandas as pd
import random

# -----------------------------
# Load Datasets
# -----------------------------
dad_jokes_file = "dad_jokes.csv"
quotes_file = "quotes.json"  # JSON file with 'Quote' and 'Author'

@st.cache_data
def load_data():
    # Load jokes
    try:
        jokes_df = pd.read_csv(dad_jokes_file)
    except FileNotFoundError:
        st.error(f"Jokes file '{dad_jokes_file}' not found!")
        jokes_df = pd.DataFrame(columns=["joke"])

    # Load quotes
    try:
        quotes_df = pd.read_json(quotes_file)
        # Rename columns to lowercase for consistency
        quotes_df = quotes_df.rename(columns={"Quote": "quote", "Author": "author"})
    except FileNotFoundError:
        st.error(f"Quotes file '{quotes_file}' not found!")
        quotes_df = pd.DataFrame(columns=["quote", "author"])
    except ValueError:
        st.error(f"Quotes file '{quotes_file}' is not a valid JSON!")
        quotes_df = pd.DataFrame(columns=["quote", "author"])

    return jokes_df, quotes_df

jokes_df, quotes_df = load_data()

# -----------------------------
# Streamlit UI
# -----------------------------
st.set_page_config(page_title="Joke & Quote Generator", page_icon="🎭", layout="centered")
st.title("🎭 Joke & Quote Generator")
st.write("Need a laugh or some inspiration? Pick one below!")

# Sidebar Choice
option = st.sidebar.radio("Choose mode:", ("Jokes", "Quotes"))

# -----------------------------
# Jokes Section
# -----------------------------
if option == "Jokes":
    if st.button("Tell me a Joke 🤣"):
        valid_jokes = jokes_df["joke"].dropna().tolist()
        if valid_jokes:
            joke = random.choice(valid_jokes)
            st.success(joke)
        else:
            st.warning("No jokes found in the dataset!")

# -----------------------------
# Quotes Section
# -----------------------------
elif option == "Quotes":
    if st.button("Give me a Quote 💡"):
        if "quote" in quotes_df.columns and "author" in quotes_df.columns:
            valid_quotes = quotes_df[quotes_df["quote"].notna()]
            if not valid_quotes.empty:
                quote = random.choice(valid_quotes.to_dict(orient="records"))
                st.info(quote["quote"])
                if quote.get("author"):
                    with st.expander("Author"):
                        st.success(quote["author"])
            else:
                st.warning("No quotes found in the dataset!")
        else:
            st.error("JSON file must contain 'Quote' and 'Author' fields!")

# -----------------------------
# Footer
# -----------------------------
st.markdown("---")
st.caption("Made with ❤️ using Streamlit")











