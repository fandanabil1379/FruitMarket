from tabulate import tabulate

HEADERS = ('Index', 'Name', 'Stock', 'Price')

# Fungsi menampilkan
def show(table, headers=HEADERS, title='\nTabel Daftar Buah\n'):
    """Fungsi untuk menampilkan tabel

    Args:
        table (List): Database
        headers (Tuple, optional): Nama kolom tabel. Defaults to HEADERS.
        title (str, optional): Judul tabel. Defaults to '\nTabel Daftar Buah\n'.
    """
    print(title)
    print(tabulate(table, headers, tablefmt="grid"))

# Fungsi Menambah buah
def add(table):
    """Fungsi untuk menambah buah baru

    Args:
        table (List): Database
    """
    name = input('Masukkan Nama Buah: ')
    stock = input('Masukkan Stock Buah: ')
    price = input('Masukkan Harga Buah: ')

    for i, item in enumerate(table):
        if name.capitalize() == item[1]:
            item[2] += int(stock)
            item[3] = int(price)
            break
    else:
        table.append([
            len(table)+1,
            name, 
            int(stock),
            int(price)
        ])

    show(table)

# Fungsi Menghapus buah
def delete(table):
    """Fungsi untuk menghapus buah

    Args:
        table (List): Database
    """
    while True:
        show(table)

        id = int(input('Masukkan Indeks Buah: '))

        if id > len(table)-1:
            print('Indeks di luar jangkauan!')
            continue
        
        for item in table:
            if id in item:
                table.remove(item)

        for idx, item in enumerate(table):
            if idx < item[0]:
                item[0] -= 1
        else:
            break  

    show(table) 
            
# Fungsi Membeli buah
def buy(table):
    CART = []
    reorder = 'yes'
    while reorder != 'no':
        show(table)
        while True:
            id = int(input('Masukkan Indeks Buah: '))
            for item in table:
                if id in item:
                    id = id
                    break
            else:
                print('Indeks buah tidak terdaftar')
                continue
            break

        while True:
            amount = int(input('Masukkan Jumlah Buah: '))
            for item in table:
                if id in item:
                    if amount > item[2]:
                        print('Jumlah stock kurang')
                        break
                    else:
                        CART.append([
                            item[1],
                            amount,
                            item[3]
                        ])
                        break
            break 

        show(CART, ['Name', 'Qty', 'Price'])

        confirm = input('Apakah akan order lagi?: ')
        if confirm == 'no':
            reorder = 'no'

    # Menghitung total belanjaan
    for item in CART:
        item.append(item[1] * item[2])
    else:
        show(CART, ['Name', 'Qty', 'Price', 'Total Harga'])

    # Proses pembayaran
    total = sum([item[-1] for item in CART])
    pembayaran(total)

# Mendefinisikan fungsi pembayaran
def pembayaran(nominal):
    """Fungsi untuk membayar belanjaan

    Args:
        nominal (int): Jumlah uang yang dibayar
    """
    while True:
        # Meminta input uang pembayaran
        bayar = input('Silahkan masukkan uang Anda:')
        # Validasi input
        if is_number(bayar):
            bayar = int(bayar)
            # Menghitung kekurangan atau sisa
            if bayar >= nominal:
                print(f'Uang kembalian Anda sebesar {bayar - nominal}')
                break
            else:
                print(f'\nUang anda kurang sebesar {nominal - bayar}\n')
        else:
            print('Masukkan angka!')

# Mendefinisikan validasi input untuk numerik
def is_number(value):
    """Fungsi untuk validasi numerik

    Args:
        value (str): Bilangan

    Returns:
        Boolean: True jika bilangan, sebaliknya
    """
    try:
        int(value)
        return True
    except:
        return False