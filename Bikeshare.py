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
        city=input("What city data would like to see,Chicago, New York City or Washington?\n").lower()

        if city not in ('chicago', 'new york city', 'washington', 'all'):
            print("invalid input, Please enter a valid input:\n")
            continue

        else:
            break

    # get user input for month (all, january, february, ... , june)
    while True:
        month=input("What month data would like to see,all, january, february, ... , june?\n").lower()

        if month not in ('january', 'february', 'march', 'april', 'may', 'june','all'):
            print("invalid input, Please enter a valid input:\n")
            continue
        else:
            break


    # get user input for day of week (all, monday, tuesday, ... sunday)
    while True:
        day=input("What day data would like to see,all, Sunday, Monday, Tuesday, Wednesday, Thursday, Friday, Saturday,or all)\n").lower()


        if day not in ('sunday', 'monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday', 'all'):
            print("invalid input, Please enter a valid input:\n")
            continue
        else:
            break


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

    # extract month and day of week from Start Time to create new columns
    df['month'] = df['Start Time'].dt.month
    df['day_of_week'] = df['Start Time'].dt.weekday_name

    # filter by month if applicable
    if month != 'all':
        # use the index of the months list to get the corresponding int
        months = ['january', 'february', 'march', 'april', 'may', 'june']
        month = months.index(month) + 1

        # filter by month to create the new dataframe
        df = df[df['month'] == month]

    # filter by day of week if applicable
    if day != 'all':
        # filter by day of week to create the new dataframe
        df = df[df['day_of_week'] == day.title()]

    return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # display the most common month
    common_month=df['month'].mode()[0]
    print('The most common month: ',common_month)



    # display the most common day of week
    common_day=df['day_of_week'].mode()[0]
    print('The most common day: ',common_day)



    # display the most common start hour
    df['hour'] = df['Start Time'].dt.hour
    common_hour=df['hour'].mode()[0]
    print('The most common hour: ',common_hour)



    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # display most commonly used start station
    common_start_station=df['Start Station'].mode()[0]
    print('The most common start station: ',common_start_station)

    # display most commonly used end station
    common_end_station=df['End Station'].mode()[0]
    print('The most common end station: ',common_end_station)

    # display most frequent combination of start station and end station trip
    common_start_end =df.groupby(['Start Station','End Station']).size().nlargest(1)
    print('The most common start station and end station: ',common_start_end)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # display total travel time
    travel_time=df['Trip Duration'].sum()
    print('The total travel time is: ', travel_time)


    # display mean travel time
    mean_travel_time=df['Trip Duration'].mean()
    print('The mean travel time is: ', mean_travel_time)


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # Display counts of user types
    user_types = df['User Type'].value_counts()
    print('User count: ',user_types)

    # Display counts of gender
    if 'Gender' not in df :
        print('Sorry, gender count information is not available for Washington city')
    else:
        gender_count=df['Gender'].value_counts()
        print('Gender count: ',gender_count )
    # Display earliest, most recent, and most common year of birth
    if 'Birth Year' not in df:
        print('Birth year information is not available for Washington city')
    else:
        earliest=df['Birth Year'].min()
        most_recent=df['Birth Year'].max()
        common_year= df['Birth Year'].mode()[0]
        print('The earliest birth year is: {}.\n The most recent birth year is: {}.\n The most common birth year is: {}'.format(earliest,most_recent,common_year))
#calculate time it took to run this function 
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

def display_raw_data(df):

    view_data = input("Would you like to view 5 rows of individual trip data? Enter yes or no?\n").lower()
    start_loc = 0
    while (view_data=='yes'):
        print(df.iloc[0:start_loc])
        start_loc += 5
        view_data = input("Do you wish to continue?: ").lower()


def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)
        display_raw_data(df)
        print("thank you")

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break

if __name__ == "__main__":
	main()
