# generate customerNo, vendorNo, companycode and fiscal year data
import pandas as pd
from faker import Faker
fake = Faker()
customerNo = [fake.bothify(text='#####') for _ in range(150050)]
vendorNo = [fake.bothify(text='#####') for _ in range(150050)]
companycode = [fake.bothify(text='#####') for _ in range(150050)]
fiscalyear = [fake.year() for _ in range(150050)]
customerNo_df = pd.DataFrame({"CustomerNo": customerNo})
vendorNo_df = pd.DataFrame({"VendorNo": vendorNo})
companycode_df = pd.DataFrame({"CompanyCode": companycode})
fiscalyear_df = pd.DataFrame({"FiscalYear": fiscalyear})


# remone duplicates
customerNo_df=customerNo_df.drop_duplicates()
vendorNo_df=vendorNo_df.drop_duplicates()
companycode_df=companycode_df.drop_duplicates()
fiscalyear_df=fiscalyear_df.drop_duplicates()
# save the data to csv

customerNo_df.head(10000).to_csv('customerNo_data.csv', index=False)
customerNo_df.head(10000).to_csv('KNA1_data.csv', index=False)
vendorNo_df.head(10000).to_csv('vendorNo_data.csv', index=False)
vendorNo_df.head(10000).to_csv('LFA1_data.csv', index=False)
companycode_df.head(10000).to_csv('companycode_data.csv', index=False)
fiscalyear_df.head(10000).to_csv('fiscalyear_data.csv', index=False)
