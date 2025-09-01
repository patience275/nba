import streamlit as st
import pickle

with open('saved_steps.pkl','rb') as f: 
    saved_steps=pickle.load(f)

scaler=saved_steps['scaler']
cosine_similarity=saved_steps['cosine_similarity']
players_scaled=saved_steps['players_scaled.pkl']    

st.title('WNBA Player Similarity App')
st.write('This app finds the most similar WNBA players based on their statistics.') 
st.slider('age',min_value=19,max_value=39,step=1)
st.slider('PER',min_value=-36.1,max_value=55.5,step=0.1)
st.slider('TS%',min_value=0.0,max_value=0.95,step=0.01)
st.slider('3PAr',min_value=0.0,max_value=1.0,step=0.01)
st.slider('FTr',min_value=0.0,max_value=2.0,step=0.01)
st.slider('ORB%',min_value=0.0,max_value=53.90,step=0.1)
st.slider('DRB%',min_value=0.0,max_value=100.0,step=0.1)
st.slider('TRB%',min_value=0.0,max_value=53.50,step=0.1)
st.slider('AST%',min_value=0.0,max_value=57.10,step=0.1)
st.slider('STL%',min_value=0.0,max_value=18.7,step=0.1)
st.slider('BLK%',min_value=0.0,max_value=15.6,step=0.1)
st.slider('TOV%',min_value=0.0,max_value=100.0,step=0.1)
st.slider('USG%',min_value=0.0,max_value=172.5,step=0.1)
st.slider('OWS',min_value=--2.50,max_value=12.0,step=0.1)
st.slider('DWS',min_value=-0.0,max_value=5.8,step=0.1)
st.slider('WS',min_value=-1.70,max_value=17.0,step=0.1)
st.slider('WS/48',min_value=-1.20,max_value=0.67,step=0.001)
st.slider('OBPM',min_value=-30.3,max_value=29.1,step=0.1)
st.slider('DBPM',min_value=-10.1,max_value=16.0,step=0.1)
st.slider('BPM',min_value=-33.9,max_value=43.3,step=0.1)
st.slider('VORP',min_value=-1.7,max_value=10.60, step=0.1)

st.write('how do you think the --maters to you?')
st.slider('age',min_value=1,max_value=1)
st.slider('PER',min_value=0,max_value=1)
st.slider('TS%',min_value=0,max_value=1)
st.slider('3PAr',min_value=0,max_value=1)
st.slider('FTr',min_value=0,max_value=1)
st.slider('ORB%',min_value=0,max_value=1)
st.slider('DRB%',min_value=0,max_value=1)
st.slider('TRB%',min_value=0,max_value=1)
st.slider('AST%',min_value=0,max_value=1)
st.slider('STL%',min_value=0,max_value=1)
st.slider('BLK%',min_value=0,max_value=1)
st.slider('TOV%',min_value=0,max_value=1)
st.slider('USG%',min_value=0,max_value=1)
st.slider('OWS',min_value=0,max_value=1)
st.slider('DWS',min_value=0,max_value=1)
st.slider('WS',min_value=0,max_value=1)
st.slider('WS/48',min_value=0,max_value=1)
st.slider('OBPM',min_value=0,max_value=1)
st.slider('DBPM',min_value=0,max_value=1)
st.slider('BPM',min_value=0,max_value=1)
st.slider('VORP',min_value=0,max_value=1)


st.button('Find Similar Players')
st.write('Most similar players are:')
