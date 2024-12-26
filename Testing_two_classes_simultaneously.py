import unittest
from Testing_Classes import Car,Talaba
class Car_Talaba_Test(unittest.TestCase):
    def setUp(self):
        make='GM'
        model='Malibu'
        year='2020'
        ism='Javlonbek'
        familiya='Shukurov'
        tyil=2000
        
        self.avto1=Car(make, model, year)
        self.talaba1=Talaba(ism, familiya,tyil)
    def test_car_model_is_not_none(self):
        if isinstance(self.avto1,Car):
            self.assertIsNotNone(self.avto1.model)
        else:
            self.assertIsNone(self.talaba1.ism)
    def test_tanishtir(self):
        if isinstance(self.talaba1,Talaba):
            x="Ismim Javlonbek Shukurov. 2000 yilda tug'ilganman"
            self.assertEqual(x,self.talaba1.tanishtir())
unittest.main()            
