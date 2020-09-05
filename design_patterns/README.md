## Design Patterns

> Alice : Hey Bob, *story* terkait "format wording" buat produk baru kemarin kamu yang mengerjakan, kan? 
>
> Bob : Iya, rencananya sih pengen buat `decorator` baru saja, biar gak mengganggu komponen *existing*. 
> 
> Alice : Oke, ide bagus! kita bisa reuse komponen lama, dan lebih fleksibel juga kan, soalnya ga semua produk harus punya format wording yang sama kaya produk baru ini. 

Berikut adalah percakapan dua orang pemrogram yang sedang membahas fitur baru yang akan mereka kerjakan. Menariknya, disini 
Bob hanya melontarkan kata "*decorator*" dan Alice langsung mengerti apa yang Bob bicarakan. 
 
Selain memberikan cara memecahkan masalah-masalah yang umum terjadi pada saat mengembangkan perangkat lunak, 
*Design Patterns* pada umumnya adalah tentang *intents*, yakni, setiap *patterns* yang dipopulerkan 
oleh "Gang of Four" ini masing-masingnya memiliki tujuan tertentu, 
disertai dengan cara memecahkannya. Yang terpenting, *design patterns* mempermudah 
komunikasi antar *engineers* untuk mendiskusikan keputusan desain dan arsitektur suatu program seperti yang digambarkan di atas.


Design patterns akan sangat berguna hanya jika abstraksi yang kita implementasikan sesuai dengan tujuan aslinya. 
Menurut saya pribadi, design patterns termasuk *"nice to know"* dan sebagai acuan saja, kita selalu bisa merujuk pada *patterns* tersebut apabila 
menemukan masalah yang serupa. 

Tentu saja tidak semua *patterns* akan pasti sesuai diimplementasikan pada masalah spesifik milik kita. 
Lebih baik memiliki *software* yang bekerja dengan baik
dan mudah dipahami daripada *over-engineering* diawal yang nantinya baru disadari ternyata tidak cocok,
kita selalu bisa memikirkan abstraksi yang sesuai nanti jika masalah yang dipecahkan sudah sangat jelas dan matang dipahami :smile:

### Design Patterns in Python
*Design patterns* pada awalnya ditujukan untuk bahasa *statically-typed*, utamanya *Java*. Ada yang beranggapan 
bahwa *design patterns* bahkan tidak diperlukan untuk bahasa pemrograman *dynamically-typed*, seperti Python. Peter Norvig memiliki 
*slides* presentasi yang menunjukkan bahwa [16 dari 23 patterns](https://norvig.com/design-patterns/design-patterns.pdf) 
yang ada pada buku *Design Patterns* dapat disederhanakan dengan 
bahasa pemrograman dinamis. Untuk saya yang belum punya banyak pengalaman, *patterns* sangat berguna, khususnya untuk 
mengkomunikasikan tujuan dan meningkatkan kedisiplinan dalam menulis program karena dibantu dengan cara-cara umum.


### Catalogue
Design patterns dapat dibagi menjadi tiga kategori

| Kategori      | Deskripsi |
| ----------- | ----------- |
| [Behavioral](behavioral/)      | Behavioral design patterns are concerned with algorithms and the assignment of responsibilities between objects.       |
| Creational   | Creational patterns provide various object creation mechanisms, which increase flexibility and reuse of existing code.        |
| structural   | Structural patterns explain how to assemble objects and classes into larger structures while keeping these structures flexible and efficient.        |