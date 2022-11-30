"""EXPLORE US BIKESHARE DATA
Course: Programming for Data Science with Python
Student: Eva Santamaría López
Date: 30 Nov 2022
Version 02
"""

import time
import pandas as pd
import numpy as np

CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }

#Lists to check validity of the user's input. Capitalized variables = Constant values.

def get_filters():

    """
    Asks user to specify a city, month, and day to analyze.

    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """
    print('Hello! Let\'s explore some US bikeshare data!')

    # While loop to ask for the selected city until a valid result is given. 'city' variable as outcome.
    # An error message prompts if the user input does not match the data variable.

    cities = ('chicago', 'new york city', 'washington')
    while True:
        city = input('Which city would you like to explore? Type: Chicago, New York City, or Washington.\n').lower()
        if city not in cities:
            print('Sorry I could not understand you. Please try again.')
            continue
        else:
            break
    
    # TO DO: get user input for month (all, january, february, ... , june) 
    # Bucle to get the selected month as outcome.
    # An error message prompts if the user input does not match the data variable.

    months = ('all', 'january', 'february', 'march', 'april', 'may', 'june')
    while True:
        month = input('Which time period would you like to explore? Type: Month name from January to June or All.\n').lower()
        if month not in months:
            print('Sorry I could not understand you. Please try again')
            continue
        else:
            break

    # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)
    # Bucle to get the selected weekday as outcome.
    # An error message prompts if the user input does not match the data variable.

    days = ('all', 'monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday', 'sunday')
    while True:
        day = input('Which period of the week would you like to explore? Type: Day name from Monday to Sunday or All. \n').lower()
        if day not in days:
            print('Sorry I could not understand you. Please try again')
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
    # Load data from the selected file into a dataframe
    df = pd.read_csv(CITY_DATA[city])

    return df

#TIME STATS
def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()
    
    # convert the Start Time column to datetime
    df['Start Time'] = pd.to_datetime(df['Start Time'])
        
    # Prepare time data. Extract month, weekday and hour from Start Time to create new columns
    df['Month'] = df['Start Time'].dt.month
    df['Day of week'] = df['Start Time'].dt.weekday 
    df['Hour'] = df['Start Time'].dt.hour 

    # Display the most common month
    most_common_month = df['Month'].mode() [0] 
    print('Most common month: ',most_common_month)

    # Display the most common day of week
    most_common_weekday = df['Day of week'].mode()[0]
    print('Most common day of the week: ', most_common_weekday)
        
    # Display the most common start hour
    most_common_start_hour = df['Hour'].mode()[0]
    print('Most commmon start time: ',most_common_start_hour,'h')

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


#STATION STATS
def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # Display most commonly used start station
    most_commonly_used_start_station = df['Start Station'].mode()[0]
    print('Most commonly Start station used: ',most_commonly_used_start_station)
        
    # Display most commonly used end station
    most_commonly_used_end_station = df['End Station'].mode()[0]
    print('Most commonly End station used: ',most_commonly_used_end_station)
        
    # Display most frequent combination of start station and end station trip
    most_common_start_end_combination = df.groupby(['Start Station','End Station']).size().nlargest(1)
    print('Most common start and end station combination: \n', most_common_start_end_combination)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

#TRIP DURATION STATS
def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # Display total travel time
    total_travel_time = df['Trip Duration'].sum()
    print('Total travel time: ', total_travel_time)

    # Display mean travel time
    mean_travel_time = df['Trip Duration'].mean()
    print('Time travel mean: ', mean_travel_time)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

#USER STATS
def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # Display counts of user types
    users_count_per_type=df['User Type'].value_counts()
    print('Count of users inside each typology\n: ', users_count_per_type)

    # Display counts of gender
    users_count_per_gender=df['Gender'].value_counts()
    print('Count of users gender:\n', users_count_per_gender)

    # Display earliest birthday year.
    earliest_birth_year=df['Birth Year'].min()
    print('Earliest birth year:', int(earliest_birth_year))
        
    # Display most recent birthday year.
    most_recent_birth_year=df['Birth Year'].max()
    print('Most recent birth year', int(most_recent_birth_year))
        
    # Display most common birth year
    most_common_birth_year= df['Birth Year'].mode()[0]
    print('Most common birth year: ', int(most_common_birth_year))

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
