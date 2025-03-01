import streamlit as st
import pandas as pd

st.set_page_config(layout="wide")

def check_password():
    if st.session_state.get("authenticated"):
        return True

    password = st.text_input("Enter password:", type="password")
    if password == "bb_predictions_test":
        st.session_state["authenticated"] = True
        return True
    elif password:
        st.error("Incorrect password")
    return False

if check_password():
    # Your app code here
    st.write("Welcome to the app!")

    df_test = pd.read_csv('test_csv2.csv')
    df_test = df_test.drop(columns = 'Unnamed: 0')

    st.title("Predictions for next basketball matches (NBA and ProA)")

    st.write("Here are the predictions:")
    st.dataframe(df_test, use_container_width=True)
