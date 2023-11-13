import pandas as pd
import numpy as np
import time

#creating a dictionary with the cities as keys and their file locations as values
CITY_DATA = { 'chicago': 'D:\\Bike-Share\\chicago.csv',
    'new york city': 'D:\\Bike-Share\\new_york_city.csv',
    'washington': 'D:\\Bike-Share\\washington.csv' }

def get_filters():
    """
    Asks user to specify a city, month, and day to analyze.

    args: none

    Returns:
        str (city): - name of the city to analyze
        str (month): - name of the month to filter by, or "all" to apply no month filter
        str (day): - name of the day of week to filter by, or "all" to apply no day filter
    """
    print(f"Hello! Let\'s explore some US bikeshare data!")
    # get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs
    # shows an empty variable to take in the city input from user
    city = ''
    # running this while loop to ensure valid inputs only
    while city not in CITY_DATA.keys():
        print("\n Welcome!") 
        print("\n Which City Do You Want to Explore?")
        print("\n  1. chicago 2. washington 3. new york city")
        print("\n City Name is NOT case sensitive")
        # taking user input and enforcing it to lower caps 
        city = input().lower()

        if city not in CITY_DATA.keys():
            print("\Please check your input and use the correct format.")
            print("\n Let us try again!...")

    print(f"\nLet Us Explore {city.title()}!")   

    # get user input for month (all, january, february, ... , june)
    # creating a dictionary to store the months and "all" option
    MONTH_DATA = {'january': 1, 'february': 2, 'march': 3, 'april': 4, 'may': 5, 'june': 6, 'all': 7}
    month = ''
    while month not in MONTH_DATA.keys():
        print("\nPlease enter the month, between January to June, that you would like to see:")
        print("\nAccepted input:\nFull month name; not case sensitive (e.g. january or JANUARY).\nFull month name in title case (e.g. April).")
        print("\n(If you wish to view data for all months, please type 'all' or 'All' or 'ALL'.)")
        month = input().lower()

        if month not in MONTH_DATA.keys():
            print("\nInvalid input. Please try again in the accepted input format.")
            print("\nRestarting...")


    print(f"\n\nGreat! Let us explore data for {month.title()} month(s).")



    # get user input for day of week (all, monday, tuesday, ... sunday)
    # Creating a list with days of the week and the "all" option
    DAY_DATA = ['monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday', 'sunday', 'all']
    day = ''
    while day not in DAY_DATA:
        print("\n Please select the day of the week, from Monday to Sunday, that you would like to explore." )
        print("\n You can also select 'all' to view all the days of the week.")
        print("\n The Day field is NOT case sensitve, so MONDAY and monday are the same.")
        day = input().lower()

        if day not in DAY_DATA:
            print("\nPlease check your input and use the correct format. ")
            print("\nLet us try again!...")


    print(f"\nGreat! Now, Let us explore data for {city.upper()}")
    print(f"\nIn the month of {month.upper()}")
    print(f"\nAnd for the following day/s: {day.upper()}")

    print('-'*40)
    return city, month, day


# creating a function that will load data from the three .csv files
def load_data(city, month, day):
    """
    Loads data for the specified city and filters by month and day if applicable.

    Args:
        parameter1 (str): name of the city to analyze
        parameter2 (str): name of the month to filter by, or "all" to apply no month filter
        parameter3 (str): name of the day of week to filter by, or "all" to apply no day filter
    Returns:
        df - Pandas DataFrame containing city data filtered by month and day
    """
    # Set display to view all columns
    pd.set_option('display.max_columns', None)
    pd.set_option('display.width', None)
    
    # Loading data for city 
    print("\nLoading Data...")
    df = pd.read_csv(CITY_DATA[city])

    # convert the Start Time and End Time column to datetime
    df['Start Time'] = pd.to_datetime(df['Start Time'])
    df['End Time'] = pd.to_datetime(df['End Time'])

    # Grab month, day of week and hour to create new columns
    df['month'] = df['Start Time'].dt.month
    df['day_of_the_week'] = df['Start Time'].dt.day_name()
    df['hour'] = df['Start Time'].dt.hour

    # Filtering by month if applicable
    if month != "all":
        # Using the index of the month in the list to return the corresponding integer
        months = ['january', 'february', 'march', 'april', 'may', 'june']
        month = months.index(month) + 1

        # Filtering by month to create the new dataframe
        df = df[df['month'] == month]

    # Filtering by day if applicable
    if day != 'all':
        # filter by day of week to create the new dataframe
        df = df[df['day_of_the_week']== day.title()]

    # Returns the file as a df with selected columns        

    return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel.
    args:
        parameter1(df): The dataframe you want to work on.

    Returns:
        none.
    """

    print('\nLet us look at some summary statistics!\n\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # display the most common month using mode method
    if not df['month'].empty:
        most_common_month = df['month'].mode().iloc[0]
        month_names = ['January', 'February', 'March', 'April', 'May', 'June']
        most_common_month_name = month_names[most_common_month - 1]
        print(f"The most common month is {most_common_month_name}")
    else:
        print("No mode found for the 'month' column.")

    # display the most common day of week
    if not df['day_of_the_week'].empty:
        most_common_day = df['day_of_the_week'].mode().iloc[0]
        print(f"The most common day of the week is {most_common_day}")
    else:
        print("No mode found for the 'day_of_the_week' column.")

    

    # display the most common start hour
    # grab hour from the Start Time column to create a new column
    if not df['hour'].empty:
        most_common_hour = df['hour'].mode().iloc[0]
        print(f"The most common hour is {most_common_hour}")
    else:
        print("No mode found for the 'hour' column.")
    


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # display most commonly used start station
    if not df['Start Station'].empty:
        common_start_station = df['Start Station'].mode().iloc[0]
        print(f"The most common start station is: {common_start_station}")
    else:
        print("No mode found for the 'Start Station' column.")


    # display most commonly used end station
    if not df['End Station'].empty:
        common_end_station = df['End Station'].mode().iloc[0]
        print(f"The most common end station is: {common_end_station}")
    else:
        print("No mode found for the 'End Station' column.")

    # display most frequent combination of start station and end station trip
    # creating a new column by combining start and end columns using str.cat
    # using .mode method to find the most frequent combination
    if not df[['Start Station', 'End Station']].empty:
        df['Start to End'] = df['Start Station'].str.cat(df['End Station'], sep=' to ')
        combination = df['Start to End'].mode().iloc[0]
        print(f"The most frequent combination is: {combination}")
    else:
        print("No mode found for the combination of start and end stations.")

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # display total travel time
    total_travel_time = df['Trip Duration'].sum()
    print("Total travel time: {} seconds".format(total_travel_time))

    # display mean travel time
    mean_travel_time = df['Trip Duration'].mean()
    print("Mean travel time: {} seconds".format(mean_travel_time))


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # Display counts of user types
    user_types = df['User Type'].value_counts()
    print("\nThere are {} user types in the dataset".format(len(user_types)))

    # Display counts of gender
    # Because not every df has the gender column, use try function 
    try:
        gender = df['Gender'].value_counts()
        print("\nThere are {} genders in the database".format(len(gender)))
    except:
        print("\nThe 'Gender' column does not exist in this file")


    # Display earliest, most recent, and most common year of birth
    # we use try function because not every df has the birth year column
    try:
        earliest = int(df['Birth Year'].min())
        recent = int(df['Birth Year'].max())
        common_year = int(df['Birth Year'].mode().iloc[0])
        print(f"\nThe earliest year of birth is {earliest}.\nThe most recent year of birth is {recent}.\nThe most common year of birth is {common_year}")
    except:
        print("\nThe 'Birth Year' column does not exist in this file")


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

# Display the output 
def display_data(df):
    """ Displaying the first five rows of data from the chosen city file """

    BIN_RESPONSE_LIST = ['yes', 'no']
    rdata = ''

    #counter ensures only details from the specified input are used
    counter = 0
    while rdata not in BIN_RESPONSE_LIST:
        print("\nDo you wish to view the raw data?")
        print("\nAccepted responses:\nYes or yes\nNo or no")
        rdata = input().lower()
        #the raw data from the df is displayed if user opts for it
        if rdata == "yes":
            print(df.head())
        elif rdata not in BIN_RESPONSE_LIST:
            print("\nPlease check your input.")
            print("Input does not seem to match any of the accepted responses.")
            print("\nRestarting...\n")

    #While loop to give user option of viewing more data
    while rdata == 'yes':
        print("Do you wish to view more raw data?")
        counter += 5
        rdata = input().lower()
        #If user opts for it, this displays next 5 rows of data
        if rdata == "yes":
             print(df[counter:counter+5])
        elif rdata != "yes":
             break

    print('-'*80)

# main function that uses all other functions
def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        display_data(df)
        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()


