"""EXPLORE US BIKESHARE DATA
Course: Programming for Data Science with Python
Student: Eva Santamaría López
Date: 30 Nov 2022
Version 01
"""
import time
import pandas as pd
import numpy as np

CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }

#Lists to check validity of the user's input. Capitalized variables = Constant values.
MONTH_DATA=['january','february','march','may','june','all']
WEEKDAY_DATA=['monday','tuesday','wednesday','thursday','friday','saturday','sunday','all']

def get_filters():
    """
    Asks user to specify a city, month, and day to analyze.

    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """
    print('Hello! Let\'s explore some US bikeshare data!')
    
    # TO DO: get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs  
    # The input of the user 'city_input' will be searched in the variable 'CITY_DATA'.
    # A new variable to store the user input is created
    city_input =' '
    
    # While loop to ask for the selected city until a valid result is given. 'city' variable as outcome.
    # An error message prompts if the user input does not match the data variable.
    while city_input not in CITY_DATA:
        city_input=input('Would you like to see data for Chicago, New York City, or Washington?\n')
        
        if city_input.lower() in CITY_DATA:
            city = CITY_DATA[city_input.lower()]
            
        else:
            print ('Sorry I could not find this city in our Database. Try typing Chicago, New York City, or Washington')
    
    # TO DO: get user input for month (all, january, february, ... , june)    
    # The input of the user 'month_input' will be searched in the variable 'MONTH_DATA'. 'month' variable as outcome
    # A new variable to store the user input is created.
    month_input = ' '
    
    # Bucle to get the selected month as outcome.
    # An error message prompts if the user input does not match the data variable.
    month_input = input('Which month - January, February, March, April, May, June or all?\n')
    if month_input.lower() in MONTH_DATA:
        month = month_input.lower()
        
    else:
        print('Sorry I could not find this month in our Database. Try typing a month between January and June.')
    
    # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)
    # The input of the user 'weekday_input' will be searched in the variable 'WEEKDAY_DATA'. 'day' variable as outcome
    # A new variable to store the user input is created.
    day_input = ' '
    
    #Bucle to get the selected weekday as outcome.
    # An error message prompts if the user input does not match the data variable.
    day_input = input('Which day - Monday, Tuesday, Wednesday, Thursday, Friday, Saturday, Sunday or all?\n')
    if day_input.lower() in WEEKDAY_DATA:
            day = day_input.lower()
    
    print('User selection: ',city,'-',month,'-',day)
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
    df = pd.read_csv(city)

    # convert the Start Time column to datetime
    df['Start Time'] = pd.to_datetime(df['Start Time'])
    
    # extract month and day of week from Start Time to create new columns
    df['month'] = df['Start Time'].dt.month
    df['day_of_week'] = df['Start Time'].dt.day_of_week 
    df['hour'] = df['Start Time'].dt.hour 

    # Month filter depending on the month input selection 'all' or an specific month.
    if month != 'all':
        month = MONTH_DATA.index(month)
    else:
        df = df.loc(df['month']==month)

    # Day filter depending on the month input selection 'all' or an specific weekday.
    if day != 'all':
        df = df.loc[df['day_of_week'] == day.title()]
    else: #sobra???
        df = df.loc(df['day']==day)
        
    return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # display the most common month
    most_common_month = df['month'].mode()[0]
    print('Most common month: ',most_common_month)
    
    # display the most common day of week
    most_common_weekday = df['day_of_week'].mode()[0]
    print('Most common day of the week: ', most_common_weekday)
    
    # display the most common start hour
    most_common_start_hour = df['hour'].mode()[0]
    print('Most commmon start time: ',most_common_start_hour,'h')

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # display most commonly used start station
    most_commonly_used_start_station = df['Start Station'].mode()[0]
    print('Most commonly Start station used: ',most_commonly_used_start_station)
    
    # display most commonly used end station
    most_commonly_used_end_station = df['End Station'].mode()[0]
    print('Most commonly End station used: ',most_commonly_used_end_station)
    
    # display most frequent combination of start station and end station trip
    most_common_start_end_combination = df.groupby(['Start Station'],['End Station']).size().nlargest(1)
    print('Most common start and end station combination: ', most_common_start_end_combination)
    
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # display total travel time
    total_travel_time = df['Trip Duration'].sum()
    print('Total travel time: ', total_travel_time)

    # display mean travel time
    mean_travel_time = df['Trip Duration'].mean()
    print('Time travel mean: ', mean_travel_time)
    
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # Display counts of user types
    users_count_per_type=df['User Type'].value_counts()
    print('Count of users inside each typology: ', users_count_per_type)

    # Display counts of gender
    users_count_per_gender=df['Gender'].value_counts()
    print('Count of users gender:', users_count_per_gender)

    # Display earliest birthday year.
    earliest_birth_year=df['Birth Year'].min()
    print('Earliest birth year: ', earliest_birth_year)
    
    # Display most recent birthday year.
    most_recent_birth_year=df['Birth Year'].max()
    print('Most recent birth year', most_recent_birth_year)
    
    # Display most common birth year
    most_common_birth_year= df['Birth Year'].mode()[0]
    print('Most common birth year: ', most_common_birth_year)
    
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

#Main function of the code. Calls to the other functions defined on the file.
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
