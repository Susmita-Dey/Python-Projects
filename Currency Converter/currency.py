def main():
    print("This program converts US dollars to Pounds Sterling\n")

    dollars = eval(input("Enter amount in dollars: "))

    pounds = convert_to_pounds(dollars)
    print("That is", pounds, "pounds.")


def convert_to_pounds(dollars): return dollars * 0.82


main()
