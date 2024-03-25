# Read from BKPF data and generate BSEG, BSEC, BSET
import pandas as pd
from faker import Faker
import random
fake = Faker()
customerNo_df = pd.read_csv('customerNo_data.csv')
companyCodeList = pd.read_csv('companycode_data.csv')
companyCodeList = companyCodeList['CompanyCode']

knb1 = pd.concat([customerNo_df, companyCodeList], axis=1)

knb1.to_csv('KNB1_data.csv', index=False)
print(knb1)


def generate_segment_data_knb5(df, table_name):
    table_name = {
        'CustomerNo': [],
        'CompanyCode': [],
        'DunningArea': [],
    }
    for _, row in df.iterrows():

        numbers_list = [1, 2]
        # Use random.choice() to select a random integer from the list
        num_records_per_lbf5 = random.choice(numbers_list)
        for _ in range(num_records_per_lbf5) :
            table_name['CustomerNo'].append(row['CustomerNo'])
            table_name['CompanyCode'].append(row['CompanyCode'])
            table_name['DunningArea'].append(fake.bothify(text='???'))
    table_df = pd.DataFrame(table_name)
    # segment_df.head(10000).to_csv(f"{table_name}_data.csv", index=False)
    return table_df

# # Generate data for LBF5
knb5_data = generate_segment_data_knb5(knb1, 'KNB5')
knb5_data = knb5_data.drop_duplicates()
knb5_data.to_csv('KNB5_data.csv', index=False)
print(knb5_data)
