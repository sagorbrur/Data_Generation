# dependency 
# pip install pydbgen


from pydbgen import pydbgen
import pandas as pd
generator = pydbgen.pydb()

# Generate a license-plate (US style)
print(generator.license_plate())

# Generate few random names
print(generator.gen_data_series(num=10,data_type='name'))

# Generate random phone numbers
print(generator.simple_ph_num())
print(generator.gen_data_series(num=10,data_type='phone_number_full'))

# Generate a full data frame with random name, street address, SSN, date
df = generator.gen_dataframe(fields=['name','street_address','ssn','date'])
print(df)

df_pd = pd.DataFrame(df)
export_csv = df_pd.to_csv('export_dataframe.csv', index = None, header=True)
print('done!')
