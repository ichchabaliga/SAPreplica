import pandas as pd
from faker import Faker
import random
fake = Faker()
customerNo = pd.read_csv('customerNo_data.csv')
customerNoList = customerNo['CustomerNo']
def generate_segment_data_KNVV():
    print("generating{} data".format('KNC1'))
    segment_data = {
        'CustomerNo': [],
        'SalesOrg': [],
        'DistributionCh': [],
        'Division': [],
    }
    for row in customerNoList:
        segment_data['CustomerNo'].append(row)
        segment_data['SalesOrg'].append(fake.random_int())
        segment_data['DistributionCh'].append(fake.random_int())
        segment_data['Division'].append(fake.random_int())

    segment_df = pd.DataFrame(segment_data)
    # segment_df.head(10000).to_csv(f"{table_name}_data.csv", index=False)
    return segment_df

segment_df = generate_segment_data_KNVV()
segment_df.to_csv('KNVV_data.csv', index=False)