from typing import Any, Text, Dict, List
from rasa_sdk import Action, Tracker
from rasa_sdk.events import SlotSet, EventType
from rasa_sdk.executor import CollectingDispatcher
import movie_recommender


class ActionMovieName(Action):

    def name(self) -> Text:
        return "action_movie_name"

    def run(self, dispatcher: "CollectingDispatcher",
        tracker: Tracker, domain: Dict
    ) -> List[EventType]:
        movie = next(tracker.get_latest_entity_values("movie"), None)
        if not movie:
            msg = "Ne istediğinizi anlamadım lütfen daha açıklayın"
            dispatcher.utter_message(text=msg)
        # film önerme fonksiyonu ordan da ekrana yansıtma
        top10 = movie_recommender.filme_gore(movie)
        message = "İstediğiniz filme göre önerilerim: \n"
        for oge in top10:
            message += '-' + oge + '\n'
        dispatcher.utter_message(text=message)


class ActionForTheActor(Action):

    def name(self) -> Text:
        return "action_for_the_actor"

    def run(
        self,
        dispatcher: "CollectingDispatcher",
        tracker: Tracker,
        domain: "DomainDict",
    ) -> List[Dict[Text, Any]]:
        actor = next(tracker.get_latest_entity_values("actor"), None)
        if not actor:
            msg = "Ne istediğinizi anlamadım lütfen daha açıklayın"
            dispatcher.utter_message(text=msg)
        # film önerme fonksiyonu ordan da ekrana yansıtma
        oneri_isimleri = movie_recommender.oyuncuya_gore(actor)
        message = "İzlemek istediğiniz oyuncunun oynadığı filmlerden önerilerim: \n"
        for oneri in oneri_isimleri:
            message += '-' + oneri + '\n'
        dispatcher.utter_message(text=message)

class ActionForTheDirector(Action):

    def name(self) -> Text:
        return "action_for_the_director"

    def run(
        self,
        dispatcher: "CollectingDispatcher",
        tracker: Tracker,
        domain: "DomainDict",
    ) -> List[Dict[Text, Any]]:
        director = next(tracker.get_latest_entity_values("director"), None)
        if not director:
            msg = "Ne istediğinizi anlamadım lütfen daha açıklayın"
            dispatcher.utter_message(text=msg)
        # film önerme fonksiyonu ordan da ekrana yansıtma
        oneriler = movie_recommender.yonetmene_gore(director)
        message = "İzlemek istediğiniz yönetmenin yönettiği filmlerden bazı önerilerim: \n"
        for oneri in oneriler:
            message += '-' + oneri + '\n'
        dispatcher.utter_message(text=message)

class ActionForTheGenre(Action):

    def name(self) -> Text:
        return "action_for_the_genre"

    def run(
        self,
        dispatcher: "CollectingDispatcher",
        tracker: Tracker,
        domain: "DomainDict",
    ) -> List[Dict[Text, Any]]:
        genre = next(tracker.get_latest_entity_values("genre"), None)
        if not genre:
            msg = "Ne istediğinizi anlamadım lütfen daha açıklayın"
            dispatcher.utter_message(text=msg)
        # film önerme fonksiyonu ordan da ekrana yansıtma
        oneriler = movie_recommender.ture_gore(genre)
        message = "İzlemek istediğiniz türe göre önerilerim: \n"
        for oneri in oneriler:
            message += '-' + oneri + '\n'
        dispatcher.utter_message(text=message)

class ActionForTheYears(Action):

    def name(self) -> Text:
        return "action_for_the_years"

    def run(
        self,
        dispatcher: "CollectingDispatcher",
        tracker: Tracker,
        domain: "DomainDict",
    ) -> List[Dict[Text, Any]]:
        min_year = next(tracker.get_latest_entity_values("min_year"), None)
        if not min_year:
            msg = "Ne istediğinizi anlamadım lütfen daha açıklayın"
            dispatcher.utter_message(text=msg)
        # film önerme fonksiyonu ordan da ekrana yansıtma
        oneriler = movie_recommender.yila_gore(int(min_year))
        message = "İstediğiniz yıl ve ondan sonra yapılan filmlerden bazı izleyebileceğiniz filmler: \n"
        for oneri in oneriler:
            message += '-' + oneri + '\n'
        dispatcher.utter_message(text=message)

class ActionForTheImdb(Action):

    def name(self) -> Text:
        return "action_for_the_imdb"

    def run(
        self,
        dispatcher: "CollectingDispatcher",
        tracker: Tracker,
        domain: "DomainDict",
    ) -> List[Dict[Text, Any]]:
        imdb = next(tracker.get_latest_entity_values("min_imdb"), None)
        if not imdb:
            msg = "Ne istediğinizi anlamadım lütfen daha açıklayın"
            dispatcher.utter_message(text=msg)
        # film önerme fonksiyonu ordan da ekrana yansıtma
        oneriler = movie_recommender.imdb_puanina_gore(float(imdb))
        message = "Filtrelemeniz üzerine imdb puanı belirttiğiniz üzerinde olan filmlerden bazıları: \n"
        for oneri in oneriler:
            message += '-' + oneri + '\n'
        dispatcher.utter_message(text=message)


class ActionForTheCountry(Action):

    def name(self) -> Text:
        return "action_for_the_country"

    def run(
        self,
        dispatcher: "CollectingDispatcher",
        tracker: Tracker,
        domain: "DomainDict",
    ) -> List[Dict[Text, Any]]:
        country = next(tracker.get_latest_entity_values("country"), None)
        if not country:
            msg = "Ne istediğinizi anlamadım lütfen daha açıklayın"
            dispatcher.utter_message(text=msg)
        # film önerme fonksiyonu ordan da ekrana yansıtma
        oneriler = movie_recommender.ulkeye_gore(country)
        message = "İstediğiniz ülke yapımı olan filmlerden izlemek isteyebileceğinizi düşündüklerim: \n"
        for oneri in oneriler:
            message += '-' + oneri + '\n'
        dispatcher.utter_message(text=message)

class ActionForTheRuntime(Action):

    def name(self) -> Text:
        return "action_for_the_runtime"


    def run(
        self,
        dispatcher: "CollectingDispatcher",
        tracker: Tracker,
        domain: "DomainDict",
    ) -> List[Dict[Text, Any]]:
        runtime = next(tracker.get_latest_entity_values("runtime"), None)
        if not runtime:
            msg = "Ne istediğinizi anlamadım lütfen daha açıklayın"
            dispatcher.utter_message(text=msg)
        # film önerme fonksiyonu ordan da ekrana yansıtma
        oneriler = movie_recommender.film_suresine_gore(float(runtime))
        message = "İstediğiniz dakika ve altında olan filmlerden bazıları: \n"
        for oneri in oneriler:
            message += '-' + oneri + '\n'
        dispatcher.utter_message(text=message)
