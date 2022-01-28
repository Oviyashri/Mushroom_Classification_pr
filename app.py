import streamlit as st 
import pandas as pd
import joblib
from sklearn.preprocessing import LabelEncoder
import base64

def data_clean(df):
    encoder = LabelEncoder()
    for column in range(len(df.columns)):
        df[df.columns[column]]= encoder.fit_transform(df[df.columns[column]])
    return df

def main():
    st.title("Mushroom Prediction")
    html_temp= """
    <div style="background-color:black;padding:10px">
    <h2 style="color:white;text-align:center;">Are your mushrooms edible or poisonous? &#127812;</h2>
    </div>
    """
    st.markdown(html_temp,unsafe_allow_html=True)

    upload_file=st.file_uploader('Choose a csv file')
    if upload_file:
        data=pd.read_csv(upload_file)
        file=data_clean(df=data)
        loaded_model = joblib.load(open("models/model.pkl", 'rb'))
        model = pd.DataFrame(loaded_model.predict(file))
        result=model.replace({0:'Edible', 1:'Poisonous'})
        st.dataframe(result)

    download=st.button('Download')
    if download:
        csv = result.to_csv(index=False)
        b64 = base64.b64encode(csv.encode()).decode()
        href = f'<a href="data:file/csv;base64,{b64}">Download csv file</a>' 
        st.balloons()




if __name__=='__main__':
    main()