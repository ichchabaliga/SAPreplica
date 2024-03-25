# Read from BKPF data and generate BSEG, BSEC, BSET
import pandas as pd
from faker import Faker
import random
fake = Faker()
bseg_df = pd.read_csv('BSEG_data.csv')
companycode_df = pd.read_csv('companycode_data.csv')
fiscalyear_df = pd.read_csv('fiscalyear_data.csv')
customerNo_df = pd.read_csv('customerNo_data.csv')
vendorNo_df = pd.read_csv('vendorNo_data.csv')
customerNo = customerNo_df['CustomerNo']
vendorNo = vendorNo_df['VendorNo']
companycode = companycode_df['CompanyCode']
fiscalyear = fiscalyear_df['FiscalYear']
def generate_segment_data_BSEG(df, table_name, additional_columns=None):
    print("generating{} data".format(table_name))
    segment_data = {
        'CompanyCode': [],
        'DocumentNo': [],
        'FiscalYear': [],
        'LineItem': [],
    }
    for _, row in df.iterrows():
           segment_data['CompanyCode'].append(row['CompanyCode'])
           segment_data['DocumentNo'].append(row['DocumentNo'])
           segment_data['FiscalYear'].append(row['FiscalYear'])
           segment_data['LineItem'].append(row['LineItem'])
           for column, func in additional_columns.items():
               X= func()
               print(X)
               if column not in segment_data:
                    segment_data[column]=[]
               segment_data[column].append(X)

    segment_df = pd.DataFrame(segment_data)
    # segment_df.head(10000).to_csv(f"{table_name}_data.csv", index=False)
    return segment_df


Additional_columns_Customer = {"SpecialGLInd": lambda: fake.bothify(text='#??#'),
                    "SpecialGLTrans": lambda: fake.bothify(text='##??'),
                    "CustomerNo": lambda: random.choice(customerNo),
                    "ClearingDoc": lambda: fake.bothify(text='####?????#'),
                    "ClearingDate": lambda: fake.date(pattern='%Y-%m-%d', end_datetime=None),
                    "AllocationNo": lambda: fake.bothify(text='####?????#')}
bsad_data=generate_segment_data_BSEG(bseg_df, 'BSAD', additional_columns=Additional_columns_Customer)
bsid_data=generate_segment_data_BSEG(bseg_df, 'BSID', additional_columns=Additional_columns_Customer)

Additional_columns_Vendor = {"SpecialGLInd": lambda: fake.bothify(text='#??#'),
                    "SpecialGLTrans": lambda: fake.bothify(text='##??'),
                    "Vendor": lambda: random.choice(vendorNo),
                    "ClearingDoc": lambda: fake.bothify(text='####?????#'),
                    "ClearingDate": lambda: fake.date(pattern='%Y-%m-%d', end_datetime=None),
                    "AllocationNo": lambda: fake.bothify(text='####?????#')}
bsik_data=generate_segment_data_BSEG(bseg_df, 'BSIK', additional_columns=Additional_columns_Vendor)
bsak_data=generate_segment_data_BSEG(bseg_df, 'BSAK', additional_columns=Additional_columns_Vendor)

Additional_columns_GL = {"GLAccount": lambda: fake.bothify(text='#??#'),
                         "ClearingDoc": lambda: fake.bothify(text='####?????#'),
                        "ClearingDate": lambda: fake.date(pattern='%Y-%m-%d', end_datetime=None),
                        "AllocationNo": lambda: fake.bothify(text='####?????#')}
bsis_data=generate_segment_data_BSEG(bseg_df, 'BSIS', additional_columns=Additional_columns_GL)
bsas_data=generate_segment_data_BSEG(bseg_df, 'BSAS', additional_columns=Additional_columns_GL)

bsad_data=bsad_data.drop_duplicates()
bsid_data=bsid_data.drop_duplicates()
bsik_data=bsik_data.drop_duplicates()
bsas_data=bsas_data.drop_duplicates()
bsis_data=bsis_data.drop_duplicates()
bsak_data=bsak_data.drop_duplicates()

bsad_data.to_csv('BSAD_data.csv', index=False)
bsid_data.to_csv('BSID_data.csv', index=False)
bsik_data.to_csv('BSIK_data.csv', index=False)
bsas_data.to_csv('BSAS_data.csv', index=False)
bsis_data.to_csv('BSIS_data.csv', index=False)
bsak_data.to_csv('BSAK_data.csv', index=False)
#
#
#
# # Export BKPF data to CSV
#
