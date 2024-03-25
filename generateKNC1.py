import pandas as pd
from faker import Faker
import random
fake = Faker()
companycodes = pd.read_csv('companycode_data.csv')
companycodelist = companycodes['CompanyCode']
fiscalyears = pd.read_csv('fiscalyear_data.csv')
fiscalyearlist = fiscalyears['FiscalYear']
customerNo_df = pd.read_csv('customerNo_data.csv')
customerNo = customerNo_df['CustomerNo']
vendorNo_df = pd.read_csv('vendorNo_data.csv')
vendorNo = vendorNo_df['VendorNo']
def generate_segment_data_KNC1():
    print("generating{} data".format('KNC1'))
    segment_data = {
        'CustomerNo': [],
        'CompanyCode': [],
        'FiscalYear': [],
    }
    for row in range(10000):
        segment_data['CustomerNo'].append(random.choice(customerNo))
        segment_data['CompanyCode'].append(random.choice(companycodelist))
        segment_data['FiscalYear'].append(random.choice(fiscalyearlist))

    segment_df = pd.DataFrame(segment_data)
    # segment_df.head(10000).to_csv(f"{table_name}_data.csv", index=False)
    return segment_df

def generate_segment_data_LFC1():
    print("generating{} data".format('LFC1'))
    segment_data = {
        'VendorNo': [],
        'CompanyCode': [],
        'FiscalYear': [],
    }
    for row in range(10000):
        segment_data['VendorNo'].append(random.choice(vendorNo))
        segment_data['CompanyCode'].append(random.choice(companycodelist))
        segment_data['FiscalYear'].append(random.choice(fiscalyearlist))

    segment_df = pd.DataFrame(segment_data)
    # segment_df.head(10000).to_csv(f"{table_name}_data.csv", index=False)
    return segment_df

segment_df = generate_segment_data_KNC1()
segment_df.to_csv('KNC1_data.csv', index=False)
segment_df2 = generate_segment_data_LFC1()
segment_df2.to_csv('LFC1_data.csv', index=False)