import streamlit as st
import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd
import pickle
from sklearn.metrics import accuracy_score
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
import altair as alt

penguin_file=st.file_uploader('upload your own penguin data',type=['csv'])
if penguin_file is None:
    st.stop()
else:
    penguin_df=pd.read_csv(penguin_file)
    penguin_df=penguin_df.dropna()
    output=penguin_df['species']
    features=penguin_df[['island','bill_length_mm','bill_depth_mm','flipper_length_mm','body_mass_g','sex']]
    features=pd.get_dummies(features)
    output,mapping=pd.factorize(output)
    xtrain, xtest, ytrain, ytest = train_test_split(features,output,test_size=0.8)
    rfc=RandomForestClassifier(random_state=15)
    rfc.fit(xtrain.values,ytrain)
    ypred=rfc.predict(xtest.values)
    score=round(accuracy_score(ypred,ytest),2)
    st.write(f'We trained a random forest model on this data, it has a score of {score}, use the inputs below to try out the model')
    with st.form('User_input'):
        island=st.selectbox('Penguin Island',options=['Biscoe','Dream','Torgerson'])
        sex =st.selectbox('Sex',options=['Female','Male'])
        bill_length=st.number_input('Bill Length (mm)', min_value=0)
        bill_depth=st.number_input('Bill Depth (mm)',min_value=0)
        flipper_length=st.number_input('Flipper Length (mm)',min_value=0)
        body_mass=st.number_input('Body Mass(g)',min_value=0)
        # Create a Submit Button and a Submit Logic

        submitted = st.form_submit_button("Submit")
            
        if submitted:
        # Put sex and island variables in the correct format
            island_biscoe,island_dream,island_torgerson=0,0,0
            if island=='Biscoe':
                island_biscoe=1
            elif island =='Dream':
                island_dream=1
            elif island == 'Torgerson':
                island_torgerson=1
            sex_female, sex_male =0,0
            if sex =='Female':
                sex_female=1
            elif sex=='Male':
                sex_male=1

            prediction=rfc.predict([[bill_length,bill_depth,flipper_length,body_mass,island_biscoe,island_dream,island_torgerson,sex_female,sex_male]])
            species=mapping[prediction][0]
            st.write(f'We predict your penguin is of the {species} species')
            st.write(f' The features used in the this prediction are ranked by relative importance below')
            fig,ax=plt.subplots()
            ax=sns.barplot(x=rfc.feature_importances_,y=features.columns)
            plt.title('Which features are the most important for species prediction?')
            plt.xlabel('Importance')
            plt.ylabel('feature')
            plt.tight_layout()
            st.pyplot(fig)
            st.write('''Below are the histograms for each continous variable seperated by penguin  species. 
                     The Vertical line represents your inputted value''')
            #plot bill length
            fig,ax=plt.subplots()
            ax=sns.displot(x=penguin_df['bill_length_mm'], hue=penguin_df['species'])
            plt.axvline(bill_length)
            plt.title('Bill length by species')
            st.pyplot(ax)
            #plot bill depth
            fig,ax=plt.subplots()
            ax=sns.displot(x=penguin_df['bill_depth_mm'], hue=penguin_df['species'])
            plt.axvline(bill_depth)
            plt.title('Bill Depth by Species')
            st.pyplot(ax)
            

            #plot flipper lenght using sns
            fig,ax=plt.subplots()
            ax=sns.displot(x=penguin_df['flipper_length_mm'], hue=penguin_df['species'])
            plt.axvline(flipper_length)
            plt.title('Flipper Length by Species')
            st.pyplot(ax)

            # plot flipper length suing altair
            hist=(alt.Chart(penguin_df)
                  .mark_bar().encode(x='flipper_length_mm', y='count()', color="species")
                  .interactive()
                  .properties(title='Flipper Length by species'))
            
            line = alt.Chart(pd.DataFrame({'flipper_length': [flipper_length]})).mark_rule(color='brown').encode(
                x='flipper_length')
            chart=hist+line
            st.altair_chart(chart)

