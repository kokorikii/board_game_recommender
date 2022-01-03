import streamlit as st
import pandas as pd
import numpy as np

pd.set_option('display.max_colwidth', -1)
pd.options.display.float_format = '{:.2%}'.format

st.title('Find Your Next Boardgame')
st.header('Choose one of your favorite boardgames from the dropdown and get 10 recommendations based on your choice')
st.markdown('---')

dataframe = pd.read_csv('./data/rec_df.csv', index_col='name')

option = st.selectbox(
    'Choose one of your favorite boardgames',
    dataframe.index
)

'You selected ', option

temp_df = 1 - dataframe[option].sort_values()[1:11].rename('Similarity Score')
temp_df = pd.DataFrame(temp_df)

# read in info csv which contains meta info for each board game
info_df = pd.read_csv('./data/info_df.csv', index_col='name')

final_df = temp_df.join(info_df)
final_df['Similarity Score'] = final_df['Similarity Score']

def path_to_image_html(path):
    '''
     This function will convert the URL in the thumbnail column to be formatted as HTML.
    '''

    return '<img src="'+ path + '" style=max-height:124px;"/>'

# st.dataframe(final_df)
st.write(final_df.to_html(escape=False, formatters=dict(Thumbnail=path_to_image_html)), unsafe_allow_html=True)