import random

def primary():

  f = open("quotes.txt")
  quotes = f.readlines()
  f.close()

  last = 13
  rnd = random.randint(0, last)
  print(quotes[rnd].rstrip(), quotes[last - rnd].rstrip())

  with open('quotes.txt', 'a') as f:
    f.write(quotes[rnd].rstrip() + quotes[last - rnd].rstrip())

if __name__== "__main__":
  primary()
