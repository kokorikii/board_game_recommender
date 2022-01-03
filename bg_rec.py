import streamlit as st
import pandas as pd
import numpy as np

st.title('Find Your Next Boardgame')
st.header('Choose one of your favorite boardgames from the dropdown and get 10 recommendations based on your choice')
st.markdown('---')

dataframe = pd.read_csv('./data/rec_df.csv', index_col='name')

option = st.selectbox(
    'Choose one of your favorite boardgames',
    dataframe.index
)

'You selected ', option

temp_df = 1 - dataframe[option].sort_values()[1:11]

final_df = temp_df.rename(index={0: 'Similarity Score (0 - 10)'})

st.table(final_df)