# ---- Functions ----

def check_age_validity():
    years = input("How old is the person you want to buy gift for: ")
    while not years.isdigit():
        years = input("Please enter valid age: ")

    if int(years) <= 0:
        check_age_validity()

    return int(years)


def check_age(years):
    print("Products: ")

    if 0 < years <= 3:
        print('\n'.join(one_to_three_years_old))
        return input("Choose present: ")

    elif 3 < years <= 6:
        print('\n'.join(four_to_six_years_old))
        return input("Choose present: ")

    elif 6 < years <= 10:
        print('\n'.join(seven_to_ten_years_old))
        return input("Choose present: ")

    elif 10 < years <= 12:
        print('\n'.join(eleven_and_twelve_years_old))
        return input("Choose present: ")

    elif 12 < years <= 17:
        print('\n'.join(thirteen_to_seventeen_years_old))
        return input("Choose present: ")

    elif years >= 18:
        print('\n'.join(eighteen_plus_years_old))
        return input("Choose present: ")


# --- Christmas gifts ---
one_to_three_years_old = {'toy car', 'milk bottle'} # fill with stock
four_to_six_years_old = {'lego', 'toy cars', 'doll', 'bicycle'} # fill with stock
seven_to_ten_years_old = {'bicycle', 'nerf', 'kids car', 'little kitchen'} # fill with stock
eleven_and_twelve_years_old = {'bicycle', 'chess', 'domino', 'jenga', 'rubik cube', 'console game', 'xbox', 'ps4'} # fill with stock
thirteen_to_seventeen_years_old = {'bicycle', 'xbox', 'ps4', 'ps5', 'console', 'computer', 'mobile', 'laptop', 'online game'} # fill with stock
eighteen_plus_years_old = {'car', 'motor', 'bicycle', 'weights', 'treadmill', 'clothes', 'cap'} # fill with stock

christmas_gifts = one_to_three_years_old | four_to_six_years_old | seven_to_ten_years_old | eleven_and_twelve_years_old | thirteen_to_seventeen_years_old | eighteen_plus_years_old

# --- Logic ---
years_old = check_age_validity()
chosen_present = check_age(years_old)

if chosen_present.lower() in christmas_gifts:
    print("Your gift is here!")
    open_gift = input('type "open" to open the gift: ')

    if open_gift.lower() == "open":
        print('******************************************')
        print(f'  {chosen_present}      {chosen_present}      {chosen_present}    ')
        print('******************************************')