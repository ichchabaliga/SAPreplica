### PAYR data generation
import pandas as pd
from faker import Faker
import random
import pycountry
fake = Faker()

payr_data = {"PayingCompany": [], "HouseBank": [], "Account": [], "PaymentMethod": [], "CheckNo":[]}
payment_method = ['Check','Wire Transfer','Cash']
for _ in range(10000):
    import random
    payr_data['PayingCompany'].append(fake.bothify(text='????'))
    payr_data['HouseBank'].append(fake.bothify(text='?????'))
    payr_data['Account'].append(fake.bothify(text='#########'))
    payr_data['PaymentMethod'].append(random.choice(payment_method))
    payr_data['CheckNo'].append(fake.bothify(text='#######'))
payr_df = pd.DataFrame(payr_data)
payr_df = payr_df.drop_duplicates()
payr_df.to_csv('PAYR_data.csv', index=False)
#print(payr_df)