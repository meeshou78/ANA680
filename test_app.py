# File: test_app.py
import unittest
from app import app

class FlaskAppTestCase(unittest.TestCase):
    def setUp(self):
        self.app = app.test_client()
        self.app.testing = True

    def test_home_page_loads(self):
        response = self.app.get('/')
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'Breast Cancer Classifier', response.data)

    def test_prediction_route(self):
        response = self.app.post('/predict', data={
            "Clump_thickness": 5,
            "Uniformity_of_cell_size": 1,
            "Uniformity_of_cell_shape": 1,
            "Marginal_adhesion": 1,
            "Single_epithelial_cell_size": 2,
            "Bare_nuclei": 1,
            "Bland_chromatin": 3,
            "Normal_nucleoli": 1,
            "Mitoses": 1
        })
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'Cancer Prediction:', response.data)

if __name__ == '__main__':
    unittest.main()