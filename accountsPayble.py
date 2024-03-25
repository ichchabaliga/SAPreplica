# Read from BKPF data and generate BSEG, BSEC, BSET
import pandas as pd
from faker import Faker
import random
import pycountry

fake = Faker()
vendor_df = pd.read_csv('vendorNo_data.csv')
company_code = pd.read_csv('companycode_data.csv')
lfb1 = pd.concat([vendor_df, company_code], axis=1)

lfb1.to_csv('LFB1_data.csv', index=False)
print(lfb1)
### Making lfb5 here

def lfb5_data_gen(df, table_name):
    table_name = {
        'VendorNo': [],
        'CompanyCode': [],
        'DunningArea': [],
    }
    for _, row in df.iterrows():

        numbers_list = [1, 2]
        # Use random.choice() to select a random integer from the list
        num_records_per_lbf5 = random.choice(numbers_list)
        for _ in range(num_records_per_lbf5) :
            table_name['VendorNo'].append(row['VendorNo'])
            table_name['CompanyCode'].append(row['CompanyCode'])
            table_name['DunningArea'].append(fake.bothify(text='???'))
    table_df = pd.DataFrame(table_name)
    # segment_df.head(10000).to_csv(f"{table_name}_data.csv", index=False)
    return table_df

# # Generate data for LBF5
lfb5_data = lfb5_data_gen(lfb1, 'LBF5')
lfb5_data = lfb5_data.drop_duplicates()
lfb5_data.to_csv('LFB5_data.csv', index=False)
print(lfb5_data)

def lfbk_data_gen(df, table_name):
    ### getting the country names codes here
    country_names_3_letters = [country.alpha_3 for country in pycountry.countries]

    table_name = {
        'VendorNo': [],
        'BankCountry': [],
        'BankKey': [],
        'BankAcc': [],
    }
    for _, row in df.iterrows():

        numbers_list = [1, 2]
        # Use random.choice() to select a random integer from the list
        num_records_per_lbf5 = random.choice(numbers_list)
        for _ in range(num_records_per_lbf5) :
            table_name['VendorNo'].append(row['VendorNo'])
            table_name['BankCountry'].append(random.choice(country_names_3_letters))
            table_name['BankKey'].append(fake.bothify(text='######'))
            table_name['BankAcc'].append(fake.bothify(text='########'))
    table_df = pd.DataFrame(table_name)
    # segment_df.head(10000).to_csv(f"{table_name}_data.csv", index=False)
    return table_df

# # Generate data for LBFK
lfbk_data=lfbk_data_gen(vendor_df, 'lfbk')
lfbk_data = lfbk_data.drop_duplicates()
lfbk_data.to_csv('LFBK_data.csv', index=False)
#print(lfbk_data)

def lfm1_data_gen(df, table_name):
    table_name = {
        'VendorNo': [],
        'PurchOrg': [],
    }
    for _, row in df.iterrows():

        numbers_list = [1, 2]
        # Use random.choice() to select a random integer from the list
        num_records_per_lbf5 = random.choice(numbers_list)
        for _ in range(num_records_per_lbf5) :
            table_name['VendorNo'].append(row['VendorNo'])
            table_name['PurchOrg'].append(fake.bothify(text='????'))
    table_df = pd.DataFrame(table_name)
    # segment_df.head(10000).to_csv(f"{table_name}_data.csv", index=False)
    return table_df

# # Generate data for LBF5
lfm1_df=lfm1_data_gen(vendor_df, 'lfm1')
lfm1_df= lfm1_df.drop_duplicates()
lfm1_df.to_csv('LFM1_data.csv', index=False)
#print(lfm1_data)


def lfm2_data_gen(df, table_name):
    table_name = {
        'VendorNo': [],
        'PurchOrg': [],
        'SubRange': [],
        'Plant': [],
    }
    for _, row in df.iterrows():

        numbers_list = [1, 2]
        # Use random.choice() to select a random integer from the list
        num_records_per_lbf5 = random.choice(numbers_list)
        for _ in range(num_records_per_lbf5) :
            table_name['VendorNo'].append(row['VendorNo'])
            table_name['PurchOrg'].append(row['PurchOrg'])
            table_name['SubRange'].append(fake.bothify(text='??????'))
            table_name['Plant'].append(fake.bothify(text='????'))
    table_df = pd.DataFrame(table_name)
    # segment_df.head(10000).to_csv(f"{table_name}_data.csv", index=False)
    return table_df

# # Generate data for LBF5
lfm2_df=lfm2_data_gen(lfm1_df, 'lfm2')
lfm2_df = lfm2_df.drop_duplicates()
lfm2_df.to_csv('LFM2_data.csv', index=False)
#print(lfm2_df)



