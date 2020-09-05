## Strategy Pattern
### Intents 
> Define a family of interchangeable algorithms, Strategy lets the algorithm vary independently from clients that use it.

### Motivation
> Different line-breaking algorithms

### Problem
Suatu saat kita diminta untuk membuat fitur diskon dari aplikasi *billing-payment* yang sedang kita bangun.
Secara bisnis, jika kita mengimplementasikan fitur ini, diprediksikan jumlah transaksi akan meningkat dan pengguna akan lebih 
cenderung melakukan transaksi secara berulang.

Dari *requirements*, ada dua jenis diskon, *fixed* dan *percentage*, dan sangat mungkin akan ada 
jenis diskon lainnya seperti diskon hanya untuk metode pembayaran tertentu, dll. Tanpa pikir panjang, sebagai pemrogram yang cekatan,
langsung saja kita buat implementasi diskon tersebut, lagipula fitur ini harus dirilis sebelum sprint berikutnya. 

```python
def calculate_discount(order):
    discount_amount = 0
    if order is pulsa and order.amount > 50000:
        # calculate discount_amount for fixed discount
    elif order is emoney and order.amount < 20000:
        # calculate discount_amount for percentage discount
    elif order is emoney and order.payment_method is pay_later:
        # calculate amount for pay later with another different percentage discount
    .
    .
    .
    return discount_amount
```

Setelah fitur dirilis, dari sisi bisnis fitur ini dianggap sukses, transaksi meningkat tajam 
dan pengguna bertransaksi berulang sampai beberapa kali setiap minggu. Tetapi dari sisi teknis, 
setiap pemrogram menambahkan tipe diskon baru, `calculate_discount` bertambah ukuran yang akhirnya sangat susah untuk 
dimengerti dan di-*maintain*.

### Solution
*Strategy pattern* menganjurkan kita agar memecah "algoritma" yang berbeda menjadi komponen yang terisolasi, 
sebagai contoh pada file [strategy.py](strategy.py).

Kita dapat dengan mudah menambahkan diskon baru, sebagai contoh :

```python
def harbolnas_discount(order):
    if order.product_name == "Voucher Game":
        return Decimal("10000")
    elif order.product_name == "Voucher Streaming":
        return order.base_price * Decimal("0.50")
```

Tentu saja kita dapat memperluas kemampuan fitur diatas, 
mungkin akan ada *requirement* untuk mengubah jumlah diskon secara dinamis dari *dashboard* operasional? dan mungkin kita 
diharuskan  untuk menyimpan jumlah diskon pada *database*. 
Secara garis besar pattern-nya akan kurang lebih sama, dan sekompleks apapun skema perhitungan diskon nantinya, 
harus terisolasi dalam komponen tersendiri tanpa harus mencampuri `client` yang memanggilnya. 


