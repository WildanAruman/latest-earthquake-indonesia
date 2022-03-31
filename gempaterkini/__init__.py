import requests
from bs4 import BeautifulSoup


"""
Method = fungsi
Field/Atribut = variabel

"""
class  GempaTerkini:
    def __init__(self, url):
        self.description = ' to get the latest earthquake in Indonesia from BMKG.go.id'
        self.result = None;
        self.url = url
    def ekstraksi_data(self):
        try:
            content = requests.get(self.url)
        except Exception:
            self.result =  None
        if content.status_code == 200:
            soup = BeautifulSoup(content.text, 'html.parser')
            result = soup.find('span', {'class': 'waktu'})
            result = result.text.split(', ')
            waktu = result[1]
            tanggal = result[0]
            result = soup.find('div', {'class': 'col-md-6 col-xs-6 gempabumi-detail no-padding'})
            result = result.findChildren('li')


            i = 0
            magnitudo = None
            ls = None
            bt = None
            pusat = None
            dirasakan = None
            lokasi = None

            for res in result:
                if i == 1:
                    magnitudo = res.text
                elif i == 2:
                    kedalaman = res.text
                elif i == 3:
                    koordinat = res.text.split(' - ')
                    ls = koordinat[0]
                    bt = koordinat[1]

                elif i == 4:
                    lokasi = res.text

                elif i == 5:
                    dirasakan = res.text

                i = i + 1
            hasil = dict()
            hasil['tanggal'] = tanggal
            hasil['waktu'] = waktu
            hasil['magnitudo'] = magnitudo
            hasil['kedalaman'] = kedalaman
            hasil['koordinat'] = {'ls': ls, 'bt': bt}
            hasil['lokasi'] = lokasi
            hasil['dirasakan'] = dirasakan
            self.result = hasil
        else:
            return None


    def tampilkan_data(self):
        if self.result is None:
            print('Tidak bisa menemukan data gempa terkini')
            return
        print('Gempa terakhir berdasarkan data BMKG')
        print(f"Tanggal, {self.result['tanggal']}")
        print(f"waktu, {self.result['waktu']}")
        print(f"Magnitudo, {self.result['magnitudo']}")
        print(f"kedalaman, {self.result['kedalaman']}")
        print(f"koordinat: {self.result['koordinat']['ls']}, {self.result['koordinat']['bt']}")
        print(f"Lokasi: {self.result['lokasi']}")
        print(f"Dirasakan, {self.result['dirasakan']}")

    def run(self):
        self.ekstraksi_data()
        self.tampilkan_data()


if __name__ == '__main__':
    gempa_di_indeonesia = GempaTerkini('https://bmkg.go.id')

    print('Deskripsi ', gempa_di_indeonesia.description)
    gempa_di_indeonesia.run()



