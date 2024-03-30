# test.py: Unit Testing and Deployment

import unittest
from model import LinearRegressionModel


class TestLinearRegressionModel(unittest.TestCase):
    def setUp(self):
        self.model = LinearRegressionModel()
        self.X_train = [[39], [40], [41], [42], [43]]
        self.y_train = [13.17, 11.88, 18.82, 18.65, 17.02]

    def test_model_fit(self):
        self.model.fit(self.X_train, self.y_train)
        self.assertIsNotNone(self.model.model)
        self.assertEqual(len(self.model.model.coef_), 1) 

    def test_model_prediction_range(self):
        self.model.fit(self.X_train, self.y_train)
        X_test = [[39], [40], [41], [42], [43], [44], [45]]  
        predicted_profits = self.model.predict(X_test)
        self.assertEqual(len(predicted_profits), len(X_test))  

    def test_model_invalid_input(self):
        with self.assertRaises(ValueError):
            self.model.predict([[50]]) 


if __name__ == '__main__':
    unittest.main()
