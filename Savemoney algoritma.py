class Keuangan:
    def __init__(self):
        self.data_pemasukan = []
        self.data_pengeluaran = []

      def tambah_pemasukan(self, pemasukan):
        self.data_pemasukan.append(pemasukan)
        def add_income(income_list, income_desc_list):
            print("=== PEMASUKAN ===")
            income = float(input("Masukkan pemasukan : Rp."))
            income_desc = input("Keterangan : ")
            income_list.append(income)
            income_desc_list.append(income_desc)
            print("Income added successfully!")

    def tambah_pengeluaran(self, pengeluaran):
        self.data_pengeluaran.append(pengeluaran)

    def bubble_sort(self, data):
        n = len(data)
        for i in range(n - 1):
            for j in range(n - i - 1):
                if data[j] > data[j + 1]:
                    data[j], data[j + 1] = data[j + 1], data[j]

    def urutkan_keuangan(self):
        self.bubble_sort(self.data_pemasukan)
        self.bubble_sort(self.data_pengeluaran)

    def binary_search(self, data, keyword):
        low = 0
        high = len(data) - 1

        while low <= high:
            mid = (low + high) // 2
            if data[mid] == keyword:
                return mid
            elif data[mid] < keyword:
                low = mid + 1
            else:
                high = mid - 1

        return -1

    def cari_pemasukan(self, keyword):
        return self.binary_search(self.data_pemasukan, keyword)

    def cari_pengeluaran(self, keyword):
        return self.binary_search(self.data_pengeluaran, keyword)

    def lihat_data(self):
        print("Data Pemasukan:")
        if len(self.data_pemasukan) > 0:
            for pemasukan in self.data_pemasukan:
                print("Rp.", pemasukan)
        else:
            print("Tidak ada data pemasukan.")

        print("\nData Pengeluaran:")
        if len(self.data_pengeluaran) > 0:
            for pengeluaran in self.data_pengeluaran:
                print("Rp.", pengeluaran)
        else:
            print("Tidak ada data pengeluaran.")


# Menu
keuangan = Keuangan()

while True:
    print("")
    print("=== Aplikasi Pencatat Keuangan ===")
    print("1. Tambah Pemasukan")
    print("2. Tambah Pengeluaran")
    print("3. Urutkan Keuangan")
    print("4. Cari Data Pemasukan")
    print("5. Cari Data Pengeluaran")
    print("6. Lihat Data")
    print("0. Keluar")
    pilihan = input("Masukkan pilihan: ")

    if pilihan == "1":
        pemasukan = input("Masukkan pemasukan : ")
        keuangan.tambah_pemasukan(pemasukan)
        print("Pemasukan berhasil ditambahkan.")

    elif pilihan == "2":
        pengeluaran = input("Masukkan pengeluaran : ")
        keuangan.tambah_pengeluaran(pengeluaran)
        print("Pengeluaran berhasil ditambahkan.")

    elif pilihan == "3":
        keuangan.urutkan_keuangan()
        print("Keuangan berhasil diurutkan.")

    elif pilihan == "4":
        keyword = input("Masukkan kata kunci: ")
        index = keuangan.cari_pemasukan(keyword)
        if index != -1:
            print("Data pemasukan ditemukan pada indeks:", index)
        else:
            print("Data pemasukan tidak ditemukan.")

    elif pilihan == "5":
        keyword = input("Masukkan kata kunci: ")
        index = keuangan.cari_pengeluaran(keyword)
        if index != -1:
            print("Data pengeluaran ditemukan pada indeks:", index)
        else:
            print("Data pengeluaran tidak ditemukan.")

    elif pilihan == "6":
        keuangan.lihat_data()

    elif pilihan == "0":
        print("Terima kasih telah menggunakan aplikasi pencatat keuangan.")
        break

    else:
        print("Pilihan tidak valid. Silakan coba lagi.")
