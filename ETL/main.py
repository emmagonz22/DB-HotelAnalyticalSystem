import etl_db_files as etl_db
import etl_xlsx_files as etl_xlsx
import etl_csv_files as etl_csv




if __name__ == "__main__":
    # load chain
    etl_xlsx.load_xlsx()
    # load hotel
    etl_csv.load_hotel_csv()
    # load employee

    # load login

    # load room description

    # load room

    # load room unavailable

    # load client

    # load reserve
    etl_db.load_reservation_data()