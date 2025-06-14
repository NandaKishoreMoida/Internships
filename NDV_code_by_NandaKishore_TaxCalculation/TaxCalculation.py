def calculate_old_regime_tax(income):
    standard_deduction = 50000
    section_80c_deduction = 150000
    taxable_income = max(0, income - standard_deduction - section_80c_deduction)

    tax = 0
    if taxable_income <= 250000:
        tax = 0
    elif taxable_income <= 500000:
        tax = (taxable_income - 250000) * 0.05
    elif taxable_income <= 1000000:
        tax = (250000 * 0.05) + (taxable_income - 500000) * 0.2
    else:
        tax = (250000 * 0.05) + (500000 * 0.2) + (taxable_income - 1000000) * 0.3

    return round(tax, 2)


def calculate_new_regime_tax(income):
    tax = 0
    slabs = [
        (300000, 0),
        (300000, 0.05),
        (300000, 0.1),
        (300000, 0.15),
        (300000, 0.2),
        (float('inf'), 0.3)
    ]

    remaining_income = income
    for slab_limit, rate in slabs:
        if remaining_income <= 0:
            break
        slab_income = min(slab_limit, remaining_income)
        tax += slab_income * rate
        remaining_income -= slab_income

    return round(tax, 2)


def main():
    while True:
        print("\n=== Tax Deduction Calculator ===")
        try:
            ctc = float(input("Enter your CTC (in Rs.): "))
            bonus = float(input("Enter your Bonus (in Rs.): "))
        except ValueError:
            print("Invalid input! Please enter numbers only.")
            continue

        total_income = ctc + bonus
        print(f"\nTotal Income: Rs.{total_income:.2f}")

        old_tax = calculate_old_regime_tax(total_income)
        new_tax = calculate_new_regime_tax(total_income)

        print(f"\nOld Regime Tax Deduction: Rs.{old_tax}")
        print(f"New Regime Tax Deduction: Rs.{new_tax}")

        if old_tax < new_tax:
            print(f"You save Rs.{new_tax - old_tax} more using the Old Regime.")
        elif new_tax < old_tax:
            print(f"You save Rs.{old_tax - new_tax} more using the New Regime.")
        else:
            print("Both regimes result in the same tax.")

        choice = input("\nDo you want to recalculate? (y/n): ").lower()
        if choice != 'y':
            print("Thank you for using the Tax Calculator!")
            break


if __name__ == "__main__":
    main()
