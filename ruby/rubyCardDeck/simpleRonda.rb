require_relative 'classes/CardGame'


rondaDeck=CardGame.new(:cardValues=> %w[1 2 3 4 5 6 7 10 11 12] , 
                :suitValues => %w[G B C S] , 
                :cardNames=>%w[As Dos Tres Quatro Five Six Seven Sauta Cabal Rey],
                :suitNames=>%w[Gold Black Cups Sticks]
                )


card1 = rondaDeck.pop('deck')
card2 = rondaDeck.pop('deck')
card3 = rondaDeck.pop('deck')

#pushing the cards back, adding a start and end to make it obvious in the printout
rondaDeck.push('deck', 'start')
rondaDeck.push('deck', card3)
rondaDeck.push('deck', card2)
rondaDeck.push('deck', card1)
rondaDeck.push('deck', 'end')
rondaDeck.remove('deck',card3)
print "----\nRemoved cards: "
print card1.to_s + "/" + card2.to_s + "/" + card3.to_s + "---\n\n"

print "\n----\nFull deck: "
print rondaDeck.getPile('deck')

print "\n----\nCards with the value 4: "

matches= rondaDeck.getCardsByColumn('deck', 0 , '4')
print matches
print "\n"