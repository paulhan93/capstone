
import time
from random import seed
from random import randint

CONST_QUOTES = ["Don't lecture me Obi-Wan. I see through the lies of the jedi. -Anakin Skywalker, Star Wars Episode III: Revenge of the Sith (2005)", 
"Assumptions are the mother of all f**k-ups. Under Siege 2 (1995)",
"I choose to run towards my problems and not away from them. Because that's what heroes do. -Thor, Thor Ragnarok (2017)",
"When you run, make sure you run to something not away from something. -The Avett Brothers",
"A calm and humble life will bring more happiness than the pursuit of success and the constant restlessness that comes with it. -Albert Einstein",
"You're doing gods work son. -Unknown",
"Be strong enough to be gentle. -Peter Cullen ",
"Maybe the real treasure was the friends we made along the way. -Unknown",
"I would rather answer a stupid question than fix a stupid mistake. - Unknown" ] 

def random_quote():
    seed(int(round(time.time() * 100)))
    return CONST_QUOTES[randint(0, len(CONST_QUOTES) - 1)]

# Test call:
# print(random_quote())