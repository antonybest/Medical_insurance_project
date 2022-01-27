medical_data = \
"""Marina Allison   ,27   ,   31.1 , 
#7010.0   ;Markus Valdez   ,   30, 
22.4,   #4050.0 ;Connie Ballard ,43 
,   25.3 , #12060.0 ;Darnell Weber   
,   35   , 20.6   , #7500.0;
Sylvie Charles   ,22, 22.1 
,#3022.0   ;   Vinay Padilla,24,   
26.9 ,#4620.0 ;Meredith Santiago, 51   , 
29.3 ,#16330.0;   Andre Mccarty, 
19,22.7 , #2900.0 ; 
Lorena Hodson ,65, 33.1 , #19370.0; 
Isaac Vu ,34, 24.8,   #7045.0"""


print("Original medical data")
print("-" * 30)
print(medical_data)
print("-" * 30)


updated_medical_data = medical_data.replace("#", "$")
print("\nUpdated medical data")
print("-" * 30)
print(updated_medical_data)
print("-" * 30)

# Number of medical records
num_records = 0
for record in updated_medical_data:
  if record == "$":
    num_records += 1
# -------------------------------
# another way of counting the medical records
# split_medical_data = updated_medical_data.split(";")
# for record in split_medical_data:
  # num_records += 1
# -------------------------------
print("-" * 30)
print(f"There are {num_records} medical records in the data.")
print("-" * 30)


medical_data_split = updated_medical_data.split(";")
print("\nSeparated medical data")
print("-" * 30)
print(medical_data_split)
print("-" * 30)


medical_records = []
for data in medical_data_split:
  split_data = data.split(",")
  medical_records.append(split_data)

print("\nSeparated medical data appended to medical_records list")
print("-" * 30)
print(medical_records)
print("-" * 30)


medical_records_clean = []
for record in medical_records:
  record_clean = []
  for item in record:
    record_clean.append(item.strip())
  medical_records_clean.append(record_clean)

print("\nCleaned medical records")
print("-" * 30)
print(medical_records_clean)
print("-" * 30)


print("\nNames of each medical patient")
print("-" * 30)
for record in medical_records_clean:
  record = record[0].upper()
  print(record)
print("-" * 30)


names = []
ages = []
bmis = []
insurance_costs = []

for record in medical_records_clean:
  names.append(record[0].upper())
  ages.append(record[1])
  bmis.append(record[2])
  insurance_costs.append(record[3])

print("\nNames")
print(names)
print("\nAges")
print(ages)
print("\nBMIs")
print(bmis)
print("\nInsuance Costs")
print(insurance_costs)


total_bmi = 0
for bmi in bmis:
  total_bmi += float(bmi)

average_bmi = total_bmi / len(bmis)

print("\nAVERAGE BMI")
print("-" * 30)
print(f"The average BMI is {round(average_bmi, 2)}")
print("-" * 30)


average_insurance_costs_list = []
for insurance in insurance_costs:
  average_insurance_costs_list.append(insurance[1:])

print("\nInsurance cost without '$' for calculation purposes")
print("-" * 30)
print(average_insurance_costs_list)
print("-" * 30)

total_insurance_cost = 0
for insurance in average_insurance_costs_list:
  total_insurance_cost += float(insurance)
average_insurance_cost = total_insurance_cost / len(average_insurance_costs_list)
print("\nAVERAGE INSURANCE COST")
print("-" * 30)
print(f"The average insurance cost is {round(average_insurance_cost, 2)}")
print("-" * 30)


print("\n CUSTOMERS DETAILS")
for i in range(0,len(names)):
  name = names[i]
  age = ages[i]
  bmi = bmis[i]
  insurnace = insurance_costs[i]
  print("-" * 30)
  print(f"{name} is {age} years old with a BMI of {bmi} and an insurance cost of {insurance}")
  print("-" * 30)

# -------- END OF FILE --------------