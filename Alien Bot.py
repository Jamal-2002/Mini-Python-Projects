# importing regex and random libraries
import re
import random

class AlienBot:
  # potential negative responses
  negative_responses = ("no", "nope", "nah", "naw", "not a chance", "sorry")
  # keywords for exiting the conversation
  exit_commands = ("quit", "pause", "exit", "goodbye", "bye", "later")
  # random starter questions
  random_questions = (
        "Why are you here? ",
        "Are there many humans like you? ",
        "What do you consume for sustenance? ",
        "Is there intelligent life on this planet? ",
        "Does Earth have a leader? ",
        "What planets have you visited? ",
        "What technology do you have on this planet? "
    )

  def __init__(self):
    self.alienbabble = {'describe_planet_intent': r'.*\s*your planet.*','answer_why_intent': r'why\sare.*','cubed_intent': r'.*cube.*(\d+)'}


  def greet(self):
    self.name = input('Hello there Human! What is your good name?\n ')
    will_help = input(f"Hi {self.name}, I'm Etcetera. I'm not from this planet. Will you help me learn about your planet?.\n")
    if will_help in self.negative_responses:
      print('Ok, have a nice Earth day!')
      return
    self.chat()  



  def make_exit(self, reply):
    for commands in self.exit_commands:
      if commands in reply:
        print('ok, have a nice day! ')
        return False
    return True      


  def chat(self):
    human_reply = input(random.choice(self.random_questions))
    while self.make_exit(human_reply):
      human_reply = input(self.match_reply(human_reply))


  def match_reply(self, reply):
    for intent, regex_pattern in self.alienbabble.items():
        found_match = re.match(regex_pattern, reply)
        
        if found_match:
            if intent == 'describe_planet_intent':
                return self.describe_planet_intent()
            elif intent == 'answer_why_intent':
                return self.answer_why_intent()
            else: # intent is 'cubed_intent', the only other option
                return self.cubed_intent(found_match.groups()[0]) 
    
    # after iterating through all of the options
    # if we haven't returned yet, then none of them worked
    # and there was no match
    return self.no_match_intent()  


  def describe_planet_intent(self):
    responses = ("My planet is a utopia of diverse organisms and species.","I am from Opidipus, the capital of the Wayward Galaxies.")
    return random.choice(responses)


  def answer_why_intent(self):
    responses = ("I come in peace.",
"I am here to collect data on your planet and its inhabitants.",
"I heard the coffee is good.")
    return random.choice(responses)
       

  def cubed_intent(self, number):
    number = int(number)
    cubed_number = number ** 3
    return f"The cube of {number} is {cubed_number}. Isn't that cool? "


  def no_match_intent(self):
    responses = ("Please tell me more.",
                 "Tell me more!",
                 "Why do you say that? ",
                 "I see. Can you elaborate",          "Interesting. Can you tell me more?",  "I see. How do you think?","Why?" ,"How do you think I feel when you say that?")
    return random.choice(responses)

obj = AlienBot()
obj.greet()
