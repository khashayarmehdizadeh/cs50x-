def main():
    dollars = dollars_to_float(input("Hom much was the meal?"))
    percent = percent_to_float(input("what percentage would you like to tip?"))
    tip = dollars * percent
    print(f"leave${tip:.2f}")


def dollars_to_float(d):
    d = d.strip('$')
    d = float(d)
    return (d)


def percent_to_float(p):
    p = p.strip('%')
    p = (float(p)) / 100
    return (p)


main()
