#Coffee Chatbot
#But first, coffee.

#Whether it’s to get us ready to jump-start our day or to get us through a late-night cram session, many of us need our regular caffeine fix! Ordering coffee is just one example of a process that can be automated with the help of a chatbot.

#The task is creating a Python chatbot that can help cut the wait time of a normal coffee run by taking customers’ orders in advance



def coffee_bot():
  print("Welcome to the cafe!")
  size = get_size()
  drink_type = drink_order()
  if drink_type == 'Latte':
    milk = order_latte()
    return("Alright that's a {} {} with {}!".format(size,drink_type,milk))

  return("Alright that's a {} {}!".format(size,drink_type))

def print_message():
  return "I'm sorry, I did not understand your selection. Please enter the corresponding letter for your response."


def get_size():
  res = input('What size drink can I get for you? \n[a] Small \n[b] Medium \n[c] Large \n> ')
  res = res.lower()
  if res == 'a':
    return 'Small'
  elif res == 'b':
    return 'Medium'
  elif res == 'c':
    return 'Large' 
  else: 
    print (print_message())
    get_size()     

def drink_order():
  res = input('''What type of drink would you like?
[a] Brewed Coffee
[b] Mocha
[c] Latte \n''')
  res = res.lower()
  if res == 'a':
    return 'Brewed Coffee'
  elif res == 'b':
    return 'Mocha'
  elif res  == 'c':
    return 'Latte'
  else:
    print(print_message())
    drink_order()      


def order_latte():
  res = input('''And what kind of milk for your latte?
[a] 2% milk
[b] Non-fat milk
[c] Soy milk \n''')
  res = res.lower()
  if res == 'a':
    return '2% milk'
  elif res == 'b':
    return 'Non-fat milk'
  elif res == 'c':
    return 'Soy milk'
  else:
    print(print_message())
    order_latte  

print(coffee_bot())
