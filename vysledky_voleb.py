"""
projekt_3.py: třetí projekt do Engeto Online Python Akademie
author: Jakub Havel
email: havel8jakub@seznam.cz
discord: Kuba H.#6482
"""
from requests import get
from bs4 import BeautifulSoup as bs
import re
import csv
import sys

def ocisti_ciselne(cislo_se_znaky):
    '''
    vytahuje z tagů potřebné číselné hodnoty
    '''
    atr_obec = re.compile(">(.{1,15})<")
    obec_se_znaky = atr_obec.findall(cislo_se_znaky)
    ciste_cislo = "".join(obec_se_znaky).replace("\xa0", " ")
    return str(ciste_cislo)

def najdi_obec(obec_k_ocisteni):
    '''
       vytahuje z tagů názvy obcí
       '''
    atr_obec = re.compile(" .{1,50}")
    obec_se_znaky = atr_obec.findall(obec_k_ocisteni)
    obec = "".join(obec_se_znaky).strip()
    return obec
def najdi_stranu (strana_k_ocisteni):
    '''
       vytahuje z tagů názvy stran
       '''
    atr_obec = re.compile(">(.*?)<")
    strana_se_znaky = atr_obec.findall(strana_k_ocisteni)
    cista_strana = "".join(strana_se_znaky)
    return cista_strana
def novy_odkaz (puvodni, pulodkaz):
    '''
       kompletuje odkazy pro vyhledávání údajů o hlasování v každé obci zvlášť
       '''
    novy_odkaz = re.sub("ps3.{1,60}",pulodkaz, puvodni)
    return novy_odkaz

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Nesprávný počet argumentů.")
        print("UKONCUJI electin-scraper")

    elif ".csv"  not in sys.argv[2]:
        print("Druhý argument není ve formátu .csv")

    elif len(sys.argv) == 3:
        try:
            adresa = (sys.argv[1])
            print("STAHUJI DATA Z VYBRANEHO URL:", (adresa))
            odpoved = get(adresa)
            rozdeleni_html= bs(odpoved.text, features= "html.parser")

            odkazy_cs=[]
            odkazy=[]
            for td in rozdeleni_html.find_all("td", "cislo"):
                odkaz =  td.a["href"]
                odkazy.append(odkaz)

            for td in rozdeleni_html.find_all("td", "cislo"):
                odkaz =  td.a["href"]
                odkazy_cs.append(novy_odkaz(adresa,odkaz))


            obce_full=[]
            hlavicka=["code", "location","registred", "envelopes", "valid"]
            odkaz_pro_hlavicku = (odkazy_cs[0])
            pro_hlavicku= get(odkaz_pro_hlavicku)
            html_hlavicka= bs(pro_hlavicku.text, features= "html.parser")
            for strany_1 in html_hlavicka.find_all("td", headers="t1sa1 t1sb2"):
                hlavicka.append(najdi_stranu(str(strany_1)))
            for strany_2 in html_hlavicka.find_all("td", headers="t2sa1 t2sb2"):
                hlavicka.append(najdi_stranu(str(strany_2)))
            hlavicka = [item.replace(",", "/") for item in hlavicka]
            obce_full.append(hlavicka)


            for odkaz in odkazy_cs:
                cista = get(odkaz)
                c_html= bs(cista.text, features= "html.parser")
                volici_v_seznamu=[]
                cislo = re.compile("\d{6}")
                cislo_obce = cislo.findall(odkaz)
                cislo_d = "".join(cislo_obce)
                volici_v_seznamu.append(cislo_d)

                for mesta in c_html.select("#publikace > h3:nth-child(4)"):
                    volici_v_seznamu.append(najdi_obec(str(mesta)))

                for volici in c_html.find_all("td", headers="sa2"):
                    volici_v_seznamu.append(ocisti_ciselne(str(volici)))

                for obalky in c_html.find_all("td", headers="sa3"):
                    volici_v_seznamu.append(ocisti_ciselne(str(obalky)))

                for hlasy in c_html.find_all("td", headers="sa6"):
                    volici_v_seznamu.append(ocisti_ciselne(str(hlasy)))

                for hlasy_pro_stranu_1 in c_html.find_all("td", headers="t1sa2 t1sb3"):
                    volici_v_seznamu.append(ocisti_ciselne(str(hlasy_pro_stranu_1)))

                for hlasy_pro_stranu_2 in c_html.find_all("td",headers="t2sa2 t2sb3") :
                    volici_v_seznamu.append(ocisti_ciselne(str(hlasy_pro_stranu_2)))
                obce_full.append(volici_v_seznamu)

            with open((sys.argv[2]), 'w', newline='') as file:
                print("UKLADAM DO SOUBORU:", (sys.argv[2]))
                writer = csv.writer(file, dialect='excel-tab')
                writer.writerows(obce_full)

            print("UKONCUJI electin-scraper")

        except Exception:
            print("Nejméně jeden argument byl zadán chybně.")
            print("UKONCUJI electin-scraper")



    else:
        print("Nesprávný počet argumentů.")
        print("UKONCUJI electin-scraper")


