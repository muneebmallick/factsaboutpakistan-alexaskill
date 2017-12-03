# author: Muneeb Mallick

from __future__ import print_function
import random

facts = [
    "Pakistan, officially the Islamic Republic of Pakistan, is a country in South Asia.",
    "It is the world's sixth most populous country with a population of more than 204 million people.",
    "It is the 36th largest country in the world in terms of area, covering 796,095 sq km.",
    "Sialkot, located in Pakistan, is the world's largest producer of handsewn footballs. Local factories in the region produce 40 to 60 million footballs a year, which is roughly 50 to 70% of the world's total production.",
    "Pakistan is the world's first Islamic country to attain nuclear power.",
    "Pakistan has the highest paved international road, The Karakoram Highway ",
    "Pakistan has the largest canal-based irrigation system in the world.",
    "Pakistan has the world's largest ambulance network. Pakistan's Edhi Foundation, which is also listed in the Guinness Book of World Records, operates the network.",
    "Pakistan's estimated population was 201,995,540 in July 2016, making it the world's sixth-most-populous country, behind Brazil and ahead of Nigeria.",
    "The name Pakistan means land of the pure in Persian and Urdu.",
    "Just two people have won the Nobel Prize from Pakistan. They are Malala Yousafzai for Peace in 2014 and Abdus Salam for Physics in 1979.",
    "Karachi, the largest city of Pakistan, is its financial hub as well as home to almost 17 million people. It also has a major seaport.",
    "Pakistan became independent in 1947 from the British Indian Empire.",
    "The Pakistani rupee is the official currency of Pakistan.",
    "Sugarcane juice is the national drink of Pakistan.",
    "Afghanistan, China, India, and Iran share a border with Pakistan.",
    "Pakistan's national language is Urdu, while its official language is English.",
    "The internet is used by 35.835 million people in Pakistan. It occupies position number 27 on the list of the top internet-using countries in the world.",
    "The 'Khewra Salt Mine' in Pakistan is the largest and oldest salt mine in the world.",
    "Pakistan has the only fertile desert in the world, the Tharparkar desert, located in Sindh province.",
    "Pakistan has the eleventh-largest armed force in the world. It has 617,000 people in its army. UN peacekeeping missions are supported largely by the Pakistani army.",
    "According to a survey, Pakistan has one of the world's top national anthem tunes.",
    "Pakistanis are the fourth-most intelligent people in the world, according to poll results gathered from 125 countries by the Institute of European Business Administration.",
    "The world's seventh-largest collection of scientists and engineers is from Pakistan.",
    "Mango is the national fruit of Pakistan, and its national flower is Jasmine.",
    "The Shah Faisal Mosque in Pakistan can accommodate 100,000 worshipers at a time. It was the largest mosque in the world from 1986 until 1993.",
]


# --------------- Helpers that build all of the responses ----------------------

def welcome_build_speechlet_response(title, output, welcome_speech, reprompt_text, should_end_session):
    return {
        'outputSpeech': {
            'type': 'SSML',
            'ssml': "<speak>" + welcome_speech + output + "</speak>"
        },
        'card': {
            'type': 'Simple',
            'title': title,
            'content': output
        },
        'reprompt': {
            'outputSpeech': {
                'type': 'PlainText',
                'text': reprompt_text
            }
        },
        'shouldEndSession': should_end_session
    }


def build_speechlet_response(title, output, reprompt_text, should_end_session):
    return {
        'outputSpeech': {
            'type': 'PlainText',
            'text': output
        },
        'card': {
            'type': 'Simple',
            'title': title,
            'content': output
        },
        'reprompt': {
            'outputSpeech': {
                'type': 'PlainText',
                'text': reprompt_text
            }
        },
        'shouldEndSession': should_end_session
    }


def build_response(session_attributes, speechlet_response):
    return {
        'version': '1.0',
        'sessionAttributes': session_attributes,
        'response': speechlet_response
    }


# --------------- Functions that control the skill's behavior ------------------

def get_welcome_response():
    """ If we wanted to initialize the session to have some attributes we could
    add those here
    """

    session_attributes = {}
    card_title = "Welcome to the Facts about Pakistan Skill by Muneeb Mallick"
    speech_output = "If you're interested in learning more about Pakistan, " \
                    "Please say tell me something interesting"
    # If the user either does not reply to the welcome message or says something
    # that is not understood, they will be prompted again with this text.
    reprompt_text = "Please say tell me a fact about Pakistan"
    should_end_session = False
    return build_response(session_attributes, welcome_build_speechlet_response(
        card_title, speech_output, "Welcome to the Facts about Pakistan Skill created by Muneeb Mallick <break/>", reprompt_text, should_end_session))


def handle_session_end_request():
    card_title = ""
    speech_output = "Thank you for trying the Facts about Pakistan Skill. " \
                    "Have a nice day! "
    # Setting this to true ends the session and exits the skill.
    should_end_session = True
    return build_response({}, build_speechlet_response(
        card_title, speech_output, None, should_end_session))

#import logging

def hasDisplay(context):
    #logging.warning(context)
    if "Display" in context["System"]["device"]["supportedInterfaces"]:
        return True
    else:
        return False


def renderTemplate(content):
    response = {
        "version": "1.0",
        "response": {
            "outputSpeech": {
                "type": "PlainText",
                "text": content["hasDisplaySpeechOutput"]
            },
            "reprompt": {
                "outputSpeech": {
                    "type": "PlainText",
                    "text": content["hasDisplayRepromptText"]
                }
            },
            "card": {
                "type": "Simple",
                "title": content["simpleCardTitle"],
                "content": content["simpleCardContent"]
            },
            "directives": [
                    {
                        "type": "Display.RenderTemplate",
                        "template": {
                            "type": "BodyTemplate2",
                            "title": content["simpleCardTitle"],
                            "textContent": {
                                "primaryText": {
                                    "text": "<font size = '4'><b><br/>" + content["simpleCardContent"] + "</b></font>",
                                    "type": "RichText"

                            #     # "secondaryText": {
                            #     #     "text": "<font size = '1'>Muneeb Mallick</font>",
                            #     #     "type": "RichText"
                            #     # },
                            #     # "tertiaryText":{
                            #     #     "text": "Tertiary Text",
                            #     #     "type": "RichText"
                            #     # }
                                }},
                            "image": {
                                "contentDescription": "Pakistan Flag Background",
                                "sources": [
                                    {
                                        "url": content["image"]
                                    }
                                ]
                            },
                            "backgroundImage": {
                                "contentDescription": "Pakistan Flag Background",
                                "sources": [
                                    {
                                        "url": "https://s3.amazonaws.com/factsaboutpakistanskill/pakistan-2697055_1920.jpg"
                                    }
                                ]
                            }
                        }
                    },
                {
                    "type": "Hint",
                    "hint": {
                        "type": "PlainText",
                        "text": "tell me something interesting about Pakistan"
                    }
                }
                ],
            "shouldEndSession": content["session"]
            },
        "sessionAttributes": content["sessionAttributes"]
    }
    return response

def getfactImage(factNum):
    if factNum == 0:
        factImage = "https://s3.amazonaws.com/factsaboutpakistanskill/map-of-pakistan-news-.jpg"
    elif factNum == 1:
        factImage = "https://s3.amazonaws.com/factsaboutpakistanskill/159530467.jpg"
    elif factNum == 2:
        factImage = "https://s3.amazonaws.com/factsaboutpakistanskill/2.png"
    elif factNum == 3:
        factImage = "https://s3.amazonaws.com/factsaboutpakistanskill/3.jpg"
    elif factNum == 5:
        factImage = "https://s3.amazonaws.com/factsaboutpakistanskill/5.jpg"
    elif factNum == 6:
        factImage = "https://s3.amazonaws.com/factsaboutpakistanskill/6.jpg"
    elif factNum == 7:
        factImage = "https://s3.amazonaws.com/factsaboutpakistanskill/7.jpg"
    elif factNum == 11:
        factImage = "https://s3.amazonaws.com/factsaboutpakistanskill/11.jpg"
    elif factNum == 12:
        factImage = "https://s3.amazonaws.com/factsaboutpakistanskill/12.jpg"
    elif factNum == 13:
        factImage = "https://s3.amazonaws.com/factsaboutpakistanskill/13.jpg"
    elif factNum == 14:
        factImage = "https://s3.amazonaws.com/factsaboutpakistanskill/14.jpg"
    elif factNum == 16:
        factImage = "https://s3.amazonaws.com/factsaboutpakistanskill/16.jpg"
    elif factNum == 18:
        factImage = "https://s3.amazonaws.com/factsaboutpakistanskill/18.jpg"
    elif factNum == 19:
        factImage = "https://s3.amazonaws.com/factsaboutpakistanskill/19.jpg"
    elif factNum == 20:
        factImage = "https://s3.amazonaws.com/factsaboutpakistanskill/20.jpg"
    elif factNum == 24:
        factImage = "https://s3.amazonaws.com/factsaboutpakistanskill/24.jpg"
    elif factNum == 25:
        factImage = "https://s3.amazonaws.com/factsaboutpakistanskill/25.jpg"
    elif factNum in (4,8,9,10):
        factImage = "https://s3.amazonaws.com/factsaboutpakistanskill/flag-1198968_1280.jpg"
    else:
        factImage = "https://s3.amazonaws.com/factsaboutpakistanskill/000.jpg"
    return factImage

def get_fact_about_pakistan(intent, session, context):
    session_attributes = {}
    card_title = "Did you know?"
    reprompt_text = "For another interesting Fact, " \
                    "Please say another one, " \
                    "or tell me something interesting."

    factIndex = random.randint(-1, 25)
    randomFact = facts[factIndex]
    speech_output = randomFact
    should_end_session = False
    factImage = getfactImage(factIndex)

    if hasDisplay(context) is True:
        content = {
            "hasDisplaySpeechOutput": speech_output,
            "hasDisplayRepromptText": reprompt_text,
            "simpleCardTitle": card_title,
            "simpleCardContent": randomFact,
            "image": factImage,
            "session": should_end_session,
            "templateToken": "factBodyTemplate",

            "sessionAttributes": {}
        }
        return renderTemplate(content)

    else:
        return build_response(session_attributes, build_speechlet_response(card_title, speech_output, reprompt_text, should_end_session))


# --------------- Events ------------------

def on_session_started(session_started_request, session):
    """ Called when the session starts """

    print("on_session_started requestId=" + session_started_request['requestId']
          + ", sessionId=" + session['sessionId'])


def on_launch(launch_request, session):
    """ Called when the user launches the skill without specifying what they
    want
    """

    print("on_launch requestId=" + launch_request['requestId'] +
          ", sessionId=" + session['sessionId'])
    # Dispatch to your skill's launch
    return get_welcome_response()


def on_intent(intent_request, session, context):
    """ Called when the user specifies an intent for this skill """

    print("on_intent requestId=" + intent_request['requestId'] +
          ", sessionId=" + session['sessionId'])

    intent = intent_request['intent']
    intent_name = intent_request['intent']['name']

    # Dispatch to your skill's intent handlers
    if intent_name == "GetNewFactIntent":
        return get_fact_about_pakistan(intent, session, context)
    elif intent_name == "AMAZON.HelpIntent":
        return get_welcome_response()
    elif intent_name == "AMAZON.CancelIntent" or intent_name == "AMAZON.StopIntent":
        return handle_session_end_request()
    else:
        raise ValueError("Invalid intent")


def on_session_ended(session_ended_request, session):
    """ Called when the user ends the session.

    Is not called when the skill returns should_end_session=true
    """
    print("on_session_ended requestId=" + session_ended_request['requestId'] +
          ", sessionId=" + session['sessionId'])
    # add cleanup logic here


# --------------- Main handler ------------------

def lambda_handler(event, context):
    """ Route the incoming request based on type (LaunchRequest, IntentRequest,
    etc.) The JSON body of the request is provided in the event parameter.
    """
    print("event.session.application.applicationId=" +
          event['session']['application']['applicationId'])

    """
    Uncomment this if statement and populate with your skill's application ID to
    prevent someone else from configuring a skill that sends requests to this
    function.
    """
    # if (event['session']['application']['applicationId'] !=
    #         "amzn1.echo-sdk-ams.app.[unique-value-here]"):
    #     raise ValueError("Invalid Application ID")

    if event['session']['new']:
        on_session_started({'requestId': event['request']['requestId']},
                           event['session'])

    if event['request']['type'] == "LaunchRequest":
        return on_launch(event['request'], event['session'])
    elif event['request']['type'] == "IntentRequest":
        return on_intent(event['request'], event['session'], event['context'])
    elif event['request']['type'] == "SessionEndedRequest":
        return on_session_ended(event['request'], event['session'])