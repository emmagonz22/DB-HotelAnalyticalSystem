import etl_db_files as etl_db
import etl_xlsx_files as etl_xlsx
import etl_csv_files as etl_csv
import etl_json_files as etl_json




if __name__ == "__main__":
    # load chain
    etl_xlsx.load_chain_xlsx()
    # load hotel
    etl_csv.load_hotel_csv()
    # load employee
    etl_json.load_employee_json()
    # load login
    etl_xlsx.load_login_xlsx()
    # load room description
    etl_json.load_roomdetails_json()
    # load room
    etl_db.load_room_data()
    # load room unavailable
    etl_csv.load_room_unavailable_csv()
    # load client
    etl_csv.load_client_csv()
    # load reserve
    etl_db.load_reservation_data()