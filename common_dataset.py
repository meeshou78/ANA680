from ucimlrepo import fetch_ucirepo
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder

def load_and_prepare_data():
    data = fetch_ucirepo(id=15)  # Breast Cancer Wisconsin (Original) Data Set
    df = data.data.original.copy()

    df.replace('?', pd.NA, inplace=True)
    df.dropna(inplace=True)
    df = df.astype({
        'Bare_nuclei': 'int32',
        'Clump_thickness': 'int32',
        'Uniformity_of_cell_size': 'int32',
        'Uniformity_of_cell_shape': 'int32',
        'Marginal_adhesion': 'int32',
        'Single_epithelial_cell_size': 'int32',
        'Bland_chromatin': 'int32',
        'Normal_nucleoli': 'int32',
        'Mitoses': 'int32',
        'Class': 'int32'
    })

    X = df.drop(columns=['Sample_code_number', 'Class'])
    y = df['Class'].replace({2: 0, 4: 1})  # Convert class to binary: 0 = benign, 1 = malignant

    return train_test_split(X, y, test_size=0.25, random_state=42)
