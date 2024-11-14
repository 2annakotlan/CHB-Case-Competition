from custom_css_file import get_custom_css_page
from nth_degree_file import get_nth_degree_page

def get_activities_recommender_page(df_degree):
  get_custom_css_page(alignment="center", button_span="full")
  st.dataframe(df_degree.head())

  


  
