from custom_css_file import get_custom_css_page
from nth_degree_file import get_full_df
import streamlit as st

def get_activities_recommender_page(df):
  get_custom_css_page(alignment="center", button_span="full")
  full_df = get_full_df(df)
  st.dataframe(full_df.head())

  


  
