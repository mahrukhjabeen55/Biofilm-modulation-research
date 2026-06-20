import streamlit as st
import pandas as pd
import plotly.express as px

st.set_page_config(layout="wide")
st.title("HEAL-4WARD: Biofilm Modulation Decision Engine")

# Load your research dataset
df = pd.read_csv('data.csv')

# --- SIDEBAR: Advanced Parameter Input ---
st.sidebar.header("Experimental Optimization")
target_bacteria = st.sidebar.selectbox("Select Target Multispecies Model", df['Target_Bacteria'].unique())
min_efficacy = st.sidebar.slider("Minimum Required Disruption Efficacy (%)", 0, 100, 50)

# --- FILTERING LOGIC ---
filtered_df = df[(df['Target_Bacteria'] == target_bacteria) & 
                 (df['Disruption_Efficacy_Pct'] >= min_efficacy)]

# --- MAIN DASHBOARD: Professional Visualization ---
col1, col2 = st.columns([1, 1])

with col1:
    st.write("### Quantitative Analysis: Structural Correlations")
    fig = px.scatter(filtered_df, x='SAXS_Radius_Gyration_nm', y='Disruption_Efficacy_Pct', 
                     size='TGA_Stability_C', color='Zeta_Potential_mV',
                     hover_data=['Sample_ID'], title="Structural Morphology vs. Biofilm Disruption")
    st.plotly_chart(fig, use_container_width=True)

with col2:
    st.write("### Elite Candidate Selection")
    st.dataframe(filtered_df[['Sample_ID', 'FTIR_Carbonyl_cm_1', 'Disruption_Efficacy_Pct', 'Biofilm_Formation_Reduction_Pct']])
    
    # Practical Recommendation
    if not filtered_df.empty:
        elite = filtered_df.loc[filtered_df['Disruption_Efficacy_Pct'].idxmax()]
        st.success(f"Optimal Nanostructure Identified: {elite['Sample_ID']}")
        st.metric("Max Disruption Efficacy", f"{elite['Disruption_Efficacy_Pct']:.2f}%")

# --- RESEARCH OBJECTIVE BRIDGE ---
st.markdown("---")
st.write("### Scientific Integration Statement")
st.info("This framework integrates polymeric nanostructure characterization (FTIR/SAXS/TGA) with microbiological assays to predict biofilm resilience. "
        "By mapping structural parameters to antimicrobial efficacy, this engine identifies optimal topologies for multispecies biofilm disruption in chronic wounds.")
