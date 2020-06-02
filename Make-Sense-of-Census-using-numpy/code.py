# --------------
# Importing header files
import numpy as np
import warnings

warnings.filterwarnings('ignore')

#New record
new_record=[[50,  9,  4,  1,  0,  0, 40,  0]]

#Reading file
data = np.genfromtxt(path, delimiter=",", skip_header=1)
#Code starts here

print("\nData: \n\n", data)
print("\nType of data: \n\n", type(data))
#concatinating
census = np.concatenate([data, new_record])
print(np.shape(census))

#age
age = np.array([i[0] for i in census])
print("age \n",age)

#max age
max_age = np.max(age)
print("max age\n",max_age)
#min age
min_age = np.min(age)
print("min age\n",min_age)

#mean age
age_mean = sum(age)/len(age)
print("mean age:\n",age_mean)

#standard deviation
age_std = np.std(age)
print("standard deviation:\n",age_std)

#race 0
race_0 = np.array([i[2] for i in census if i[2]==0])

#race 1
race_1 = np.array([i[2] for i in census if i[2]==1])


#race 2
race_2 = np.array([i[2] for i in census if i[2]==2])


#race 3
race_3 = np.array([i[2] for i in census if i[2]==3])

#race 4
race_4 = np.array([i[2] for i in census if i[2]==4])


#length
len_0 = len(race_0)
len_1 = len(race_1)
len_2 = len(race_2)
len_3 = len(race_3)
len_4 = len(race_4)

#minority

minority_race = min(len_0,len_1,len_2,len_3,len_4)
print("minority race:\n",minority_race)

#senior_citizen
senior_citizen = np.array([i for i in census if i[0]>60], dtype = 'int32')

working_hours_sum = sum([i[6] for i in senior_citizen])
print("working hours:\n",working_hours_sum)

senior_citizen_len = len(senior_citizen)
print("senior_citizen_len:\n",senior_citizen_len)

avg_working_hours = working_hours_sum/senior_citizen_len
print("avg_working_hours:\n",avg_working_hours)

#jobs
high = np.array([i for i in census if i[1]>10])
low = np.array([i for i in census if i[1]<=10])


avg_pay_high = np.mean([i[7] for i in high])
print("avg_pay_high:\n",avg_pay_high)

avg_pay_low = np.mean([i[7] for i in low])
print("avg_pay_low:\n",avg_pay_low)






