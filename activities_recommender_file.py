from custom_css_file import get_custom_css_page
from nth_degree_file import get_full_df
import streamlit as st
from population_data_file import population_df

def get_activities_recommender_page(df):
  get_custom_css_page(alignment="center", button_span="full")

  st.dataframe(population_df)

  


  
