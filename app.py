import streamlit as st
import pandas as pd
import plotly.express as px

# Configuration
st.set_page_config(page_title="HEAL-4WARD Clinical Tool", layout="wide")

# Load your specific research data
# If your file is named 'HEAL_4WARD_Undeniable_Research_Data (1).csv', use that name below
try:
    df = pd.read_csv('data.csv') 
except:
    st.error("File 'data.csv' not found. Please rename your uploaded CSV file to 'data.csv' on GitHub.")
    st.stop()

st.title("🛡️ Chronic Wound Biofilm: Therapeutic Selector")
st.markdown("This system analyzes multispecies biofilm disruption efficacy based on your experimental characterization data.")

# Sidebar for precise targeting
st.sidebar.header("Clinical Pathogen Selector")
pathogen = st.sidebar.selectbox("Select Target Pathogen", df['Target_Bacteria'].unique())
target_zeta = st.sidebar.slider("Minimum Required Zeta Potential (mV)", -30.0, 50.0, 0.0)

# Filter Data (The 'Solution' Logic)
filtered = df[(df['Target_Bacteria'] == pathogen) & (df['Zeta_Potential_mV'] >= target_zeta)]

if not filtered.empty:
    # Identify the best performing candidate
    best = filtered.loc[filtered['Disruption_Efficacy_Pct'].idxmax()]
    
    st.success(f"**Recommended Formulation:** {best['Sample_ID']}")
    
    col1, col2 = st.columns(2)
    col1.metric("Disruption Efficacy", f"{best['Disruption_Efficacy_Pct']:.1f}%")
    col2.metric("Biofilm Reduction", f"{best['Biofilm_Formation_Reduction_Pct']:.1f}%")
    
    # Visualization for the research committee
    fig = px.scatter(filtered, x='SAXS_Radius_Gyration_nm', y='Disruption_Efficacy_Pct',
                     size='FTIR_Carbonyl_cm_1', color='Zeta_Potential_mV',
                     title=f"Optimization Landscape for {pathogen}")
    st.plotly_chart(fig, use_container_width=True)
else:
    st.warning("No formulation matches these criteria. Suggest adjusting synthesis parameters.")
