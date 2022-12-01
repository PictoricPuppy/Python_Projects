"""EXPLORE US BIKESHARE DATA
Course: Programming for Data Science with Python
Student: Eva Santamaría López
Date: 01 Dec 2022
Version 03
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
    
    # Display the most common month in word instead of number
    if most_common_month ==1:
        most_common_month = 'January'
    elif most_common_month ==2:
        most_common_month = 'February'
    elif most_common_month ==3:
        most_common_month = 'March'
    elif most_common_month ==4:
        most_common_month = 'April'
    elif most_common_month ==5:
        most_common_month = 'May'
    elif most_common_month ==6:
        most_common_month = 'June'
    elif most_common_month ==7:
        most_common_month = 'July'
    elif most_common_month ==8:
        most_common_month = 'August'
    elif most_common_month ==9:
        most_common_month = 'September'
    elif most_common_month ==10:
        most_common_month='October'
    elif most_common_month ==11:
        most_common_month='November'
    elif most_common_month ==12:
        most_common_month = 'December'
    
    print('Most common month: ',most_common_month)

    # Display the most common day of week
    most_common_weekday = df['Day of week'].mode()[0]
    
    #Displays the most common day of week in word instead of number
    if most_common_weekday==1:
        most_common_weekday = 'Monday'
    elif most_common_weekday ==2:
        most_common_weekday = 'Tuesday'
    elif most_common_weekday ==3:
        most_common_weekday = 'Wednesday'
    elif most_common_weekday ==4:
        most_common_weekday = 'Thursday'
    elif most_common_weekday ==5:
        most_common_weekday = 'Friday'
    elif most_common_weekday ==6:
        most_common_weekday = 'Saturday'
    elif most_common_weekday ==7:
        most_common_weekday = 'Sunday'
        
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
    total_travel_time_seconds = total_travel_time%60
    total_travel_time_minutes = total_travel_time//60%60
    total_travel_time_hours = total_travel_time//3600%60
    
    print('Total travel time: ', round(total_travel_time_hours,2),' hours ',round(total_travel_time_minutes,2),' minutes ', round(total_travel_time_seconds,2),' seconds')

    # Display mean travel time
    mean_travel_time = df['Trip Duration'].mean()
    mean_travel_time_seconds = mean_travel_time%60
    mean_travel_time_minutes = mean_travel_time//60%60
    mean_travel_time_hours = mean_travel_time//3600%60
    print('Mean travel time: ', round(mean_travel_time_hours,2),' hours ',round(mean_travel_time_minutes,2),' minutes ', round(mean_travel_time_seconds,2),' seconds')

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

#USER STATS
def user_stats(df,city):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # Display counts of user types
    users_count_per_type=df['User Type'].value_counts()
    print('Count of users inside each typology\n: ', users_count_per_type)

    # Display counts of gender
    if city != 'washington':
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
        
    if city == 'washington':
        print('DATABASE INFO: Washington does not have user stats data.')
        
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

def display_raw_data(df):
    """ Your docstring here """
    i = 0
    raw = input("Would you like to see some data from the dataset? Type: Yes or No.").lower() # TO DO: convert the user input to lower case using lower() function
    pd.set_option('display.max_columns',200)

    while True:            
        if raw == 'no':
            break
        elif raw == 'yes':
            print(df.iloc[i]) # TO DO: appropriately subset/slice your dataframe to display next five rows
            raw = input("Display 5 adittional lines. Type: Yes/No.").lower() # TO DO: convert the user input to lower case using lower() function
            i += 5
        else:
            raw = input("\nYour input is invalid. Please enter only 'yes' or 'no'\n").lower()
            
def main():

    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df,city)
        display_raw_data(df)

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes' and restart.lower()!='ye' and restart.lower() != 'y':
            break


if __name__ == "__main__":
	main() 
