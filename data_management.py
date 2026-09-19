import csv, sqlite3 # ha ha

def read_transactions(db, csv_pointer, cat_defs_file= "", date_col = "Date", desc_col = "Description", cat_col = "Category", val_col = "Debit") -> None:
    """Imports a specified csv into a specified database.
    
    Args:
    db: a db handle
    csv: name/path for a csv file
    cat_defs_file: a json file that maps payment descriptions to categories if one is not found.
    date_col: the column header to use as a date
    desc_col: column header for payment title
    cat_col: column header for payment category
    val_col: column header for payment amount    
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

def open_create_db(db_pointer) -> sqlite3.Connection:
    """Creates or opens a specified database.

    Args:
    db_pointer: name/path of a database you want to connect to or make.
    """
    con = sqlite3.connect(db_pointer)
    cur = con.cursor()

    cur.execute("CREATE TABLE IF NOT EXISTS transactions(date text, description text, category text, value real)")
    cur.execute("""
                INSERT INTO transactions VALUES
                ('2026-01-05', 'Poopmarket', 'Dining', '38.39')
                """)
    con.commit()
    cur.close()

    return con

    