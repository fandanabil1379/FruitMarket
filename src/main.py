import market

database = [
    [0, 'Apel', 20, 10000],
    [1, 'Anggur', 15, 15000],
    [2, 'Jeruk', 25, 20000],
]

main_menu = '''
Selamat Datang di Pasar Buah!

List Menu:

1. Show
2. Add
3. Delete
4. Buy
5. Exit

'''
def main():
    while True:
        choice = input(main_menu)
        if choice == '1':
            market.show(database)
        elif choice == '2':
            market.add(database)
        elif choice == '3':
            market.delete(database)
        elif choice == '4':
            market.buy(database)
        elif choice == '5':
            break
        else:
            print('Masukkan angka sesuai pilihan (1-5)')
            continue


main()