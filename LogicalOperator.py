from operator import truediv


high_income = False
good_credit = True
student = True


if high_income and good_credit:
    print("eligible")
else:
    print("not eligible")


if high_income or good_credit:
    print("eligible")
else:
    print("not eligible")


if not student:
    print("eligible")
else:
    print("not eligible")


    if (high_income or good_credit) and not student:
        print("eligible")
    else:
        print("not eligible")
