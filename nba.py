import streamlit as st
import pandas as pd
import numpy as np

import pickle
with open('scaler.pkl', 'rb') as f:
    scaler = pickle.load(f)

st.title('NBA player discovery')
st.write('this webpp helps you get players based on your needs')
st.write('enter your needs')

fg = st.slider('FG', min_value=0.0, max_value=12.64, value=0.0, step=0.1)
fga = st.slider('FGA', min_value=0.0, max_value=23.34, value=0.0, step=0.01)
fg_pct = st.slider('FG%', min_value=0.0, max_value=1.00, value=0.0, step=0.01)
three_p = st.slider('3P', min_value=0.0, max_value=4.23, value=0.0, step=0.01)
three_pa = st.slider('3PA', min_value=0.0, max_value=12.21, value=0.0, step=0.01)
three_p_pct = st.slider('3P%', min_value=0.0, max_value=1.00, value=0.0, step=0.01)
ft = st.slider('FT', min_value=0.0, max_value=7.70, value=0.0, step=0.01)
fta = st.slider('FTA', min_value=0.0, max_value=10.73, value=0.0, step=0.01)
ft_pct = st.slider('FT%', min_value=0.0, max_value=1.00, value=0.0, step=0.01)
orb = st.slider('ORB', min_value=0.0, max_value=4.55, value=0.0, step=0.1)
drb = st.slider('DRB', min_value=0.0, max_value=10.43, value=0.0, step=0.1)
trb = st.slider('TRB', min_value=0.0, max_value=14.27, value=0.0, step=0.1)
ast = st.slider('AST', min_value=0.0, max_value=11.38, value=0.0, step=0.1)
stl = st.slider('STL', min_value=0.0, max_value=2.97, value=0.0, step=0.1)
blk = st.slider('BLK', min_value=0.0, max_value=3.88, value=0.0, step=0.1)
tov = st.slider('TOV', min_value=0.0, max_value=4.66, value=0.0, step=0.1)
pf = st.slider('PF', min_value=0.0, max_value=3.56, value=0.0, step=0.1) 

show_undervalued = st.checkbox('Show only undervalued players')



input_vector = [
    fg, fga, fg_pct, three_p, three_pa, three_p_pct,
    ft, fta, ft_pct, orb, drb, trb, ast, stl, blk, tov,pf]


import numpy as np
input_vector_scaled = scaler.transform([input_vector])

# Calculate gmsc/36 if not present
df = pd.read_csv('database_24_25.csv')
if 'gmsc/36' not in df.columns:
    df['gmsc/36'] = (df['GmSc'] / df['MP']) * 36

# Calculate undervalued if not present
if 'undervalued' not in df.columns:
    df['undervalued'] = (df['gmsc/36'] > df['gmsc/36'].quantile(0.75)) & (df['MP'] < df['MP'].median())

import pandas as pd
from sklearn.metrics.pairwise import euclidean_distances

# Load your player data (make sure columns match input_vector order)

perf_columns = ['FG', 'FGA', 'FG%', '3P', '3PA', '3P%', 'FT', 'FTA', 'FT%', 'ORB', 'DRB', 'TRB', 'AST', 'STL', 'BLK', 'TOV','PF']
perfomance = df[perf_columns]

# Scale the player data using the same scaler
perfomance_scaled = scaler.transform(perfomance)

# Calculate Euclidean distances
distances = euclidean_distances(perfomance_scaled, input_vector_scaled)

# Add distances to DataFrame
df['distance'] = distances

# Filter undervalued if checkbox is checked
if show_undervalued and 'undervalued' in df.columns:
    df = df[df['undervalued'] == True]

# ...existing code...

# Map slider variables to feature names and their default values
slider_defaults = {
    'FG': 0.0, 'FGA': 0.0, 'FG%': 0.0, '3P': 0.0, '3PA': 0.0, '3P%': 0.0,
    'FT': 0.0, 'FTA': 0.0, 'FT%': 0.0, 'ORB': 0.0, 'DRB': 0.0, 'TRB': 0.0,
    'AST': 0.0, 'STL': 0.0, 'BLK': 0.0, 'TOV': 0.0, 'PF': 0.0
}
slider_values = {
    'FG': fg, 'FGA': fga, 'FG%': fg_pct, '3P': three_p, '3PA': three_pa, '3P%': three_p_pct,
    'FT': ft, 'FTA': fta, 'FT%': ft_pct, 'ORB': orb, 'DRB': drb, 'TRB': trb,
    'AST': ast, 'STL': stl, 'BLK': blk, 'TOV': tov, 'PF': pf
}

# Find which features the user changed
chosen_features = [name for name, value in slider_values.items() if value != slider_defaults[name]]

# Always show 'Player' and 'distance'
display_columns = ['Player', 'distance'] + chosen_features

# Show top 10 most similar players with only chosen features
st.subheader("Top 10 Most Similar Players")
st.dataframe(df.sort_values('distance').head(10)[display_columns])

