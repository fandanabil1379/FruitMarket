# Mendefinisikan harga buah
price_apel = 10000
price_jeruk = 15000
price_anggur = 20000

# Mendefinisikan stock buah
stock_apel = 5
stock_jeruk = 10
stock_anggur = 7

while True:

    # Meminta input jumlah apel yang dibeli kepada user
    while True:
        n_apel = int(input('Masukkan jumlah apel: '))
        if n_apel > stock_apel:
            print(f'Jumlah pesanan tidak terpenuhi, stock Apel sisa {stock_apel}')
        else:
            break

    # Meminta input jumlah jeruk yang dibeli kepada user
    while True:
        n_jeruk = int(input('Masukkan jumlah jeruk: '))
        if n_jeruk > stock_jeruk:
            print(f'Jumlah pesanan tidak terpenuhi, stock Jeruk sisa {stock_jeruk}')
        else:
            break

    # Meminta input jumlah anggur yang dibeli kepada user
    while True:
        n_anggur = int(input('Masukkan jumlah anggur: '))
        if n_anggur > stock_anggur:
            print(f'Jumlah pesanan tidak terpenuhi, stock Anggur sisa {stock_anggur}')
        else:
            break

    # Menghitung total belanjaan per buah
    total_apel = n_apel * price_apel
    total_jeruk = n_jeruk * price_jeruk
    total_anggur = n_anggur * price_anggur

    # Menghitung total belanjaan
    total = total_apel + total_jeruk + total_anggur

    # Show
    print(f'''\nDetail Belanjaan
        
    Apel : {n_apel} x {price_apel} = {total_apel}
    Jeruk : {n_jeruk} x {price_jeruk} = {total_jeruk}
    Anggur : {n_anggur} x {price_anggur} = {total_anggur}
        
    Total : {total}
    ''')

    # Melakukan pembayaran
    while True:
        bayar = int(input('Silahkan masukkan uang Anda:'))
        if bayar >= total:
            print('\nTerima kasih')
            print(f'Uang kembalian Anda sebesar {bayar - total}\n')
            break
        else:
            print(f'\nUang anda kurang sebesar {total - bayar}\n')
        
    # Update stock buah
    stock_apel -= n_apel
    stock_jeruk -= n_jeruk
    stock_anggur -= n_anggur

    # Konfirmasi belanja ulang
    konfirmasi = input('Apakah akan melakukan belanja lagi?: ')
    if konfirmasi == 'no':
        break