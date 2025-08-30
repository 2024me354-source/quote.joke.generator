import streamlit as st
import pandas as pd
import random

# -----------------------------
# Load Datasets
# -----------------------------
dad_jokes_file = "dad_jokes.csv"

@st.cache_data
def load_data():
    # Load jokes
    try:
        jokes_df = pd.read_csv(dad_jokes_file)
    except FileNotFoundError:
        st.error(f"Jokes file '{dad_jokes_file}' not found!")
        jokes_df = pd.DataFrame(columns=["joke"])
    return jokes_df

jokes_df = load_data()

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
# Quotes Section (with file uploader)
# -----------------------------
elif option == "Quotes":
    uploaded_file = st.file_uploader("Upload your file here", type=["json"])

    if uploaded_file is not None:
        try:
            quotes_df = pd.read_json(uploaded_file)
            quotes_df = quotes_df.rename(columns={"Quote": "quote", "Author": "author"})
        except ValueError:
            st.error("Uploaded file is not a valid JSON!")
            quotes_df = pd.DataFrame(columns=["quote", "author"])
    else:
        st.info("Please upload a Quotes JSON file to continue.")
        quotes_df = pd.DataFrame(columns=["quote", "author"])

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
