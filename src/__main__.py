import os
import sys
import csv
import market

def clear_screen():
    """
    A function to clean the user interface
    """
    # For Windows
    if os.name == 'nt':
        _ = os.system('cls')
    # For macOS and Linux
    else:
        _ = os.system('clear')

def initialize_db():
    """
    A function to initialize the database 

    Returns:
        dict: Fruit database
    """
    with open(PATH, 'r') as file:
        # Membuat objek reader
        reader = csv.reader(file, delimiter=";")
        # Inisialisasi database kosong
        database = {}
        # Mengisi data ke dalam database
        for row in reader:
            idx, name, stock, price = row
            database.update({name: [int(idx), name, int(stock), int(price)]})

    return database

def main():
    """
    The main program to run the whole process
    """
    global database
    while True:
        # Meminta input berupa opsi fitur yang akan dijalankan
        choice = market.int_validation(main_menu)
        # Jalankan fitur sesuai opsi yang di pilih 
        if choice == 1:
            market.show(database)
        elif choice == 2:
            market.add(database)
        elif choice == 3:
            market.delete(database)
        elif choice == 4:
            market.buy(database)
        elif choice == 5:
            break
        # Jika opsi tidak ada, maka minta input ulang
        else:
            print('Masukkan opsi (1-5)\n')
            continue

        # Menjaga agar database selalu diperbarui
        with open(PATH, 'w') as file:
            # Membuat objek writer
            writer = csv.writer(file, delimiter=";")
            # Menulis data ke dalam file csv
            writer.writerows(database.values())

if __name__ == "__main__":
    # Mendefinisikan tampilan utama aplikasi
    main_menu = '''
Selamat Datang di Pasar Buah!

List Menu:

1. Show
2. Add
3. Delete
4. Buy
5. Exit

Input: '''
    
    # Membersihkan tampilan user
    clear_screen()

     # Setting the path of database file
    if getattr(sys, 'frozen', False):
        PATH = sys._MEIPASS
        PATH = os.path.join(PATH, 'data/db.csv') 
    else:
        PATH = os.getcwd()
        PATH = os.path.join(PATH, 'data/db.csv') 

    # Initializing database
    database = initialize_db()

    # Menjalankan menu utama
    main()