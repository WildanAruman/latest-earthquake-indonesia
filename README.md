# latest-earthquake-indonesia
This package will get the latest earthquake from BMKG | Indonesian Agency for Meteorological, Climatological and Geophysics 

## HOW IT WORK?
This Package will scrape from [BMKG](https://bmkg.go.id) to get latest Quake happened in Indonesia

Thisa package will use BeatifulSoup4 and Request, to produce output in the form of JSON that is ready to be used in web or mobile application

## HOW TO USE
'''

import gempaterkini



if __name__ == '__main__':
    gempa_di_indeonesia = gempaterkini.GempaTerkini('https://bmkg.go.id')
    print(f'Aplikasi utama menggunkan package yang memiliki deskripsi {gempa_di_indeonesia.description}')

    gempa_di_indeonesia.tampilkan_keterangan()
    gempa_di_indeonesia.run()

'''

