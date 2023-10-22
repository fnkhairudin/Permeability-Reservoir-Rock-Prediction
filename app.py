import streamlit as st
import pickle
import pandas as pd
import numpy as np
import base64

# load model
def load_model():
    file_name = "model/permeability_prediction.sav"
    with open(file_name, 'rb') as pickled:
        model = pickle.load(pickled)

    return model

model = load_model()

# set background, use base64 to read local file
def set_bg_hack(main_bg):
    '''
    A function to unpack an image from root folder and set as bg.
 
    Returns
    -------
    The background.
    '''
    # set bg name
    main_bg_ext = "jpg"
        
    st.markdown(
         f"""
         <style>
         .stApp {{
             background: url(data:image/{main_bg_ext};base64,{base64.b64encode(open(main_bg, "rb").read()).decode()});
             background-size: cover
         }}
         </style>
         """,
         unsafe_allow_html=True
     )

def page_view():
  # title
  st.markdown("<h1 style='text-align: center;'>Permeability(D) Prediction Based on Porosity and Connate Water Saturation</h1>", unsafe_allow_html=True)
  # line spacing with horizontal straight line
  st.markdown('***')

  # notes
  st.subheader(":spiral_note_pad: Notes:")
  note =f"""1. Limitation:
    - The purpose of this website is for demonstrate how machine learning is works. Not for production phase.
2. Model:
    - The model used is XGBoost (Extreme Gradient Boosting)
    - The prediction results can be off by approximately 0.019593 darcy (MAE) from the actual permeability, or in percentage terms the permeability prediction will be off by approximately 1.14% (MAPE) from the actual permeability.
    """
  # st.text_area("", note, height=50)
  # st.markdown(md, unsafe_allow_html=True)

  custom_css = '''
    <style>
        div.css-1om1ktf.e1y61itm0 {
          width: 1500px;
        }
    </style>
    '''
  st.markdown(custom_css, unsafe_allow_html=True)
  st.text_area("", note, height=270)

  # image background
  set_bg_hack("reports/rig.jpg")
  # image_rig = Image.open("reports/rig.jpg")
  # st.image(image_rig, '')
  
  # side bar title
  st.sidebar.header('Physical Properties of Reservoir Rocks')

# collect user input
def user_report():
  # slider of user input
  Porosity = st.sidebar.number_input(label="Porosity", min_value=0.000, max_value=0.476, step=0.001, format="%f")
  Swc = st.sidebar.number_input(label='Connate Water Saturation', min_value=0.000, max_value=1.000, step=0.001, format="%f")

  user_report_data = {
      'Porosity':Porosity,
      'Swc':Swc,
  }

  report_data = pd.DataFrame(user_report_data, index=['Data'])
  return report_data

def main():
    # page view
    page_view()

    # collect user input as tabulat format
    user_data = user_report()
    # st.header('Physical Properties of Reservoir Rocks')
    st.write(user_data)

    # predict the salary
    st.subheader('Permeability(D) Prediction:')
    if st.button("Predict you permeability here!"):
      permeability_pred = model.predict(user_data)
      st.subheader(str(np.round(permeability_pred[0], 10)) + ' ' + 'Darcy')

if __name__  == "__main__":
    main()