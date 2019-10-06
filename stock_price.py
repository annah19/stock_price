DATE_COL = 0
VOLUME_COL = 6
ADJ_CLOSE_COL = 5


def open_file(filename):
    ''' Returns a file stream if filename found, otherwise error msg '''
    try:
        file_stream = open(filename, "r")
        return file_stream
    except FileNotFoundError:
        return print("Filename", filename ,"not found!")

def get_data_list(file_stream):
    ''' Input a file stream, returns a data file, where the data is a list of list. 
    Each line is a list and a string '''
    data_list = [ ]	

    for line_str in file_stream:
        # strip end-of-line, split on commas, and append items to list 
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
        # If the month of that year is not already in the list we append it to the list
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
        # average_price = (V1∗C1+V 2∗C2+···+Vn∗Cn)/(V1+V2+···+Vn)
        monthly_averages_list[x].append(vol_adj_sum / vol_sum)
        monthly_averages_list[x] = tuple(monthly_averages_list[x])

    return monthly_averages_list

def get_highest_day(data_list):
    '''  '''
    highest_price = 0
    highest_day = ""
    for i in range(1,len(data_list)):
        if float(data_list[i][ADJ_CLOSE_COL]) > highest_price:
            highest_price = float(data_list[i][ADJ_CLOSE_COL])
            highest_day = data_list[i][DATE_COL]
    return highest_price, highest_day


def main():
    filename = input("Enter filename: ")
    file_stream = open_file(filename)
    
    data_list = get_data_list(file_stream)

    monthly_averages = get_monthly_averages(data_list)
    print(monthly_averages)

    highest_day = get_highest_day(data_list)
    print("Highest price", highest_day[0], "on day", highest_day[1])

main()