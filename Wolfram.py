# -*- coding: utf-8-*-
import random
import re
import wolframalpha
import time
import sys
from sys import maxint


WORDS = ["WHO", "WHAT", "HOW MUCH", "HOW MANY", "HOW OLD"]


def handle(text, mic, profile):
    app_id = profile['keys']['WOLFRAMALPHA']
    client = wolframalpha.Client(app_id)

    mic.say("Wolfram Alpha know it...")
    query = client.query(text)
    if len(query.pods) > 0:
        texts = ""
        pod = query.pods[1]
        if pod.text:
            texts = pod.text
        else:
            texts = "I can not find anything"

        mic.say(texts.replace("|", ""))
    else:
        mic.say("Sorry, Could you be more specific?.")


def isValid(text):
    return any(p.lower() in text.lower() for p in WORDS)
