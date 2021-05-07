import requests
from bs4 import BeautifulSoup as bs


url = 'https://www.time.ir/'
r = requests.get(url)
soup = bs(r.content, features="lxml")


shamsi_info = soup.find('div', attrs={'id': 'ctl00_cphTop_Sampa_Web_View_TimeUI_ShowDate00cphTop_3734_pnlShamsi'})
shamsi_date = shamsi_info.find('span', attrs={'class': 'show numeral'}).text

miladi_info = soup.find('div', attrs={'id': 'ctl00_cphTop_Sampa_Web_View_TimeUI_ShowDate00cphTop_3734_pnlGregorian'})
miladi_date = miladi_info.find('span', attrs={'class': 'show numeral'}).text


ghamari_info = soup.find('div', attrs={'id': 'ctl00_cphTop_Sampa_Web_View_TimeUI_ShowDate00cphTop_3734_pnlHijri'})
ghamari_date = ghamari_info.find('span', attrs={'class': 'show numeral'}).text

borjfalaki_info = soup.find('div', attrs={'class': 'astrologicalSign'})
borjfalaki_date = borjfalaki_info.find('span', attrs={'class': 'show sign'}).text


azan_sobh = soup.find('span', attrs={'id': 'ctl00_cphTop_Sampa_Web_View_EphemerisUI_EphemerisByCity12cphTop_3736_lblAzanMorning'}).text
tolo_khorshid = soup.find('span', attrs={'id': 'ctl00_cphTop_Sampa_Web_View_EphemerisUI_EphemerisByCity12cphTop_3736_lblAzanSunrise'}).text
azan_zohr = soup.find('span', attrs={'id': 'ctl00_cphTop_Sampa_Web_View_EphemerisUI_EphemerisByCity12cphTop_3736_lblAzanNoon'}).text
ghorob_khorshid = soup.find('span', attrs={'id': 'ctl00_cphTop_Sampa_Web_View_EphemerisUI_EphemerisByCity12cphTop_3736_lblAzanSunset'}).text
azan_maghreb = soup.find('span', attrs={'id': 'ctl00_cphTop_Sampa_Web_View_EphemerisUI_EphemerisByCity12cphTop_3736_lblAzanNight'}).text
nime_shab = soup.find('span', attrs={'id': 'ctl00_cphTop_Sampa_Web_View_EphemerisUI_EphemerisByCity12cphTop_3736_lblMidNight'}).text



print("تاریخ :")
print(f"تاریخ شمسی : {shamsi_date}")
print(f"تاریخ میلادی : {miladi_date}")
print(f"تاریخ قمری : {ghamari_date}")
print(f"برج فلکی : {borjfalaki_date}")

print("اوقات شرعی به افق تهران :")
print(f"اذان صبح : {azan_sobh}")
print(f"طلوع خورشید : {tolo_khorshid}")
print(f"اذان ظهر : {azan_zohr}")
print(f"غروب خورشید : {ghorob_khorshid}")
print(f"اذان مغرب : {azan_maghreb}")
print(f"نیمه شب شرعی : {nime_shab}")
