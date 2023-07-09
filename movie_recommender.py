import pandas as pd
from sklearn.metrics.pairwise import cosine_similarity
import random

filmTabanı = pd.read_csv("filmler.csv")
filmTabanı = filmTabanı.drop_duplicates()

isimler = filmTabanı['İsim'].tolist()
türler = filmTabanı['Türler'].str.split("|").tolist()

def kelime_torbası(tür_listesi):
    torba = {}
    for tür in tür_listesi:
        torba[tür] = 1
    return torba

def filme_gore(film):
    # En baştakini tanımadığı için buraya tekrar ekledim düzeltilecek
    from sklearn.metrics.pairwise import cosine_similarity
    kelimeTorbası = [kelime_torbası(film_türleri) for film_türleri in türler]
    tür_df = pd.DataFrame(kelimeTorbası, index=isimler).fillna(0)
    cosine_similarity = cosine_similarity(tür_df)
    similarity_df = pd.DataFrame(cosine_similarity, index=tür_df.index, columns=tür_df.index)
    for i in range(0, len(isimler)):
        if film in isimler[i]:
            print(filmTabanı.iloc[i])
            film_index = i
            top_10 = similarity_df.iloc[film_index].sort_values(ascending=False)[1:11]
            top_10_list = top_10.index.to_series()[top_10.notnull()].tolist()

    return top_10_list

def ture_gore(istenilen_tür):
    istenilen_tür = istenilen_tür.capitalize()
    türTabanı = pd.DataFrame(columns=filmTabanı.columns)
    türlerA = filmTabanı['Türler'].to_list()
    for i in range(len(türlerA)):
        if istenilen_tür in türlerA[i]:
            türTabanı.loc[len(türTabanı)] = filmTabanı.iloc[i]
    del türTabanı['Unnamed: 0']
    filmler = türTabanı['İsim'].tolist()
    length = len(filmler)
    if length <= 10:
        return filmler
    else:
        oneriler = random.sample(filmler, 10)
        return oneriler

def imdb_puanina_gore(min_imdb):
    imdbTabanı = pd.DataFrame(columns=filmTabanı.columns)
    imdbPuanları = filmTabanı['IMDb Puanı'].to_list()
    for i in range(len(imdbPuanları)):
        if min_imdb <= imdbPuanları[i]:
            imdbTabanı.loc[len(imdbTabanı)] = filmTabanı.iloc[i]
    del imdbTabanı['Unnamed: 0']
    filmler = imdbTabanı['İsim'].tolist()
    top_10 = random.sample(filmler, 10)
    return top_10

def yonetmene_gore(istenilen_yönetmen):
    yönetmenTabanı = pd.DataFrame(columns=filmTabanı.columns)
    yönetmenler = filmTabanı['Yönetmen'].to_list()
    for i in range(len(yönetmenler)):
        if istenilen_yönetmen in yönetmenler[i]:
            yönetmenTabanı.loc[len(yönetmenTabanı)] = filmTabanı.iloc[i]
    del yönetmenTabanı['Unnamed: 0']
    filmler = yönetmenTabanı['İsim'].tolist()
    return filmler

def oyuncuya_gore(istenilen_oyuncu):
    oyuncuTabanı = pd.DataFrame(columns=filmTabanı.columns)
    oyuncular = filmTabanı['Oyuncular'].to_list()
    for i in range(len(oyuncular)):
        if istenilen_oyuncu in oyuncular[i]:
            oyuncuTabanı.loc[len(oyuncuTabanı)] = filmTabanı.iloc[i]
    del oyuncuTabanı['Unnamed: 0']
    filmler = oyuncuTabanı['İsim'].tolist()
    return filmler

def film_suresine_gore(max_film_süresi):
    sonFilmSüreleri = []
    süreTabanı = pd.DataFrame(columns=filmTabanı.columns)
    film_süreleri = filmTabanı['Film Süresi'].to_list()
    for filmSüresi in film_süreleri:
        filmSüresi = filmSüresi.replace(' dakika', '')
        filmSüresi = int(filmSüresi)
        sonFilmSüreleri.append(filmSüresi)
    for i in range(len(sonFilmSüreleri)):
        if max_film_süresi <= sonFilmSüreleri[i]:
            süreTabanı.loc[len(süreTabanı)] = filmTabanı.iloc[i]
    del süreTabanı['Unnamed: 0']
    filmler = süreTabanı['İsim'].tolist()
    top_10 = random.sample(filmler, 10)
    return top_10


def yila_gore(min_yil):
    son_yillar = []
    yilTabani = pd.DataFrame(columns=filmTabanı.columns)
    yillar = filmTabanı['Yıl'].tolist()
    for yil in yillar:
        yil = int(yil)
        son_yillar.append(yil)
        for i in range(len(son_yillar)):
            if min_yil <= son_yillar[i]:
                yilTabani.loc[len(yilTabani)] = filmTabanı.iloc[i]
    del yilTabani['Unnamed: 0']
    filmler = yilTabani['İsim'].tolist()
    top_10 = random.sample(filmler, 10)
    return top_10

def ulkeye_gore(istenilen_ülke):
    ulkeTabanı = pd.DataFrame(columns=filmTabanı.columns)
    ulkeler = filmTabanı['Ülke'].to_list()
    for i in range(len(ulkeler)):
        if istenilen_ülke in ulkeler[i]:
            ulkeTabanı.loc[len(ulkeTabanı)] = filmTabanı.iloc[i]
    del ulkeTabanı['Unnamed: 0']
    filmler = ulkeTabanı['İsim'].tolist()
    length = len(filmler)
    if length <= 10:
        return filmler
    else:
        oneriler = random.sample(filmler, 10)
        return oneriler
def random_film():
    import requests
    from bs4 import BeautifulSoup

    top_10 = []
    URL = "https://randommer.io/random-movies"
    page = requests.get(URL).text
    pageText = BeautifulSoup(page, 'lxml')
    boxes = pageText.findAll('div', class_='col-md-3')
    for box in boxes:
        name = box.find('div', class_='caption').text
        top_10.append(name)
    return top_10
