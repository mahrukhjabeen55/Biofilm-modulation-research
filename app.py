import streamlit as st
import pandas as pd

st.title("HEAL-4WARD: Research Data Dashboard")

# Load your specific file
df = pd.read_csv('HEAL_4WARD_Undeniable_Research_Data (1)_3.csv')

st.write("### Research Data Fingerprints")
st.dataframe(df)

st.write("This dashboard provides a transparent overview of my nanostructure characterization and biofilm modulation research.")
