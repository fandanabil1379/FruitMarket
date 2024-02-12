# Mendefinisikan harga buah
price_apel = 10000
price_jeruk = 15000
price_anggur = 20000

# Mendefinisikan stock buah
stock_apel = 5
stock_jeruk = 10
stock_anggur = 7

# Ucapan pembuka
print('Selamat Datang di Pasar Buah!')

# Mendefinisikan validasi input untuk number
def is_number(value):
    try:
        int(value)
        return True
    except:
        return False

# Mendefinisikan fungsi input buah
def inputBuah(stock, price, name='Apel'):
    """Fungsi untuk meminta jumlah buah dan hitung harga buah

    Args:
        stock (int): Jumlah buah tersisa
        price (int): Harga buah
        name (str, optional): Nama buah yang dipesan. Defaults to 'Apel'.

    Returns:
        int: total harga, dan stock
    """
    while True:
        # Meminta jumlah buah yang dipesan
        qty = input(f'Masukkan jumlah {name}: ')
        # Validasi inputan
        if is_number(qty):
            qty = int(qty)
            # Membandingkan ketersediaan buah dengan pesanan
            if qty > stock:
                print(f'Jumlah pesanan tidak terpenuhi, stock {name} sisa {stock}')
            else:
                break
        else:
            print('Masukkan angka!')

    # Menghitung total harga buah
    totalPrice = qty * price

    # Update stock buah
    stock -= int(qty) 

    return qty, totalPrice, stock

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
                print('\nTerima kasih')
                print(f'Uang kembalian Anda sebesar {bayar - nominal}\n')
                break
            else:
                print(f'\nUang anda kurang sebesar {nominal - bayar}\n')
        else:
            print('Masukkan angka!')

    
# Main program
while True:
    # Hitung harga per buah
    n_apel, total_apel, stock_apel = inputBuah(stock_apel, price_apel, name='Apel')
    n_jeruk, total_jeruk, stock_jeruk = inputBuah(stock_jeruk, price_jeruk, name='Jeruk')
    n_anggur, total_anggur, stock_anggur = inputBuah(stock_anggur, price_anggur, name='Anggur')

    # Menghitung total belanjaan
    total = total_apel + total_jeruk + total_anggur

    # Tampilkan detail belanjaan
    print(f'''\nDetail Belanjaan
        
    Apel : {n_apel} x {price_apel} = {total_apel}
    Jeruk : {n_jeruk} x {price_jeruk} = {total_jeruk}
    Anggur : {n_anggur} x {price_anggur} = {total_anggur}
        
    Total : {total}
    ''')

    # Melakukan pembayaran
    pembayaran(total)

    # Konfirmasi belanja ulang
    konfirmasi = input('Apakah akan melakukan belanja lagi?: ')
    if konfirmasi == 'no':
        break