#part 1
try:
  # open up the movie review file
  fp = open("movie_reviews.txt", "r")
except:
  print ("Can't open file")
else:
  data = fp.read().lower()
  fp.close()

  # isolate each review
  reviews = data.split("\n")

  # set up a dictionary to hold all of our vocab words
  sentiment = {}

  # visit every line in the file
  for line in reviews:

    score = int(line[0])
    rest = line[2:]

    # isolate each word in the review
    words = rest.split(" ")

    # clean up words
    for w in words:
      clean = ""
      for c in w:
        if c.isalpha():
          clean += c

      # add to dictionary
      if len(clean) > 0:

        # see if this word is in our dictionary
        if clean not in sentiment:
          sentiment[ clean ] = [ score, 1 ]
        else:
          sentiment[ clean ][0] += score
          sentiment[ clean ][1] += 1

  # ask the user for a word
  word = input("Enter a word: ")

  # see if we know about this word
  if word in sentiment:
    print ( word, "has been seen in", sentiment[word][1], "reviews")
    print ("It's average score is:", sentiment[word][0]/sentiment[word][1])
    if sentiment[word][0]/sentiment[word][1] >= 2:
      print ("This is a POSITIVE phrase")
    else:
      print ("This is a NEGATIVE phrase")
  else:
    print ("There is no average score for reviews containing the word", word,"\nCannot determine if this word is positive or negative")

print()
#part 2
import time
try:
  # open up the movie review file
  fp = open("movie_reviews.txt", "r")
except:
  print ("Can't open file")
else:
  data = fp.read().lower()
  fp.close()
  #when the compiling of data starts
  start=time.time()
  # isolate each review
  reviews = data.split("\n")
  
  # set up a dictionary to hold all of our vocab words
  sentiment = {}

  # visit every line in the file
  for line in reviews:

    score = int(line[0])
    rest = line[2:]

    # isolate each word in the review
    words = rest.split(" ")

    # clean up words
    for w in words:
      clean = ""
      for c in w:
        if c.isalpha():
          clean += c

      # add to dictionary
      if len(clean) > 0:

        # see if this word is in our dictionary
        if clean not in sentiment:
          sentiment[ clean ] = [ score, 1 ]
        else:
          sentiment[ clean ][0] += score
          sentiment[ clean ][1] += 1
  #when compiling of data ends
  end=time.time()
  #print statements
  print("Initializing sentiment database\nSentiment database initialization complete")
  #num of unique words analyzed
  print("Total unique words analyzed:", len(sentiment))
  #compute number of seconds it took to complete
  print("Analysis took", format(end-start,".2f"),"seconds to complete")
  
  print()
  # ask the user for a word
  phrase = input("Enter a phrase to test: ")
  #split the words
  words = phrase.split(" ")
  total=0
  good=0
  
  for word in words:
    # see if we know about this word
    clean = ""
    for c in word:
      if c.isalpha():
        clean += c
    #make the word lower
    lower=clean.lower()
    #if it's in sentiment add to the total
    if lower in sentiment:
      #indicate how many times the word has shown up with it's average rating
      print ("* '", lower,"' ", " has been seen in ", sentiment[lower][1], " reviews with an average rating of ", sentiment[lower][0]/sentiment[lower][1], sep="")
      #add the score to the total
      total+=sentiment[lower][0]/sentiment[lower][1]
      #indicate that the word will be factored into calculations
      good+=1
    else:
      #if the word does not have a rating, don't include it into calculations
      print ("* '", lower,"' ", " does not have a rating", sep="")
  #if there is no score, that means we don't have enough data to compute
  if total == 0:
    print("Not enough data to compute sentiment")
  #if the score is positive
  elif total/good >= 2:
    print("Average score for this phrase is", total/good)
    print ("this is a POSITIVE phrase")
  #if the score is negative
  else:
    print("Average score for this phrase is", total/good)
    print ("This is a NEGATIVE phrase")
    
print()
#part 3
#function sentiment_init
#input nothing
#processing from the movie reviews txt file, create a dicttionary
#output return the dictionary
def sentiment_init():
  try:
    fp = open("movie_reviews.txt", "r")
  except:
    print ("Can't open file")
    return
  else:
    #extract the data
    data = fp.read().lower()
    #close the file
    fp.close()
    # isolate each review
    reviews = data.split("\n")
    
    # set up a dictionary to hold all of our vocab words
    sentiment = {}

    # visit every line in the file
    for line in reviews:
      #the score is the first value
      score = int(line[0])
      #the review is the rest
      rest = line[2:]

      # isolate each word in the review
      words = rest.split(" ")

      # clean up words
      for w in words:
        clean = ""
        for c in w:
          if c.isalpha():
            clean += c

        # add to dictionary
        if len(clean) > 0:

          # see if this word is in our dictionary
          if clean not in sentiment:
            sentiment[ clean ] = [ score, 1 ]
          else:
            sentiment[ clean ][0] += score
            sentiment[ clean ][1] += 1
    return sentiment

#function compute_sentiment
#input dictionary and a string
#processing compute whether or not the word is positive or negative
#return the value of the word
def compute_sentiment(dictionary, string):
  #split the string
  words = string.split(" ")
  #accumulate the number of words
  total=0
  #for a word in words
  for word in words:
    #clean up the word
    clean = ""
    for c in word:
      if c.isalpha():
        clean += c
    #make the word lower
    lower=clean.lower()
    #if it's in sentiment add to the total
    if lower in sentiment:
      total+=(dictionary[lower][0]/dictionary[lower][1])
    #it's a neutral word so give it a score of 2
    else:
      total += 2
  #return sentiment score  
  return total/len(words)
sentiment = sentiment_init()
a1 = compute_sentiment(sentiment, "The happy dog and the sad cat")
a2 = compute_sentiment(sentiment, "It made me want to poke out my eyeballs")
a3 = compute_sentiment(sentiment, "I loved this movie!")
a4 = compute_sentiment(sentiment, "Pikachu charmander!!!")

#print (a1, a2, a3, a4)
#scores should look like the following: 2.280133625200816 1.768915591909414 2.07085642181999 2.0
