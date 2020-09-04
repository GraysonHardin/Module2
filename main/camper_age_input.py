def main():
    age_in_years = int(input("Enter age in years: "))
    age_in_months = convert_to_months(age_in_years)
    print(f'The age in months is {age_in_months}')

    age_in_months = int(input("Enter age in months: "))
    age_in_years = convert_to_years(age_in_months)
    print(f'The age in years is {age_in_years}')


def convert_to_months(age_in_years):
    age_in_months = age_in_years * 12
    return age_in_months


def convert_to_years(age_in_months):
    age_in_years = age_in_months / 12
    return age_in_years


if __name__ == '__main__':
    main()
