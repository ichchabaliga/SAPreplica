import pandas as pd
from faker import Faker
import random

fake = Faker()
bkpf_df = pd.read_csv('BKPF_data.csv')

vendorNo_df = pd.read_csv('vendorNo_data.csv')
vendorNo = vendorNo_df['VendorNo']
def generate_segment_data_BSEG(df, table_name, additional_columns=None):
    print("generating{} data".format(table_name))
    segment_data = {
        'CompanyCode': [],
        'DocumentNo': [],
        'FiscalYear': [],

    }
    for _, row in df.iterrows():
           segment_data['CompanyCode'].append(row['CompanyCode'])
           segment_data['DocumentNo'].append(row['DocumentNo'])
           segment_data['FiscalYear'].append(row['FiscalYear'])
           for column, func in additional_columns.items():
               x = func()
               if column not in segment_data:
                    segment_data[column] = []

               segment_data[column].append(x)


    segment_df = pd.DataFrame(segment_data)
    # segment_df.head(10000).to_csv(f"{table_name}_data.csv", index=False)
    return segment_df
bsip_data = generate_segment_data_BSEG(bkpf_df, 'BSIP', additional_columns={"LineItem": lambda: fake.random_int(min=1, max=999),
                                                                            "Amount": lambda: fake.random_int(min=1, max=999),
                                                                            "Currency": lambda: fake.currency_code(),
                                                                            "DocumentDate": lambda: fake.date_this_century(),
                                                                            "Vendor": lambda: random.choice(vendorNo),
                                                                            "ReferenceDoc": lambda: fake.random_int(min=1, max=999)})

bsip_data.to_csv('BSIP_data.csv', index=False)


