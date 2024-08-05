import streamlit as st
import pandas as pd
import altair as alt
import time
st.title("Palmer's Penguins")
st.markdown("Use this Streamlit app to make your own scatterplot about penguins!")

penguin_file=st.file_uploader("Select your own Penguin CSV(default provided)")
@st.cache_data()
# Defining the Load_file function
def load_file(penguin_file):
    time.sleep(3)
    if penguin_file is not None:
        df=pd.read_csv(penguin_file)
    else:
        #st.stop()
        df=pd.read_csv('penguins.csv')
    return(df)

#calling the load_file function
penguins_df=load_file(penguin_file)
    # penguins_df=pd.read_csv('penguins.csv')

# selected_species= st.selectbox("What species?", ["Adelie","Gentoo","Chinstrap"])
x_var=st.selectbox("Choose X variable?",["bill_length_mm","bill_depth_mm","flipper_length_mm","body_mass_g"])
y_var=st.selectbox("Choose Y variable?",["bill_length_mm","bill_depth_mm","flipper_length_mm","body_mass_g"])

# penguins_df=penguins_df[penguins_df["species"]==selected_species]
alt_chart=(alt.Chart(penguins_df,title=f"Scatterplot of Palmer's Penguins")
           .mark_circle()
           .encode(x=x_var, y=y_var, color="species")
           .interactive())
st.altair_chart(alt_chart,use_container_width=True)
