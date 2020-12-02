# Gabriel Daniels
# PSID 1856516


def get_age():
    age_ = int(input())
    if age_ > 75 or age_ < 18:
        raise ValueError('Invalid age.')
    return age_


def fat_burning_heart_rate(age):
    heartbeat = .7 * (220 - age)
    return heartbeat


if __name__ == "__main__":
    try:
        age = get_age()
        hr = fat_burning_heart_rate(age)
        print('Fat burning heart rate for a', age, 'year-old:', hr, 'bpm')
    except ValueError as excpt:
        print(excpt)
        print('Could not calculate heart rate info.\n')

