import time
import pandas as pd
import numpy as np

CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }

def get_filters():
    """
    Asks user to specify a city, month, and day to analyze.

    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """
    print('Hello! Let\'s explore some US bikeshare data!')
    # get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs
    while True:
        city = input("Which city would you like to see data for? (chicago, new york city, or washington?)")
        city = city.lower()
        if city in CITY_DATA.keys():
            break
        else:
            print("invalid input! please enter one of these: (chicago, new york city, washington)")

    # get user input for month (all, january, february, ... , june)
    while True:
        month = input("Which month would you like to filter the data by? (january... june, or all)")
        month = month.lower()
        if month in ['january', 'february', 'march', 'april', 'may', 'june', 'all']:
            break
        else:
            print("invalid input! please enter one of these: ('january', 'february', 'march', 'april', 'may', 'june', 'all')")

    # get user input for day of week (all, monday, tuesday, ... sunday)
    while True:
        day = input("Which day would you like to filter the data by?  (monday...sunday, or all)")
        day = day.lower()
        if day in ['monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday', 'sunday', 'all']:
            break
        else:
            print("invalid input! please enter one of these: ('monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday', 'sunday', 'all')")


    print('-'*40)
    return city, month, day


def load_data(city, month, day):
    """
    Loads data for the specified city and filters by month and day if applicable.

    Args:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    Returns:
        df - Pandas DataFrame containing city data filtered by month and day
    """
    # load data file into a dataframe
    df = pd.read_csv(CITY_DATA[city])
    # convert the Start Time column to datetime
    df['Start Time'] = pd.to_datetime(df['Start Time'])
    # extract month to create a month column
    df['month'] = df['Start Time'].dt.month
    # extract day to create a day column
    df['day_of_week'] = df['Start Time'].dt.strftime("%A")
    # extract hour to create an hour column
    df['hour'] = df['Start Time'].dt.strftime("%H")

    # filter by month
    if month != 'all':
        months = ['january', 'february', 'march', 'april', 'may', 'june']
        month = months.index(month) + 1
        # create the new dataframe
        df = df[df['month'] == month]

    # filter by day of week
    if day != 'all':
        # create the new dataframe
        df = df[df['day_of_week'] == day.title()]
    return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # display the most common month
    print("The most common month: ", df['month'].mode()[0])

    # display the most common day of week
    print("The most common day of week: ", df['day_of_week'].mode()[0])

    # display the most common start hour
    print("The most common hour: ", df['hour'].mode()[0])

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # display most commonly used start station
    print("The most commonly used start station: ", df['Start Station'].mode()[0])

    # display most commonly used end station
    print("The most commonly used end station: ", df['End Station'].mode()[0])

    # display most frequent combination of start station and end station trip
    df['station'] = df['Start Station'] + " " + df['End Station']
    print("The most frequent combination of start station and end station trip: ", df['station'].mode()[0])

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # display total travel time
    print("Total travel time = ",df['Trip Duration'].sum())

    # display mean travel time
    print("Mean travel time = ", df['Trip Duration'].mean())

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df, city=None):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # Display counts of user types
    user_types = df['User Type'].value_counts()
    print("Counts of user types",user_types)

    # Display counts of gender
    if city != 'washington':
        gender = df['Gender'].value_counts()
        print("Counts of gender\n", gender)

    # Display earliest, most recent, and most common year of birth
    print("year of birth statistics")
    # earliest
    print('Earliest year of birth:', df['Birth Year'].min())
    # most recent
    print('Earliest year of birth:', df['Birth Year'].max())
    # most common
    print('Earliest year of birth:', df['Birth Year'].mode()[0])

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()
