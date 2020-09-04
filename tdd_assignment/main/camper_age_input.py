"""
Program: camper_age_input.py
Author: Grayson Hardin
Last date modified: 9/3/2020


This program will take the age of (1-5) and convert it to months.
Additionally, the program will accept months (12-60) to years.
I felt the assignment was not made clear enough, so I thought it would be best to cover both of my bases. I hope you enjoy.

"""


def main():
    # Here, we gain user input for years.
    age_in_years = int(input("Enter age in years: "))
    age_in_months = convert_to_months(age_in_years)
    print(f'The age in months is {age_in_months}')
    # Likewise, we gain the input for months.
    age_in_months = int(input("Enter age in months: "))
    age_in_years = convert_to_years(age_in_months)
    print(f'The age in years is {age_in_years}')


# The function below is where we perform the calculations for years to months.
def convert_to_months(age_in_years):
    age_in_months = age_in_years * 12
    return age_in_months


# This function takes months and does the math to convert the input to months.
def convert_to_years(age_in_months):
    age_in_years = age_in_months / 12
    return age_in_years


if __name__ == '__main__':
    main()
