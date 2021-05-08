import requests
from bs4 import BeautifulSoup as bs


class Time:
    url = 'https://www.time.ir/'
    r = requests.get(url)
    soup = bs(r.content, features="lxml")

    shamsi = soup.find('div', attrs={'id': 'ctl00_cphTop_Sampa_Web_View_TimeUI_ShowDate00cphTop_3734_pnlShamsi'}).\
        find('span', attrs={'class': 'show numeral'}).text

    miladi = soup.find('div', attrs={'id': 'ctl00_cphTop_Sampa_Web_View_TimeUI_ShowDate00cphTop_3734_pnlGregorian'}).\
        find('span', attrs={'class': 'show numeral'}).text

    ghamari = soup.find('div', attrs={'id': 'ctl00_cphTop_Sampa_Web_View_TimeUI_ShowDate00cphTop_3734_pnlHijri'}).\
        find('span', attrs={'class': 'show numeral'}).text

    borjfalaki = soup.find('div', attrs={'class': 'astrologicalSign'}).\
        find('span', attrs={'class': 'show sign'}).text

    azan_sobh = soup.find('span', attrs={
        'id': 'ctl00_cphTop_Sampa_Web_View_EphemerisUI_EphemerisByCity12cphTop_3736_lblAzanMorning'}).text

    tolo_khorshid = soup.find('span', attrs={
        'id': 'ctl00_cphTop_Sampa_Web_View_EphemerisUI_EphemerisByCity12cphTop_3736_lblAzanSunrise'}).text

    azan_zohr = soup.find('span', attrs={
        'id': 'ctl00_cphTop_Sampa_Web_View_EphemerisUI_EphemerisByCity12cphTop_3736_lblAzanNoon'}).text

    ghrob_khorshid = soup.find('span', attrs={
        'id': 'ctl00_cphTop_Sampa_Web_View_EphemerisUI_EphemerisByCity12cphTop_3736_lblAzanSunset'}).text

    azan_maghreb = soup.find('span', attrs={
        'id': 'ctl00_cphTop_Sampa_Web_View_EphemerisUI_EphemerisByCity12cphTop_3736_lblAzanNight'}).text

    nime_shab = soup.find('span', attrs={
        'id': 'ctl00_cphTop_Sampa_Web_View_EphemerisUI_EphemerisByCity12cphTop_3736_lblMidNight'}).text
