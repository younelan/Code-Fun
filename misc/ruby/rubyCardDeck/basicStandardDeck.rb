require_relative 'classes/CardGame'

stdGame=CardGame.new(
                :cardNames=>%w[Ace 2 3 4 5 6 7 8 9 10 Jack Queen King],
                :suitNames=>%w[Spades Diamonds Hearts]
                )

#take 3 cards from the deck
card1 = stdGame.pop('deck')
carstdGame = stdGame.pop('deck')
card3 = stdGame.pop('deck')

#insert back the cards
stdGame.push('deck', card3)
stdGame.push('deck', carstdGame)
stdGame.push('deck', card1)

#remove card 3 again using the remove method
stdGame.remove('deck',card3)
print "----\n"

#print the card we took out
print card1.to_s + "/" + carstdGame.to_s + "/" + card3.to_s + "---\n\n"

#try to match all the hearts in the main deck pile
matches= stdGame.getCardsByColumn('deck', 1 , 'H')
print "Matches: " 
print matches
