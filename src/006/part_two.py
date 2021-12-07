import common

"""
Brute-force was "fine" for part 1 but for part 2 this will be painfully slow :)
I guess we have to start being a bit careful with what we are implementing from now onwards ;)
"""

TOTAL_DAYS = 256

if __name__ == "__main__":
    for input_file in common.inputs:
        lanternfishes = []

        for line in common.read_file(input_file):
            lanternfishes = line.split(",")
        lanternfishes = [int(reset) for reset in lanternfishes]

        # how many will be generated on each day
        days_old = [0] * 9
        # each fish will generate another one after "reset" days
        for reset in lanternfishes:
            days_old[reset] += 1

        # for each day that passes...
        for day in range(TOTAL_DAYS):
            # on day "day+7" we will generate "day" new fishes
            on_day = day + 7
            # just make sure we get the rest of the division by (max_reset_days + 1)
            days_old[on_day % 9] += days_old[day % 9]

        print(sum(days_old))
