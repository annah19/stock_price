DATE_COL = 0
VOLUME_COL = 6
ADJ_CLOSE_COL = 5


def open_file(filename):
    ''' Returns a file stream if filename found, otherwise error msg '''

    try:
        file_stream = open(filename, "r")
        return file_stream

    except FileNotFoundError:
        return None


def get_data_list(file_stream):
    ''' Input a file stream, returns a data file, where the data is a list of list. 
    Each line is a list and a string '''

    data_list = [ ]	

    for line_str in file_stream:
        # Put a splitted list into another list
        data_list.append(line_str.strip().split(',')) 

    return data_list

def create_month_list(data_list):
    ''' Input data and returns a list of list with the first index as 
    the year and month '''

    month_list = []

    # We don't include the header in the file in the for loop
    for i in range(1,len(data_list)):

        # We only need the year and the month
        date = data_list[i][DATE_COL][:-3]

        # If the month of that year is not already in the list
        # we append it to the list
        if [date] not in month_list:
            month_list.append([date])

    return month_list

def get_monthly_averages(data_list):
    ''' Returns the average price for the month'''

    monthly_averages_list = create_month_list(data_list)
    
    # We need to go through every month, make sure the date 
    # is in that month, if the date is in the month we add 
    # that to the calculation
    for x in range(0, len(monthly_averages_list)):

        vol_sum = 0
        vol_adj_sum = 0
        
        for i in range(1,len(data_list)):

            date = data_list[i][DATE_COL][:-3]

            if date in monthly_averages_list[x]:
                adj_close = float(data_list[i][ADJ_CLOSE_COL])
                volume = float(data_list[i][VOLUME_COL])
                vol_sum += volume
                vol_adj_sum += volume * adj_close

        # Calculate the average price using this formula  
        # (V1∗C1+V 2∗C2+···+Vn∗Cn)/(V1+V2+···+Vn)

        monthly_averages_list[x].append(vol_adj_sum / vol_sum)
        monthly_averages_list[x] = tuple(monthly_averages_list[x])

    return monthly_averages_list

def get_highest_day(data_list):
    ''' Takes in a list and returns the highest price in that list '''
    highest_price = 0
    highest_day = ""

    for i in range(1,len(data_list)):

        if float(data_list[i][ADJ_CLOSE_COL]) > highest_price:
            highest_price = float(data_list[i][ADJ_CLOSE_COL])
            highest_day = data_list[i][DATE_COL]

    return highest_day, highest_price

def print_monthly_averages(monthly_averages_list):
    ''' Takes a list of tuples and prints out 2 columns'''

    # Print out the header for the information
    print("{:<10s} {:>7s}" .format("Month","Price"))

    # Print the average for each month
    for month_tuple in monthly_averages_list:
        print("{:<10s} {:>7.2f}" .format(month_tuple[0],month_tuple[1]))

    return

def main():

    filename = input("Enter filename: ")
    file_stream = open_file(filename)

    # Make sure the file exists before we run the program
    if file_stream:
    
        data_list = get_data_list(file_stream)

        monthly_averages = get_monthly_averages(data_list)
        
        print_monthly_averages(monthly_averages)

        highest_day = get_highest_day(data_list)

        # Only print out two digits after decimal point in the price column
        print("Highest price {:.2f}".format(highest_day[1]), "on day", highest_day[0])
    else:
        print("Filename {} not found!" .format(filename))

main()