# --------------
# Importing header files
import numpy as np
import pandas as pd
from scipy.stats import mode 
 
import warnings
warnings.filterwarnings('ignore')


#Reading file
bank_data = pd.read_csv(path)


#Code starts here
bank = pd.DataFrame(bank_data)
categorical_var = bank.select_dtypes(include = 'object')
#print(categorical_var)

numerical_var = bank.select_dtypes(include = 'number')
#print(numerical_var)


banks = bank.drop(columns='Loan_ID')
#print(banks)
print("Sum of Null values")
print(banks.isnull().sum())

bank_mode = banks.mode()
print("bank mode")
print(bank_mode)


banks.fillna(bank_mode, inplace=True)
print(banks.shape)
print(banks.isnull().sum().values.sum())


avg_loan_amount = pd.pivot_table(banks,index = ['Gender', 'Married', 'Self_Employed'], values = ['LoanAmount'],aggfunc = np.mean)

print(avg_loan_amount['LoanAmount'][1],2)

loan_approved_se = banks.loc[(banks["Self_Employed"]=="Yes")  & (banks["Loan_Status"]=="Y"), ["Loan_Status"]].count()
print(loan_approved_se)


loan_approved_nse = banks.loc[(banks["Self_Employed"]=="No")  & (banks["Loan_Status"]=="Y"), ["Loan_Status"]].count()
print(loan_approved_nse)


percentage_se = (loan_approved_se/614)*100
percentage_nse = (loan_approved_nse/614)*100
print("percentage_se")
print("%.2f"%percentage_se)
print("percentage_nse")
print("%.2f"%percentage_nse)

loan_term = banks['Loan_Amount_Term'].apply(lambda x: x/12 )
big_loan_term = len(loan_term[loan_term >= 25])
print("big_loan_term")
print(big_loan_term)


loan_groupby = banks.groupby(["Loan_Status"])
loan_groupby = loan_groupby['ApplicantIncome', 'Credit_History']
mean_values = loan_groupby.mean()



