from tabulate import tabulate

def int_validation(prompt):
    """Fungsi untuk validasi input bilangan bulat.

    Args:
        prompt (String): Pesan tampilan pada prompt.

    Returns:
        int: bilangan bulat.
    """
    while True:
        try:
            # Meminta input kepada user
            num = float(input(prompt))
            # Jika input bernilai negatif, maka minta input ulang
            if num < 0:
                print('Tidak boleh negatif!')
                continue
            # Selain itu, output kan sebagai bilangan bulat
            else:
                break
        # Jika input selain numerik, maka minta input ulang
        except:
            print('Silahkan input kan numerik!')
            continue

    return int(num)

def str_validation(prompt):
    """Fungsi untuk validasi input teks.

    Args:
        prompt (String): Pesan tampilan pada prompt.

    Returns:
        str: teks.
    """
    while True:
        # Meminta input teks kepada user
        sentence = input(prompt)
        # Jika teks terdiri dari alfabet, maka output kan teks 
        if sentence.isalpha():
            break
        # Selain itu, maka minta input ulang
        else:
            print('Silahkan input kan alfabet!')
            continue

    return sentence


def convert_to_table(data, columns, title):
    """Fungsi untuk menampilkan data dalam format tabulasi

    Args:
        data (Dictionary): Database.
        columns (Tuple, optional): Nama kolom dalam tabel.
        title (str, optional): Judul tabel.
    """
    # Menampilkan judul tabel
    print(title)

    # Mengubah format data menjadi format tabulasi
    print(tabulate(data, headers=columns, tablefmt="grid"))

def show(table):
    """Fungsi untuk menampilkan daftar buah

    Args:
        table (Dictionary): Database buah.
    """
    # Menampilkan database buah dalam format tabulasi
    convert_to_table(
        data=table.values(), 
        columns=['Index', 'Name', 'Stock', 'Price'],
        title='\nTabel Daftar Buah\n'
    )

def add(table):
    """Fungsi untuk menambah buah baru

    Args:
        table (Dictionary): Database buah.
    """
    # Memasukkan nama, harga, dan ketersediaan buah
    name = str_validation('Masukkan Nama Buah: ')
    stock = int_validation('Masukkan Stock Buah: ')
    price = int_validation('Masukkan Harga Buah: ')

    # Melakukan cek apabila buah sudah ada di database
    for item in table.values():
        # Jika ada, maka update stock dan harga
        if name.capitalize() == item[1]:
            item[2] += stock
            item[3] = price
            break
    # Jika tidak, tambahkan sebagai item baru
    else:
        table.update({
            f'{name}': [
                len(table)+1,
                name.capitalize(), 
                stock,
                price]
            }
        )

    # Menampilkan daftar buah terkini
    show(table)

def delete(table):
    """Fungsi untuk menghapus buah

    Args:
        table (Dictionary): Database buah.
    """
    while True:
        # Menampilkan daftar buah yang tersedia
        show(table)

        # Meminta input indeks buah
        id = int_validation('Masukkan Indeks Buah: ')

        # Cek apakah indeks buah tersedia atau tidak
        # Jika tidak ada, maka minta input ulang
        if id > len(table)-1:
            print('Indeks di luar jangkauan!')
            continue
        # Sebaliknya, hapus buah sesuai indeks yg dimaksud
        else:
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
        table (List): Database buah.
    """
    CART = []
    # Proses input buah dan jumlah buah yang akan dibeli
    reorder = None
    while reorder != 'NO':
        # Menampilkan daftar buah yang tersedia
        show(table)

        # Proses memilih buah berdasarkan indeks
        while True:
            id = int_validation('Masukkan Indeks Buah: ')

            if id > len(table)-1:
                print('Indeks buah tidak terdaftar')
                continue
            else:
                index, name, stock, price = list(table.values())[id]

            if id == index:
                break
            
        # Proses menentukan jumlah buah yang dipesan
        while True:
            amount = int_validation('Masukkan Jumlah Buah: ')

            if amount > stock:
                print('Jumlah stock kurang')
                continue
            else:
                CART.append([name, amount, price])
                break
    
        # Menampilkan keranjang belanjaan
        convert_to_table(
            data=CART, 
            columns=['Name', 'Qty', 'Price'],
            title='\nTabel Daftar Belanjaan Anda\n'
        )

        # Meminta konfirmasi ulang apakah akan belanja lagi
        while True:
            confirm = input('Apakah akan order lagi?: ').upper()
            if confirm.isalpha() and confirm in ['YES', 'NO']:
                reorder = confirm
                break
            else:
                print('Silahkan masukkan YES/NO saja!')
                continue
        
        # Update stock buah
        table[name][2] -= amount

    # Menghitung total belanjaan
    for item in CART:
        item.append(item[1] * item[2])
    else:
        convert_to_table(
            data=CART, 
            columns=['Name', 'Qty', 'Price', 'Total'],
            title='\nTabel Daftar Belanjaan Anda\n'
        )
        
    # Proses pembayaran
    totalPrice = sum([item[-1] for item in CART])
    payment(totalPrice)
    

def payment(nominal):
    """Fungsi untuk membayar belanjaan

    Args:
        nominal (int): Jumlah uang yang harus dibayar.
    """
    print(f'Total yang harus Anda bayar: Rp {nominal}')
    while True:
        try:
            # Meminta input uang pembayaran
            bayar = int(input('Silahkan masukkan uang Anda: Rp '))
        except:
            print('Masukkan angka!')
            continue
    
        # Jika uang terpenuhi, hitung sisa
        if bayar >= nominal:
            print(f'Uang kembalian Anda sebesar Rp {bayar - nominal}')
            break
        # Jika tidak, maka hitung kekurangan
        else:
            print(f'\nUang anda kurang sebesar Rp {nominal - bayar}\n')
        