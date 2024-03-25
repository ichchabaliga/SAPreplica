import pandas as pd
from faker import Faker
import random
fake = Faker()
customerNo = pd.read_csv('customerNo_data.csv')
customerNoList = customerNo['CustomerNo']
knvv_df = pd.read_csv('KNVV_data.csv')
def generate_segment_data_KNVV(df,table_name,additional_column=None):

    print("generating{} data".format(table_name))
    segment_data = {
        'CustomerNo': [],
        'SalesOrg': [],
        'DistributionCh': [],
        'Division': [],
    }
    for _, row in df.iterrows():

        numbers_list = [1, 2, 3]
        # Use random.choice() to select a random integer from the list
        num_records_per_bkpf = random.choice(numbers_list)
        for i in range(num_records_per_bkpf):

            segment_data['CustomerNo'].append(row['CustomerNo'])
            segment_data['SalesOrg'].append(row['SalesOrg'])
            segment_data['DistributionCh'].append(row['DistributionCh'])
            segment_data['Division'].append(row['Division'])
            for column, func in additional_column.items():
                X = func()
                print(X)
                if column not in segment_data:
                    segment_data[column] = []
                segment_data[column].append(X)

    segment_df = pd.DataFrame(segment_data)
    # segment_df.head(10000).to_csv(f"{table_name}_data.csv", index=False)
    return segment_df
additional_column_knvp = {'PartnerFunction': lambda: fake.bothify(text='?????'),
'PartnerCounter': lambda: fake.random_int()}
additional_column_knvd = {'OutputType': lambda: fake.bothify(text='?????'), "MessLanguage": lambda: fake.bothify(text='?????')}
segment_df = generate_segment_data_KNVV(knvv_df,'KNVP',additional_column=additional_column_knvp)
segment_df2 = generate_segment_data_KNVV(knvv_df,'KNVD',additional_column=additional_column_knvd)
segment_df.to_csv('KNVP_data.csv', index=False)
segment_df2.to_csv('KNVD_data.csv', index=False)