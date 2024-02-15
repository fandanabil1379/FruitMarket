from tabulate import tabulate

HEADERS = ('Index', 'Name', 'Stock', 'Price')

def show(table, headers=HEADERS, title='\nTabel Daftar Buah\n'):
    """Fungsi untuk menampilkan tabel

    Args:
        table (Dictionary): Database
        headers (Tuple, optional): Nama kolom tabel. Defaults to HEADERS.
        title (str, optional): Judul tabel. Defaults to '\nTabel Daftar Buah\n'.
    """
    # Menampilkan judul tabel
    print(title)

    # Menampilkan database dalam tabulasi
    print(tabulate(table.values(), headers, tablefmt="grid"))

def add(table):
    """Fungsi untuk menambah buah baru

    Args:
        table (Dictionary): Database
    """
    # Memasukkan nama, harga, dan ketersediaan buah
    name = input('Masukkan Nama Buah: ')
    stock = input('Masukkan Stock Buah: ')
    price = input('Masukkan Harga Buah: ')

    # Melakukan cek apabila buah sudah ada di database
    for item in table.values():
        # Jika ada, maka update stock dan harga
        if name.capitalize() == item[1]:
            item[2] += int(stock)
            item[3] = int(price)
            break
    # Jika tidak, tambahkan sebagai item baru
    else:
        table.update({
            f'{name}': [
                len(table)+1,
                name.capitalize(), 
                int(stock),
                int(price)]
            }
        )

    # Menampilkan daftar buah terkini
    show(table)

def delete(table):
    """Fungsi untuk menghapus buah

    Args:
        table (Dictionary): Database
    """
    while True:
        # Menampilkan daftar buah yang tersedia
        show(table)

        # Meminta input indeks buah
        try:
            id = int(input('Masukkan Indeks Buah: '))
            if id > len(table)-1:
                print('Indeks di luar jangkauan!')
                continue
        except:
            print('Masukkan angka saja!')
            continue 

        # Proses menghapus buah berdasarkan indeks 
        for val in table.copy().values():
            if id in val:
                del table[val[1]]
  
        # Proses update indeks buah
        for idx, item in enumerate(list(table.values())):
            if idx < item[0]:
                item[0] -= 1
        else:
            break 

    # Menampilkan daftar buah terkini
    show(table) 
            
def buy(table):
    """Fungsi untuk belanja buah

    Args:
        table (List): Database
    """
    CART = []
    # Proses input buah dan jumlah buah yang akan dibeli
    reorder = 'yes'
    while reorder != 'no':
        # Menampilkan daftar buah yang tersedia
        show(table)

        # Proses memilih buah berdasarkan indeks
        while True:
            try:
                id = int(input('Masukkan Indeks Buah: '))
                if id in list(table.values())[id]:
                    break
            except: 
                print('Indeks buah tidak terdaftar')
            
        # Proses menentukan jumlah buah yang dipesan
        while True:
            try:
                amount = int(input('Masukkan Jumlah Buah: '))
            except:
                print('Jumlah buah tidak valid')
                continue

            if amount > list(table.values())[id][2]:
                print('Jumlah stock kurang')
                continue
            else:
                CART.append([
                    list(table.values())[id][1],
                    amount,
                    list(table.values())[id][3]
                ])
                break
    
        # Menampilkan keranjang belanjaan
        print(tabulate(CART, ['Name', 'Qty', 'Price'], tablefmt="grid"))

        # Meminta konfirmasi ulang apakah akan belanja lagi
        while True:
            confirm = input('Apakah akan order lagi?: ')
            if confirm.isalpha() and confirm.upper() in ['N', 'NO']:
                reorder = 'no'
                break
            elif confirm.isalpha() and confirm.upper() in ['Y', 'Yes']:
                reorder = 'yes'
                break
            else:
                print('Silahkan masukkan Yes/No saja!')
                continue

    # Menghitung total belanjaan
    for item in CART:
        item.append(item[1] * item[2])
    else:
        print(tabulate(CART, ['Name', 'Qty', 'Price', 'Total Harga'], 
                       tablefmt="grid"))
        
    # Proses pembayaran
    total = sum([item[-1] for item in CART])
    pembayaran(total)

def pembayaran(nominal):
    """Fungsi untuk membayar belanjaan

    Args:
        nominal (int): Jumlah uang yang dibayar
    """
    print(f'Total yang harus Anda bayar: Rp{nominal}')
    while True:
        try:
            # Meminta input uang pembayaran
            bayar = int(input('Silahkan masukkan uang Anda:'))
        except:
            print('Masukkan angka!')
            continue
    
        # Jika uang terpenuhi, hitung sisa
        if bayar >= nominal:
            print(f'Uang kembalian Anda sebesar {bayar - nominal}')
            break
        # Jika tidak, maka hitung kekurangan
        else:
            print(f'\nUang anda kurang sebesar {nominal - bayar}\n')
        