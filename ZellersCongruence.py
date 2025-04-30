class DateCalculator:
    def __init__(self, year: int, month: int, day: int):
        # Adjust month and year if date is Jan or Feb
        if month == 1 or month == 2:
            month += 12
            year -= 1

        self.year = year
        self.month = month
        self.day = day

    def calculate_day_of_week(self) -> str:
        q = self.day
        m = self.month
        K = self.year % 100  # year of the century
        J = self.year // 100  # zero-based century

        # Zeller's Congruence Formula
        h = (q + (13 * (m + 1)) // 5 + K + K // 4 + J // 4 + 5 * J) % 7

        # Map Zeller’s output to weekdays
        days = ["Saturday", "Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday"]
        return days[h]


# === User Input Section ===
try:
    day = int(input("Enter day: "))
    month = int(input("Enter month (1-12): "))
    year = int(input("Enter year: "))

    date = DateCalculator(year, month, day)
    print(f"\nThe day of the week was: {date.calculate_day_of_week()}")

except ValueError:
    print("Please enter valid integers for day, month, and year.")