import streamlit as st 
import pandas as pd
import joblib
from app_frame import app_frame
import base64

def main():
    st.title("Mushroom Prediction&#127812;")

    html_temp= """
    <div style="background-color:Blanchedalmond;padding:15px">
    <h2 style="color:black;text-align:center;">Are your mushrooms edible or poisonous? Find out now!..</h2>
    </div>
    """
    st.markdown(html_temp,unsafe_allow_html=True)

    upload_file=st.file_uploader('Choose a csv file')
    html_temp="""
    <div style="background-color:Blanchedalmond;padding:3px">
    </div>
    """
    st.markdown(html_temp,unsafe_allow_html=True)
    
    if upload_file:
        data=pd.read_csv(upload_file)
        file=app_frame.data_clean(df=data)
        loaded_model = joblib.load(open("models/model.pkl", 'rb'))
        model = pd.DataFrame(loaded_model.predict(file))
        result=model.replace({0:'Edible', 1:'Poisonous'})
        st.dataframe(result)

    download=st.button('Download Prediction')
    
    if download:
        csv = result.to_csv(index=False)
        b64 = base64.b64encode(csv.encode()).decode()
        linko= f'<a href="data:file/csv;base64,{b64}" download="mushrooms_prediction.csv">Download csv file</a>'
        st.markdown(linko,unsafe_allow_html=True)
        'Click to download'

if __name__=='__main__':
    main()