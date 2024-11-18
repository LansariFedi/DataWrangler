from sklearn.preprocessing import StandardScaler, LabelEncoder

class DataWizard:
    def __init__(self):
        self.le = {}
        self.ss = StandardScaler()

    def clean(self, data):
        cat_col = data.select_dtypes(include='object').columns
        num_col = data.select_dtypes(include=['int', 'float']).columns
        if cat_col:
            for col in cat_col:
                data[col] = data[col].fillna('Missing')
        if num_col:
            for col in num_col:
                data[col] = data[col].fillna(data[col].mean())
        return data

    def EncodeAndScale_fit(self, data):
        cat_col = data.select_dtypes(include='object').columns
        num_col = data.select_dtypes(include=['int', 'float']).columns
        if cat_col:
            for col in cat_col:
                encoder = LabelEncoder()
                data[col] = encoder.fit_transform(data[col])
                self.le[col] = encoder
        if num_col:
            data[num_col] = self.ss.fit_transform(data[num_col])
        return data

    def EncodeAndScale_transform(self, data):
        cat_col = data.select_dtypes(include='object').columns
        num_col = data.select_dtypes(include=['int', 'float']).columns
        if cat_col:
            for col in cat_col:
                data[col] = self.le[col].transform(data[col])
        if num_col:
            data[num_col] = self.ss.transform(data[num_col])
        return data