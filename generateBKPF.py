# This script generates fake data for the BKPF, BSEG, BSEC, BSET, and BSIP tables
import pandas as pd
from faker import Faker

fake = Faker()

# Determine how many records you want in each table
num_records_bvor = 10000
num_records_per_bvor = 3  # How many BSEG, BSEC, and BSET records per one BKPF record
interdata= [fake.random_int() for _ in range(num_records_bvor)]

print(len(interdata))

companycodes = pd.read_csv('companycode_data.csv')
companycodelist = companycodes['CompanyCode']
fiscalyears = pd.read_csv('fiscalyear_data.csv')
fiscalyearlist = fiscalyears['FiscalYear']

bvor_data = {"IntercompanyNo": [], "CompanyCode": [], "FiscalYear": [], "DocumentNo": []}
for _ in range(len(interdata)):
    import random
    numbers_list = [1,2,3]
    # Use random.choice() to select a random integer from the list
    num_records_per_bkpf = random.choice(numbers_list)
    for i in range(num_records_per_bkpf) :
        bvor_data['IntercompanyNo'].append(interdata[_])
        bvor_data['CompanyCode'].append(random.choice(companycodelist))
        bvor_data['FiscalYear'].append(random.choice(fiscalyearlist))
        bvor_data['DocumentNo'].append(fake.bothify(text='##########'))

# Generate BKPF data
bvor_df = pd.DataFrame(bvor_data)
print(bvor_df)
bkpf_data = bvor_df[['CompanyCode', 'FiscalYear', 'DocumentNo']]
print(bkpf_data)

bkpf_df = pd.DataFrame(bkpf_data)
bkpf_df=bkpf_df.drop_duplicates()
bvor_df=bvor_df.drop_duplicates()


bkpf_df.to_csv('BKPF_data.csv', index=False)
bvor_df.to_csv('BVOR_data.csv', index=False)
# Generate BSEG, BSEC, and BSET data
#
