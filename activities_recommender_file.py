from custom_css_file import get_custom_css_page
from nth_degree_file import second_degree

def get_activities_recommender_page(second_degree):
  get_custom_css_page(alignment="center", button_span="full")
  st.dataframe(second_degree.head())

  


  
