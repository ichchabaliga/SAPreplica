# Read from BKPF data and generate BSEG, BSEC, BSET
import pandas as pd
from faker import Faker
import random
fake = Faker()
bkpf_df = pd.read_csv('BKPF_data.csv')

def generate_segment_data_BKFP(df, table_name, additional_columns=None, refin=None):
    print("generating{} data".format(table_name))
    segment_data = {
        'CompanyCode': [],
        'DocumentNo': [],
        'FiscalYear': [],
        'LineItem': [],
    }
    for _, row in df.iterrows():

                numbers_list = [1, 2, 3]
                # Use random.choice() to select a random integer from the list
                num_records_per_bkpf = random.choice(numbers_list)
                for _ in range(num_records_per_bkpf) :
                    segment_data['CompanyCode'].append(row['CompanyCode'])
                    segment_data['DocumentNo'].append(row['DocumentNo'])
                    segment_data['FiscalYear'].append(row['FiscalYear'])
                    segment_data['LineItem'].append(fake.random_int(min=1, max=999))
    segment_df = pd.DataFrame(segment_data)
    # segment_df.head(10000).to_csv(f"{table_name}_data.csv", index=False)
    return segment_df

# # Generate data for BSEG, BSEC, and BSET
bseg_data=generate_segment_data_BKFP(bkpf_df, 'BSEG')
bsec_data=generate_segment_data_BKFP(bkpf_df, 'BSEC')
bset_data=generate_segment_data_BKFP(bkpf_df, 'BSET')
# bsip_data=generate_segment_data_BKFP(bkpf_df, 'BSIP',  refin="one-to-one", additional_columns=Additional_columns_BSIP)
# # Generate data for bsip
# print(bsip_data)
#
# bsip_data.to_csv('BSIP_data.csv', index=False)
bsec_data=bsec_data.drop_duplicates()
bseg_data=bseg_data.drop_duplicates()
bset_data=bset_data.drop_duplicates()

bseg_data.to_csv('BSEG_data.csv', index=False)
bsec_data.to_csv('BSEC_data.csv', index=False)
bset_data.to_csv('BSET_data.csv', index=False)

#
# print("Data generated successfully")
#
#
#