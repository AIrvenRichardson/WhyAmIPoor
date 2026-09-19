import csv # ha ha

def read_transactions(db, csv_pointer, date_conv = "Date", cat_defs_file= "") -> None:
    """Imports a specified csv into a specified database.
    
    Args:
    db: a db handle
    csv: name/path for a csv file
    date_conv: the column header to use as a date
    cat_defs_file: a json file that maps payment descriptions to categories if one is not found.
    """
    #if not db: #Don't need a try block here since this will be called from a function that sets a db handle.
        #raise FileNotFoundError("No database found!") for now, let's not.

    #Check for the existence of the csv file.
    try:
        fp_csv = open(csv_pointer)
        reader = csv.reader(fp_csv)
    except FileNotFoundError:
        raise FileNotFoundError("Can't open the CSV or it does not exist! Exiting")

    # Don't know yet what the structure of these will look like so Imma just not do it for now.
    if cat_defs_file != "":
        print("ughhhhhhhhhhhhh")

    for row in reader:
        print(row)
    
    
    

    