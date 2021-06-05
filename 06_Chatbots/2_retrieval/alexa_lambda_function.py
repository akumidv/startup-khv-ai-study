# -*- coding: utf-8 -*-

# This sample demonstrates handling intents from an Alexa skill using the Alexa Skills Kit SDK for Python.
# Please visit https://alexa.design/cookbook for additional examples on implementing slots, dialog management,
# session persistence, api calls, and more.
# This sample is built using the handler classes approach in skill builder.
import logging
import ask_sdk_core.utils as ask_utils

from ask_sdk_core.skill_builder import SkillBuilder
from ask_sdk_core.dispatch_components import AbstractRequestHandler
from ask_sdk_core.dispatch_components import AbstractExceptionHandler
from ask_sdk_core.handler_input import HandlerInput

from ask_sdk_model import Response

logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)

import random
import requests

session = dic()


msg_templates_negative = [
            "Это плохо.",
            "Все в порядке, у нас у всех бывают такие дни.",
            "Мне жаль. ",
            "Это очень плохо",
            "Это нормально."
        ]

msg_templates_positive = [
            'Потрясающе.',
            'Рад это слышать!',
            'Замечательно!',
            'Отлично!',
        ]

def welcome():
    """This function generates welcome messages that voice.py functions use to welcome the user."""
    greetings = [
        'Привет,',
        'Доброе утро,',
        'Добрый день,',
        'Здорово,',
        'Рад тебя видеть,',
    ]

    inquires = [
        "Как дела?",
        "Чего делаешь?",
        "Как себя чувствуешь сегодня?",
        "Как себя чувствуешь?",
        "Как ты?",
        "Как дела сегодня?",
        "Как продвигается?",
        "Что у тебя новенького?",
        "Чего расскажешь?",
        "Что нового?",
        "Как здоровье?"
    ]

    welcome = ((random.choice(greetings)) + " " + (random.choice(inquires)))

    print(welcome)
    return (welcome)

def re():
    """This generates the re-prompt phrases that the skill uses if a user has not responded. """
    reprompts = [
        'Ты ещё здесь?',
        'Ты уже ушел?',
        'Ты хочешь чтобы я проверил, что ты здесь?',
        'Привет?',
        'Ты тут?'
    ]

    help_message = "Скажи 'помощь' если нужна поддержка"
    print((random.choice(reprompts)) + " " + (help_message))
    return ((random.choice(reprompts)) + " " + (help_message))

def condolences():
    """This function  generates the condolences used by the voice.py functions when a user responds with something negative"""
    condolences = [
        "Мне жаль это слышать",
        "Мне жаль, что вы не чувствуете себя хорошо",
        "Мне так жаль",
        "Прости, он скоро поправится.",
        "Хорошо, что не идеально.",
        "Это очень плохо",
        "Главное ваши эмоции в это время, и я буду рад помочь вам плечо них.",
        "Я обещаю, она станет лучше.",
        "Мне жаль, но я здесь для вас."
    ]
    print(random.choice(condolences))
    return (random.choice(condolences))


def ideas():

    """This is the function that generates the idea for mood improvement that is offered by various voice.py functions"""

    ideas = [
        "Пойти погулять",
        "Завершить один рутиной",
        "Играть в свою любимую видеоигру",
        "Играть со своим питомцем",
        "Посмотреть фильм",
        "Посмотрите на фотографии с вашего последнего отпуска",
        "Надеть модный наряд",
        "Иди  в магазин",
        "Работа на своем хобби.",
        "Пойти в спортзал",
        "Упражнение",
        "Сделайте 10 отжиманий",
        "Готовим вкусный обед",
        "Пойти за покупками",
        "Занимаюсь йогой",
        "Ремонт что-то около вашего дома",
        "Кататься на велосипеде",
        "Каракули",
        "Нарисовать картину.",
        "Звонок другу и потусоваться.",
        "Иди в свой любимый кафетерий",
        "Перейти по живописной дороге",
        "Сделать новую стрижку",
        "Послушать любимую музыку",
        "Сходить на рыбалку",
        "Смотреть на звезды",
        "Медитировать",
        "Вист музей",
        "Смотреть видео ребенок мопсы",
        "Сделать пазл",
        "Переставить мебель в комнате в вашем доме",
        "Навести порядок в доме",
        "Стирать",
        "Составьте список дел на этой неделе",
        "Приготовьте обед на завтра.",
        "Посмотри в зеркало и скажи себе, что ты потрясающий.",
    ]

    return (random.choice(ideas))


def evaluate_answers():
    """This function evaluates the user's answers to the questions the skill poses if "NegativeFeeling" is called.
    It evaluates the functions in order of usual routine. """
    if session.attributes["Bed"] == "No":
        return "Ладно, давайте начнем с того, что встанем с постели. Вы можете это сделать!"
    elif session.attributes["Eaten"] == "No":
        return "Все в порядке, но ты должен попробовать поесть. Ты сможешь это!"
    elif session.attributes["Showered"] == "No":
        return "Хммм. Может, тебе стоит принять хороший горячий душ? Это поможет вам чувствовать себя лучше."
    elif session.attributes["Dressed"] == "No":
        return "Хорошо. Что ж, давай попробуем одеться. Ты сможешь это сделать!"
    elif session.attributes["Outside"] == "No":
        return "Что ж, давайте попробуем выйти на улицу. Это может быть интересным."
    else:
        return "Это отлично делать все эти вещи. Когда вы в депрессии, такие мелочи могут быть самыми трудными"


class LaunchRequestHandler(AbstractRequestHandler):
    """Handler for Skill Launch."""
    def can_handle(self, handler_input):
        # type: (HandlerInput) -> bool

        return ask_utils.is_request_type("LaunchRequest")(handler_input)

    def handle(self, handler_input):
        # type: (HandlerInput) -> Response
        welcome_text = welcome()
        welcome_re_text = re()

        return (
            handler_input.response_builder
                .speak(welcome_text)
                .ask(welcome_re_text)
                .response
        )


class PositiveFeelingHandler(AbstractRequestHandler):
    """This function is triggered if the PositiveFeeling intent is detected. """
    def can_handle(self, handler_input):
        # type: (HandlerInput) -> bool
        return ask_utils.is_intent_name("PositiveFeeling")(handler_input)

    def handle(self, handler_input):
        # type: (HandlerInput) -> Response
        congrats = [
            'Это так приятно слышать!',
            'Я рад, что ты сегодня хорошо себя чувствуешь',
            'Я рад это слышать.',
            'О, счастливый день!',
            'Потрясающе.',
            'Приятно слышать!',
            'Замечательно!',
            'Отлично!',
            'Я так рад этому!',
            'Это так здорово!'
        ]
        speak_output = random.choice(congrats)
        session["feeling"] = "Good"
        session["State"] = "Question 0 Answered"
        return (
            handler_input.response_builder
                .speak(speak_output)
                # .ask(speak_output)
                .response
        )


class NegativeFeelingHandler(AbstractRequestHandler):
    """This function is triggered if the NegativeFeeling intent is detected. This also kicks off the question to guage
    whether the user has perfomed daily activities."""
    def can_handle(self, handler_input):
        # type: (HandlerInput) -> bool
        return ask_utils.is_intent_name("NegativeFeeling")(handler_input)

    def handle(self, handler_input):
        # type: (HandlerInput) -> Response
        condolence = condolences()
        session.attributes["feeling"] = "Down"
        session.attributes["State"] = "Question 1 Answered"

        speak_output = condolence + "       " + "Ты сегодня встал с постели?"

        return (
            handler_input.response_builder
                .speak(speak_output)
                # .ask(speak_output)
                .response
        )

""" The following functions are called depending on the user's answers."""
class BedYesHandler(AbstractRequestHandler):
    def can_handle(self, handler_input):
        # type: (HandlerInput) -> bool
        return ask_utils.is_intent_name("BedYes")(handler_input)

    def handle(self, handler_input):
        # type: (HandlerInput) -> Response
        message = random.choice(msg_templates_positive)
        session["Bed"] = "Yes"
        session["State"] = "Question 2 Answered"


        speak_output = message + "         " + "Ты сегодня ел?"

        return (
            handler_input.response_builder
                .speak(speak_output)
                # .ask(speak_output)
                .response
        )

class BedNoHandler(AbstractRequestHandler):
    def can_handle(self, handler_input):
        # type: (HandlerInput) -> bool
        return ask_utils.is_intent_name("BedNo")(handler_input)

    def handle(self, handler_input):
        # type: (HandlerInput) -> Response
        message = random.choice(msg_templates_negative)
        session["Bed"] = "No"
        session["State"] = "Question 2 Answered"


        speak_output = message + "         " + "Ты сегодня ел?"

        return (
            handler_input.response_builder
                .speak(speak_output)
                # .ask(speak_output)
                .response
        )
class AteYesHandler(AbstractRequestHandler):
    def can_handle(self, handler_input):
        # type: (HandlerInput) -> bool
        return ask_utils.is_intent_name("AteYes")(handler_input)

    def handle(self, handler_input):
        # type: (HandlerInput) -> Response
        message = random.choice(msg_templates_positive)
        session["Eaten"] = "Yes"
        session["State"] = "Question 3 Answered"


        speak_output = message + "         " + "Ты принмал сегодня душ?"

        return (
            handler_input.response_builder
                .speak(speak_output)
                # .ask(speak_output)
                .response
        )

class AteNoHandler(AbstractRequestHandler):
    def can_handle(self, handler_input):
        # type: (HandlerInput) -> bool
        return ask_utils.is_intent_name("AteNo")(handler_input)

    def handle(self, handler_input):
        # type: (HandlerInput) -> Response
        message = random.choice(msg_templates_negative)
        session["Eaten"] = "No"
        session["State"] = "Question 3 Answered"


        speak_output = message + "         " + "Ты принмал сегодня душ?"

        return (
            handler_input.response_builder
                .speak(speak_output)
                # .ask(speak_output)
                .response
        )

class ShowerYesHandler(AbstractRequestHandler):
    def can_handle(self, handler_input):
        # type: (HandlerInput) -> bool
        return ask_utils.is_intent_name("ShowerYes")(handler_input)

    def handle(self, handler_input):
        # type: (HandlerInput) -> Response
        message = random.choice(msg_templates_positive)
        session["Showered"] = "Yes"
        session["State"] = "Question 4 Answered"


        speak_output = message + "         " + "Ты принмал сегодня душ?"

        return (
            handler_input.response_builder
                .speak(speak_output)
                # .ask(speak_output)
                .response
        )

class ShowerNoHandler(AbstractRequestHandler):
    def can_handle(self, handler_input):
        # type: (HandlerInput) -> bool
        return ask_utils.is_intent_name("ShowerNo")(handler_input)

    def handle(self, handler_input):
        # type: (HandlerInput) -> Response
        message = random.choice(msg_templates_negative)
        session["Showered"] = "No"
        session["State"] = "Question 4 Answered"


        speak_output = message + "         " + "Ты уже оделся?"

        return (
            handler_input.response_builder
                .speak(speak_output)
                # .ask(speak_output)
                .response
        )

class DressedYesHandler(AbstractRequestHandler):
    def can_handle(self, handler_input):
        # type: (HandlerInput) -> bool
        return ask_utils.is_intent_name("DressedYes")(handler_input)

    def handle(self, handler_input):
        # type: (HandlerInput) -> Response
        message = random.choice(msg_templates_positive)
        session["Dressed"] = "Yes"
        session["State"] = "Question 5 Answered"


        speak_output = message + "         " + "Ты принмал сегодня душ?"

        return (
            handler_input.response_builder
                .speak(speak_output)
                # .ask(speak_output)
                .response
        )

class DressedNoHandler(AbstractRequestHandler):
    def can_handle(self, handler_input):
        # type: (HandlerInput) -> bool
        return ask_utils.is_intent_name("DressedNo")(handler_input)

    def handle(self, handler_input):
        # type: (HandlerInput) -> Response
        message = random.choice(msg_templates_negative)
        session["Eaten"] = "No"
        session["State"] = "Question 5 Answered"

        speak_output = message + "         " + "Ты уже оделся?"

        return (
            handler_input.response_builder
                .speak(speak_output)
                # .ask(speak_output)
                .response
        )

class OutsideYesHandler(AbstractRequestHandler):
    def can_handle(self, handler_input):
        # type: (HandlerInput) -> bool
        return ask_utils.is_intent_name("OutsideYes")(handler_input)

    def handle(self, handler_input):
        # type: (HandlerInput) -> Response
        message = random.choice(msg_templates_positive)
        session["Outside"] = "Yes"
        session["State"] = "Suggested"

        if response == "Это отлично делать все эти вещи. Когда вы в депрессии, такие мелочи могут быть самыми трудными.":
            suggestion_inquiry = "Давай попробуем что-нибудь еще, чтобы улучшить твое настроение."
        else:
            suggestion_inquiry = "Вот идея, сделать что-то ещё для улучшения настроения."
            idea = ideas()

        speak_output = message + "      " + suggestion_inquiry + "       " + idea + "          " + "Я надесь, что помог. Ты хочешь еще одно предложение?"

        return (
            handler_input.response_builder
                .speak(speak_output)
                # .ask(speak_output)
                .response
        )

class OutsideNoHandler(AbstractRequestHandler):
    def can_handle(self, handler_input):
        # type: (HandlerInput) -> bool
        return ask_utils.is_intent_name("OutsideNo")(handler_input)

    def handle(self, handler_input):
        # type: (HandlerInput) -> Response
        message = random.choice(msg_templates_negative)
        session["Outside"] = "No"
        session["State"] = "Suggested"
        suggestion_inquiry = "Давай попробуем что-нибудь еще, чтобы улучшить твое настроение."
        idea = ideas()

        speak_output = message + "      " + response + "       " + suggestion_inquiry + "       " + idea + "          " + "Я надесь, что помог. Ты хочешь еще одно предложение?"

        return (
            handler_input.response_builder
                .speak(speak_output)
                # .ask(speak_output)
                .response
        )

""" The following functions handle the built-in Amazon intents based on the session state. """
class NoIntentHandler(AbstractRequestHandler):
    def can_handle(self, handler_input):
        # type: (HandlerInput) -> bool
        return ask_utils.is_intent_name("AMAZON.NoIntent")(handler_input)

    def handle(self, handler_input):
        # type: (HandlerInput) -> Response

        try:
            if session["State"] == "Question 0 Answered":
                return statement("Хорошо. Заходи ко мне ещё раз")
            elif session["State"] == "Question 1 Answered":
                message = random.choice(msg_templates_negative)
                session["State"] = "Question 2 Answered"
                session["Bed"] = "No"
                speak_output = message + "            " + "Вы уже ели сегодня?"
            elif session.attributes["State"] == "Question 2 Answered":
                message = random.choice(msg_templates_negative)

                session["Eaten"] = "No"
                session["State"] = "Question 3 Answered"
                speak_output = message + "            " + "Принимали сегодня душ?"
            elif session.attributes["State"] == "Question 3 Answered":
                message = random.choice(msg_templates_negative)
                session["Showered"] = "No"
                session["State"] = "Question 4 Answered"
                speak_output = message + "            " + "Уже оделись?"
            elif session["State"] == "Question 4 Answered":
                message = random.choice(msg_templates_negative)
                session["Dressed"] = "No"
                session["State"] = "Question 5 Answered"
                speak_output = message + "         " + "Выходили уже сегодня на улицу?"
            elif session["State"] == "Question 5 Answered":
                message = random.choice(msg_templates_negative)

                session["Outside"] = "No"
                session["State"] = "Suggested"
                response = evaluate_answers()
                suggestion_inquiry = "Давайте попробуем что-нибудь ещё, чтобы улучшить ваше настроение."
                idea = ideas()
                speak_output = message + "      " + response + "       " + suggestion_inquiry + "       " + idea + "          " + "Я надеюсь, что помог. Я могу сделать что-нибудь ещё?"
            elif session["State"] == "Suggested":
                session["State"] = "AnythingElse"
                rspeak_output = "Хорошо, я надесюь это помогло. Что нибудь еще я могу сделать?"
            elif session.attributes["State"] == "AnythingElse":
                speak_output = "Никаких проблемы. Приходи ещё. Пока"
            else:
                speak_output = "Я извинясь, но не понял это. Как вы себя чувствуете?"
        except:
            speak_output = "Я извинясь, но не понял это. Как вы себя чувствуете?"
        return (
            handler_input.response_builder
                .speak(speak_output)
                .response
        )

class YesIntentHandler(AbstractRequestHandler):
    def can_handle(self, handler_input):
        # type: (HandlerInput) -> bool
        return ask_utils.is_intent_name("AMAZON.YesIntent")(handler_input)

    def handle(self, handler_input):
        # type: (HandlerInput) -> Response
        try:
            if session["State"] == "Question 0 Answered":
                speak_output = "Хорошо. Чтоя смогу сделать для вас?"

            elif session["State"] == "Question 1 Answered":
                message = random.choice(msg_templates_positive)
                session["Bed"] = "Yes"
                session["State"] = "Question 2 Answered"
                speak_output = message + "         " + "Вы сегодня ели?"

            elif session["State"] == "Question 2 Answered":
                message = random.choice(msg_templates_positive)
                session["Eaten"] = "Yes"
                session["State"] = "Question 3 Answered"
                speak_output = message + "           " + "Вы принимали душ?"

            elif session["State"] == "Question 3 Answered":
                message = random.choice(msg_templates_positive)

                session["Showered"] = "Yes"
                session["State"] = "Question 4 Answered"
                speak_output = message + " " + "Вы уже оделись?"

            elif session["State"] == "Question 4 Answered":
                message = random.choice(msg_templates_positive)

                session["Dressed"] = "Yes"
                session["State"] = "Question 5 Answered"
                speak_output = message + "            " + "Вы уже гуляли сегодня?"

            elif session["State"] == "Question 5 Answered":
                message = random.choice(msg_templates_positive)

                session["Outside"] = "Yes"
                session["State"] = "Suggested"
                response = evaluate_answers()
                if response == "Это отлично делать все эти вещи. Когда вы в депрессии, такие мелочи могут быть самыми трудными.":
                    suggestion_inquiry = "Давайте попробуем что нибудь ещё, чтобы улучшить ваше настроение."
                else:
                    suggestion_inquiry = "Вот еще идея, чтобы улучшить ваше настроение."
                    idea = ideas()
                session["State"] = "AnythingElse"
                speak_output = message + "      " + suggestion_inquiry + "       " + idea + "          " + "Я надеюсь, что помог. Могу что-нибудь ещё сделать?"
            elif session["State"] == "Suggested":
                message = "Хорошо. Вот ещё идя. "
                idea = ideas()
                session["State"] = "Suggested"
                speak_output = message + "       " + idea + "          " + "Вы хотите попробовать ещё одно предложение?"
            elif session["State"] == "AnythingElse":
                speak_output = "Хорошо я люблю помогать. Что я ещё могу сделать для вас. Скажите help если хотите узнать о других могих возможностях."
            else:
                rspeak_output = "Я извинясь, но не понял это. Как вы себя чувствуете? "
        except:
            speak_output = "Я извинясь, но не понял это. Как вы себя чувствуете?"
        return (
            handler_input.response_builder
                .speak(speak_output)
                .response
        )



""" The following functions handle the additional use cases of recommending a therapist, detecting and preventing suicide, and
giving ideas on how to improve the user's mood."""
class SuggestIdeaHandler(AbstractRequestHandler):
    def can_handle(self, handler_input):
        # type: (HandlerInput) -> bool
        return ask_utils.is_intent_name("SuggestIdea")(handler_input)

    def handle(self, handler_input):
        # type: (HandlerInput) -> Response
        suggestion_inquiry = "Вот еще идея, чтобы улучшить ваше настроение."
        idea = ideas()
        session.attributes["State"] = "Suggested"
        speak_output = suggestion_inquiry + "       " + idea + "          " + "Хочешь попробовать ещё одно предложение?"

        return (
            handler_input.response_builder
                .speak(speak_output)
                .response
        )


class HotLineHandler(AbstractRequestHandler):
    def can_handle(self, handler_input):
        # type: (HandlerInput) -> bool
        return ask_utils.is_intent_name("HotLine")(handler_input)

    def handle(self, handler_input):
        # type: (HandlerInput) -> Response
        speak_output = ("""Пожалуйста, не причиняйте вреда ни себе, ни кому-либо еще. Возможно, я просто робот, но я
был создан человеком, который хочет помочь вам и думает, что вы того стоите. Пожалуйста, позвоните в на Горячую линия по
 профилактике по телефону 1-800-273-8255. Они готовы общаться с вами 24 часа в сутки, 7 дней в неделю.""")
        #.standard_card(title='National Suicide Prevention Hot Line', text='Call Now 1-800-273-8255 ', large_image_url='https://upload.wikimedia.org/wikipedia/commons/thumb/4/41/Lifelinelogo.svg/1200px-Lifelinelogo.svg.png')
        return (
            handler_input.response_builder
                .speak(speak_output)
                .response
        )

class FindTherapistHandler(AbstractRequestHandler):
    """This function uses the Google Places API to recommend a therapist based on the user's location. """
    def can_handle(self, handler_input):
        # type: (HandlerInput) -> bool
        return ask_utils.is_intent_name("FindTherapist")(handler_input)

    def handle(self, handler_input):
        # type: (HandlerInput) -> Response
        keyword = "counseling OR therapist OR psychiatrist"
        try:
            address = get_alexa_location()
            logging.debug(address)
            pass
        except:
            logging.error("COULD NOT GET ALEXA LOCATION")
            logging.debug(traceback.format_exc())
            speak_output = """Хмм. Похоже, я не могу найти ваше местоположение. Пожалуйста, разрешите доступ к вашему
местоположение в приложении Alexa и повторите попытку"""
            #.consent_card("read::alexa:device:all:address")
        try:
            gcodeurl = 'https://maps.googleapis.com/maps/api/geocode/json'
            params = {'sensor': 'false', 'address': address}
            gc = requests.get(gcodeurl, params=params, verify=False)
            results = gc.json()['results']
            location = results[0]['geometry']['location']
            location = "{},{}".format(location['lat'], location['lng'])
        except:
            logging.error('ERROR using google geocoder')
            logging.debug(gc.json())
            speak_output = "Извините, у меня сейчас проблемы с этим. Пожалуйста, повторите попытку позже."
            return (
                handler_input.response_builder
                    .speak(speak_output)
                    .response
            )
        print(location)
        key = os.environ['GCLOUD_KEY']
        URL2 = "https://maps.googleapis.com/maps/api/place/textsearch/json?location={}&query={}&key={}".format(location,
                                                                                                               keyword,
                                                                                                               key)
        print(URL2)
        r2 = requests.get(URL2, verify=False)
        if r2.status_code == 200:
            first_output = r2.json()
        else:
            speak_output = "Извините, у меня сейчас проблемы с этим. Пожалуйста, повторите попытку позже."
            return (
                handler_input.response_builder
                    .speak(speak_output)
                    .response
            )
        results = first_output['results']
        idnum = (results[1]['place_id'])
        name = (results[1]['name'])
        # print(results[1])
        # print(idnum)
        URL3 = "https://maps.googleapis.com/maps/api/place/details/json?placeid={}&key={}".format(idnum, key)
        r3 = requests.get(URL3, verify=False)
        if r3.status_code == 200:
            second_output = r3.json()
            phone = (second_output['result'])['international_phone_number']
            # print(second_output)
            # print(phone)
            session["State"] = "Null"
            message = """Я нашел рядом с тобой психотерапевта.
Их имя: {}, а номер: {}. Я добавил их контактную информацию на карточку в приложении Alexa.
Могу ли я еще что-нибудь сделать?""".format(name, phone)
            card = "Name:{} \n Phone:{}".format(name, phone)
            speak_output =  message
                #.standard_card(title="I've found you a possible therapist", text=card, large_image_url="https://images.unsplash.com/photo-1489533119213-66a5cd877091?ixlib=rb-0.3.5&ixid=eyJhcHBfaWQiOjEyMDd9&s=7c006c52fd09caf4e97536de8fcf5067&auto=format&fit=crop&w=1051&q=80")
        else:
            speak_output = "Sorry, I'm having trouble doing that right now. Please try again later."
        return (
            handler_input.response_builder
                .speak(speak_output)
                .response
        )

class HelpIntentHandler(AbstractRequestHandler):
    """Handler for Help Intent."""
    def can_handle(self, handler_input):
        # type: (HandlerInput) -> bool
        return ask_utils.is_intent_name("AMAZON.HelpIntent")(handler_input)

    def handle(self, handler_input):
        # type: (HandlerInput) -> Response
        speak_output = """Есть несколько вещей, которые я могу сделать, чтобы помочь. Я могу порекомендовать терапевта или предложить предложение для
способ улучшить свое настроение. Я также обладаю способностью обнаруживать суицидальные намерения,
но я действительно надеюсь, что вам это не понадобится. """

        return (
            handler_input.response_builder
                .speak(speak_output)
                .response
        )

class CancelOrStopIntentHandler(AbstractRequestHandler):
    """Single handler for Cancel and Stop Intent."""
    def can_handle(self, handler_input):
        # type: (HandlerInput) -> bool
        return (ask_utils.is_intent_name("AMAZON.CancelIntent")(handler_input) or
                ask_utils.is_intent_name("AMAZON.StopIntent")(handler_input))

    def handle(self, handler_input):
        # type: (HandlerInput) -> Response
        speak_output = "Хорошего дня. Я надеюсь скоро получить от вас новости"

        return (
            handler_input.response_builder
                .speak(speak_output)
                .response
        )

class FallbackIntentHandler(AbstractRequestHandler):
    """Single handler for Fallback Intent."""
    def can_handle(self, handler_input):
        # type: (HandlerInput) -> bool
        return ask_utils.is_intent_name("AMAZON.FallbackIntent")(handler_input)

    def handle(self, handler_input):
        # type: (HandlerInput) -> Response
        logger.info("In FallbackIntentHandler")
        speech = "Хм, я не уверен. Вы можете поздороваться или спросить помощи, командой help"
        reprompt = "Я этого не понял. Чем я могу вам помочь?"

        return handler_input.response_builder.speak(speech).ask(reprompt).response

class SessionEndedRequestHandler(AbstractRequestHandler):
    """Handler for Session End."""
    def can_handle(self, handler_input):
        # type: (HandlerInput) -> bool
        return ask_utils.is_request_type("SessionEndedRequest")(handler_input)

    def handle(self, handler_input):
        # type: (HandlerInput) -> Response

        # Any cleanup logic goes here.

        return handler_input.response_builder.response



class CatchAllExceptionHandler(AbstractExceptionHandler):
    """Generic error handling to capture any syntax or routing errors. If you receive an error
    stating the request handler chain is not found, you have not implemented a handler for
    the intent being invoked or included it in the skill builder below.
    """
    def can_handle(self, handler_input, exception):
        # type: (HandlerInput, Exception) -> bool
        return True

    def handle(self, handler_input, exception):
        # type: (HandlerInput, Exception) -> Response
        logger.error(exception, exc_info=True)

        speak_output = "Извините, мне было трудно сделать то, о чем вы просили. Пожалуйста, попробуйте еще раз."

        return (
            handler_input.response_builder
                .speak(speak_output)
                .ask(speak_output)
                .response
        )

# The SkillBuilder object acts as the entry point for your skill, routing all request and response
# payloads to the handlers above. Make sure any new handlers or interceptors you've
# defined are included below. The order matters - they're processed top to bottom.


sb = SkillBuilder()

sb.add_request_handler(LaunchRequestHandler())

sb.add_request_handler(PositiveFeelingHandler())
sb.add_request_handler(NegativeFeelingHandler())
sb.add_request_handler(BedYesHandler())
sb.add_request_handler(BedNoHandler())
sb.add_request_handler(AteYesHandler())
sb.add_request_handler(AteNoHandler())
sb.add_request_handler(ShowerYesHandler())
sb.add_request_handler(ShowerNoHandler())
sb.add_request_handler(DressedYesHandler())
sb.add_request_handler(DressedNoHandler())
sb.add_request_handler(OutsideYesHandler())
sb.add_request_handler(OutsideNoHandler())
sb.add_request_handler(NoIntentHandler())
sb.add_request_handler(YesIntentHandler())
sb.add_request_handler(SuggestIdeaHandler())
sb.add_request_handler(HotLineHandler())
sb.add_request_handler(FindTherapistHandler())

sb.add_request_handler(HelpIntentHandler())
sb.add_request_handler(CancelOrStopIntentHandler())
sb.add_request_handler(FallbackIntentHandler())
sb.add_request_handler(SessionEndedRequestHandler())
sb.add_request_handler(IntentReflectorHandler()) # make sure IntentReflectorHandler is last so it doesn't override your custom intent handlers

sb.add_exception_handler(CatchAllExceptionHandler())

lambda_handler = sb.lambda_handler()
