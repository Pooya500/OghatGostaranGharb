import requests
from bs4 import BeautifulSoup as bs


class Time:
    url = 'https://www.time.ir/'

    def shamsi(self):
        r = requests.get(self.url)
        soup = bs(r.content, features="lxml")

        shamsi_info = soup.find('div',
                                attrs={'id': 'ctl00_cphTop_Sampa_Web_View_TimeUI_ShowDate00cphTop_3734_pnlShamsi'})
        shamsi_date = shamsi_info.find('span', attrs={'class': 'show numeral'}).text
        return shamsi_date

    def miladi(self):
        r = requests.get(self.url)
        soup = bs(r.content, features="lxml")

        miladi_info = soup.find('div',
                                attrs={'id': 'ctl00_cphTop_Sampa_Web_View_TimeUI_ShowDate00cphTop_3734_pnlGregorian'})
        miladi_date = miladi_info.find('span', attrs={'class': 'show numeral'}).text

        return miladi_date

    def ghamari(self):
        r = requests.get(self.url)
        soup = bs(r.content, features="lxml")
        ghamari_info = soup.find('div',
                                 attrs={'id': 'ctl00_cphTop_Sampa_Web_View_TimeUI_ShowDate00cphTop_3734_pnlHijri'})
        ghamari_date = ghamari_info.find('span', attrs={'class': 'show numeral'}).text

        return ghamari_date

    def borjfalaki(self):
        r = requests.get(self.url)
        soup = bs(r.content, features="lxml")
        borjfalaki_info = soup.find('div', attrs={'class': 'astrologicalSign'})
        borjfalaki_date = borjfalaki_info.find('span', attrs={'class': 'show sign'}).text

        return borjfalaki_date

    def azan_sobh(self):
        r = requests.get(self.url)
        soup = bs(r.content, features="lxml")

        azan_sobh = soup.find('span', attrs={
            'id': 'ctl00_cphTop_Sampa_Web_View_EphemerisUI_EphemerisByCity12cphTop_3736_lblAzanMorning'}).text

        return azan_sobh

    def tolo_khorshid(self):
        r = requests.get(self.url)
        soup = bs(r.content, features="lxml")

        tolo_khorshid = soup.find('span', attrs={
            'id': 'ctl00_cphTop_Sampa_Web_View_EphemerisUI_EphemerisByCity12cphTop_3736_lblAzanSunrise'}).text

        return tolo_khorshid

    def azan_zohr(self):
        r = requests.get(self.url)
        soup = bs(r.content, features="lxml")

        azan_zohr = soup.find('span', attrs={
            'id': 'ctl00_cphTop_Sampa_Web_View_EphemerisUI_EphemerisByCity12cphTop_3736_lblAzanNoon'}).text

        return azan_zohr

    def ghrob_khorshid(self):
        r = requests.get(self.url)
        soup = bs(r.content, features="lxml")

        ghorob_khorshid = soup.find('span', attrs={
            'id': 'ctl00_cphTop_Sampa_Web_View_EphemerisUI_EphemerisByCity12cphTop_3736_lblAzanSunset'}).text

        return ghorob_khorshid

    def azan_maghreb(self):
        r = requests.get(self.url)
        soup = bs(r.content, features="lxml")

        azan_maghreb = soup.find('span', attrs={
            'id': 'ctl00_cphTop_Sampa_Web_View_EphemerisUI_EphemerisByCity12cphTop_3736_lblAzanNight'}).text

        return azan_maghreb

    def nime_shab(self):
        r = requests.get(self.url)
        soup = bs(r.content, features="lxml")

        nime_shab = soup.find('span', attrs={
            'id': 'ctl00_cphTop_Sampa_Web_View_EphemerisUI_EphemerisByCity12cphTop_3736_lblMidNight'}).text
        return nime_shab
