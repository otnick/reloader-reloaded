import requests
from bs4 import BeautifulSoup
import time
import winsound

cookies = {
    "OLS_SESSION_ID": "a38dd5fe52fe5d7604f4db631ee5581e",
    "QueueITAccepted-SDFrts345E-V3_tixxfetchallv1": "EventId%3Dtixxfetchallv1%26QueueId%3De93d2bc5-d67b-4b03-9f7c-6381ae74a898%26RedirectType%3Dsafetynet%26IssueTime%3D1715197292%26Hash%3Dff483ca24547b2f46bbccd00354699a59ba68cfbcdb93c79bcaca57b8466a5ff",
    "_abck": "5C2C955462218FA955573499A8E78400~0~YAAQ3u8ZuODZeE2PAQAAgMu5WQtxHQsjIU1WXM+0hwhAnkscVLNt8aJO2F95ykZjeS9k7W35okAJH9GrpbVgmo3HXBLahK4ob/Fsf+SwM6uIevu57xvlMvn0+CXVhJO3ANAIfdkk0ABsLa27jZ2vg6I+l9Hvm+mZAsgDe4zLnKR44nVQx90sw0/bWD1atTsZ2nY/iCEnhfndiunpu7iKvKQHVYUMkP3hdmbW6lYkHrx4+CDBXXQVun1CfwuTsON4GGzZocU6yqhBDjN6UAQQ5J+5X6rXTL3QO3zaUiTDr55Q5K37WXpgCmW3tgaHeom334gaFy9tfkhu5bR6ZS5m+ls4CD4VKd+VgVlRy/dmAxZ8HQRogEJOwyGpB/+cJvuEg7SRIHBD6sBcI7YlGmLx8airg2X9vn1CKGokep0iPuY7dws=~-1~-1~1715200893",
    "ak_bmsc": "A85EC5C5959DFC4BB615CC30C2B04A65~000000000000000000000000000000~YAAQ3u8ZuBz1eE2PAQAA9Ai7WRec5iydKIS7WNS45x+usNdlTH6isyPwCcw6p4UmGq69usE88eX4Yx7jKlN41K39gjTNO5zEq6to99Vc5OYirBgSnyB9ftOMpPpJIJx3GoFQtUzI6DdYBAY6aA5oYxA/qInzn5ShrNpQOihDMqfZVenVE6jP1ttgTXI/ffBsCYFevC4Bmb6BF8Rfe2UPTeoprkD6io8AZdWCvqwIQpE4B6M9zoOuT5UAGalHpMsiojl+/ToxBp7mB5eKnDkIhggxR7gF+KUjIdjH1W5o4wx4LNLKjdQS+JTtE3RViDOC6IuKJjLJJKAhyPrcJZTDY/ZxvpXvrdHEwI6q4Ao3Yucf1nQnNCwyMfOYDDmDNgMy6rO57u1afk9J4evhlw7ilMK8TYLcA8ti7s8tRRxvW4C8KvuOIztMSgz6ApLkCXHBhdt5AV3R5LFoyAOQ5fWvjVkt3ewpPKpSBBGBB6os670aJ/4TsZs4zgCGHNjJX1baki7qV55+U8JciB5NvMPJHcP8pnosqhxlgvOIEU4YxpeNTwFmGoSujotK",
    "bm_mi": "B7009EB729E87FDAEAEA4D03E414E827~YAAQ3u8ZuDfueE2PAQAAQr26WRcJwgZmM03ugS5uPZBUVPoy42c2EU2He7Hpk20GgJiCfg7RW/pBenC0tROIWr4OD6aZai/CVY77b31vwb/XwYGkD6HqERdhjE+UC/YUPoHPScr8mH7NOf/vETCkUc6VuhQC3OSDqSMcAHFV9ivF1xaKFADVqy0DdVxkeY5PGwlihY4U+gA6Cp6+vv87yGHciAb50tOLJ5+oieDe3Vt39rkIdUobw+Rid88GTwQrWGz2cdjQla2IAbjAQjMWk94oVe0aaSB73c/7hclsV+Q5MhQeTSuC27Dtp1J7vHMeQZFRBxdNCepLloJ75rRfs/FzkWZYhvooz3pf/ySu6I/tvXOnmmBbsBPwhrHoweaFMS0lEgDMZHtI80j0fdBbNnfVLDzoweQDqUm8R8xA~1",
    "bm_sv": "B7FDE97FE833179ABEEA46104DADE470~YAAQ3u8ZuKryeE2PAQAAgvO6WRe5HoVCIutTyms1sHTK5yp7WF5CkZduh3bfBE65JFrjoqkE/0kzBMxGlcFWHJ9fEliHZgI+0S81djRbEn+LlgB1eYsuN7qLjkpw8XLeAfEIVRWFjJ4cZZGDPjBPMA1pbL8AQLh8oRRnBr7rGwI5RDk9usHsBmkMhbxrMtEjpkAeURBBb/2Ib7Yq1gy1uBDZeA+33J9ENXwWD8lVE79XAxX6vdE9iGoY/YqLyf/SYpO5ZolrdsLI0myl~1",
    "bm_sz": "6435A2CF6B59B84D7EAF891A19D920FC~YAAQ3u8ZuMoHek2PAQAAZGHGWRdxfP9d4PsTRuNIVD22W/+7qw5FjMpSgJmPZ2NDUYFivXLS2xWA5QukYwbKHPhTziR1GVzhHrsDhHIL/KqOkQtPMdKJO5wOARDRCnebkx4PgIOKaCbrv2u8qFWZHUyLVhm/MtO39Z1v8IQZj+pnAYHl9me9lfWLwGmlgi+OPF0Cagt+L+aRQjMi2QLB/7PDZKYkLrLq3vKEcqBuQDUzd1alpYYt1p0YuFlgR14sS3Oc5CG4dik6VRB4pwLJcwsXW+mgNWBQJFyiyztGJxuujXYA1oSP/h2JKFbF69W0LhH6s2n+2tgAjEYsBS9wMszvU5cQU3r6wnOqqaChOv5I++9XxiM6RC2G/HSfbwy0E1kJ0RdD5PUgXfLLAzN7BEU1iXOjq00dhKdnOdXUOLZzxscKrpI6r00s/61zqc7v2UFRixwS8P/MW4ORNlpYwn4DC0IODk782j2EBZcDVEFDeWxpLIN4c6SiGpxCttUbtBPPCJCzbei2wvoHt7ujs9K4sajLz/vRxzMkRHqlUUz53PabN2dloqjepjxzsr5eTDy/yZg=~3490360~3354690",
    "ols_cookieconsent": "agree"
}

# 'Cookie': 'cookie1=wert1; cookie2=wert2'
CookiesString = '; '.join([f'{key}={value}' for key, value in cookies.items()])

# Funktion zum Abrufen des HTML-Inhalts einer Webseite
def get_webpage_content(url):
    print("Abrufen der Webseite...")
    # fake header, um als Browser zu erscheinen
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'}
    response = requests.get(url, headers=headers, cookies=cookies, timeout=5)
    print(response.status_code)
    if response.status_code == 200:
        return response.text
    else:
        print("Fehler beim Abrufen der Webseite")
        return None

# Funktion zum Vergleichen von zwei HTML-Inhalten
def compare_content(old_content, new_content):
    if old_content == new_content:
        return False
    else:
        return True

# Funktion zum Senden einer Benachrichtigung (z.B. per E-Mail)
def send_notification():
    # Hier implementierst du den Code, um eine Benachrichtigung zu senden
    print("Die Webseite wurde aktualisiert!")
    winsound.Beep(1000, 1000)  # Windows-Sound abspielen

# Hauptfunktion zum Überwachen der Webseite
def monitor_webpage(url, refresh_interval):
    old_content = None

    while True:
        new_content = get_webpage_content(url)
        
        if new_content:
            if old_content is not None:
                if compare_content(old_content, new_content):
                    send_notification()
            old_content = new_content
        
        time.sleep(refresh_interval)

# Beispielaufruf der Hauptfunktion
if __name__ == "__main__":
    url = "https://www.ticket-onlineshop.com/ols/werderbremen/de/einzelkarten/channel/shop/index"  # Hier die zu überwachende Webseite eintragen
    refresh_interval = 10  # Intervall in Sekunden, wie oft die Seite überprüft werden soll
    winsound.Beep(1000, 1000)  # Windows-Sound abspielen
    monitor_webpage(url, refresh_interval)