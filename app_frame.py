from sklearn.preprocessing import LabelEncoder

class app_frame:
    def __init__(self) -> None:
        pass

    def data_clean(df):
        encoder = LabelEncoder()
        for column in range(len(df.columns)):
            df[df.columns[column]]= encoder.fit_transform(df[df.columns[column]])
        return df