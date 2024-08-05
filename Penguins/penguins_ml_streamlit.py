import streamlit as st
import pickle
# Load model and unique mapping from pickle to respective variables
rf_pickle=open('rf_penguin.pickle','rb')
map_pickle=open('output_penguin.pickle','rb')
rfc=pickle.load(rf_pickle)
mapping=pickle.load(map_pickle)
rf_pickle.close()
map_pickle.close()

with st.form("penguin_form"):
# create avenues for user input 
    island=st.selectbox('Penguin Island',options=['Biscoe','Dream','Torgerson'])
    sex =st.selectbox('Sex',options=['Female','Male'])
    bill_length=st.number_input('Bill Lenght (mm)', min_value=0)
    bill_depth=st.number_input('Bill Depth (mm)',min_value=0)
    flipper_length=st.number_input('Flipper Lenght (mm)',min_value=0)
    body_mass=st.number_input('Body Mass(g)',min_value=0)
    # Create a Submit Button and a Submit Logic

    submitted = st.form_submit_button("Submit")
        
    if submitted:
    # Put sex and island variables in the correct format
        island_biscoe,island_dream,island_togerson=0,0,0
        if island=='Biscoe':
            island_biscoe=1
        elif island =='Dream':
            island_dream=1
        elif island == 'TOrgerson':
            island_togerson=1
        sex_female, sex_male =0,0
        if sex =='Female':
            sex_female=1
        elif sex=='Male':
            sex_male=1

        # use the prediction model to predict the species basis the user input
        prediction=rfc.predict([[bill_length,bill_depth,flipper_length,body_mass,island_biscoe,island_dream,island_togerson,sex_female,sex_male]])
        species=mapping[prediction][0]
        st.write(f'We predict your penguin is of the {species} species')