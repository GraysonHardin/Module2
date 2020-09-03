def main():
    age_in_years = int(input("Hi: "))
    age_in_months = convert_to_months(age_in_years)
    print(f'The age in months is {age_in_months}')



def convert_to_months(age_in_years):
    age_in_months = age_in_years * 12
    return age_in_months

def convert_to_years(age_in_months):
    return age_in_months / 12



if __name__ == '__main__':
    main()
