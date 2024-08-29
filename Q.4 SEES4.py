Total_purchase=float(input('please enter your total purchase amount: '))
years_of_membership=int(input('how many years have you been a member of the bookstore: '))
number_of_complaints=int(input('how many complaints have you filed in the past year: '))
number_of_past_year_purchases=int(input('how many purchases have you made this year: '))

if years_of_membership>10 :
    discount=0.10
elif years_of_membership>=6 and years_of_membership<=10:
    discount=0.08
elif years_of_membership<6:
    discount=0.05

complaint_adjustment=0.02*number_of_complaints
adjusted_discount=discount - complaint_adjustment

if adjusted_discount<0:
    discount=0

if number_of_past_year_purchases>20:
    bonus_discount=0.05
else:bonus_discount=0

net_discount= bonus_discount + adjusted_discount
new_total_purchase=Total_purchase*(1-net_discount)
print('net discount= ',f"${net_discount*Total_purchase:.2f}")
print('new_total_purchase=$',new_total_purchase)
 







