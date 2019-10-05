DATE_COL = 0
VOLUME_COL = 6
ADJ_CLOSE_COL = 5


def open_file(filename):
    ''' Returns a file stream if filename found, otherwise error msg '''
    try:
        file_stream = open(filename, "r")
        return file_stream
    except FileNotFoundError:
        return print("Filename". filename ,"not found!")

def get_data_list(file_stream):
    ''' Input a file stream, returns a data file, where the data is a list of list. 
    Each line is a list and a string '''
    data_list = [ ]	
    # start with an empty list 
    for line_str in file_stream:
    # strip end-of-line, split on commas, and append items to list 
        data_list.append(line_str.strip().split(',')) 
    return data_list

def get_monthly_averages(data_list):
    ''' Returns the average price for the month'''

    monthly_averages_list = []

    
    for i in range(1,len(data_list)):
        
        date = data_list[i][DATE_COL]
        date = date.split("-")
        date = date[0] + "-" + date[1]

    vol_sum = 0
    vol_adj_sum = 0


    for i in range(1,len(data_list)):
        adj_close = float(data_list[i][ADJ_CLOSE_COL])
        volume = float(data_list[i][VOLUME_COL])
        vol_sum += volume
        vol_adj_sum += volume * adj_close
    
    average_price = vol_adj_sum / vol_sum


    # average_price = (V1∗C1+V 2∗C2+···+Vn∗Cn)/(V1+V2+···+Vn)
    return average_price

def get_highest_price(data_list):
    pass

def main():
    filename = input("Enter filename: ")
    file_stream = open_file(filename)
    
    data_list = get_data_list(file_stream)

    test = get_monthly_averages(data_list)

    print(test)
    

main()