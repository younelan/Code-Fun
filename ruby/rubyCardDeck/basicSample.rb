require_relative 'classes/CardPile'

suits=%w(A B C)
cards=%w(1 2 3 4 5)
pile=CardPile.new(cards.product(suits))
print pile.getDeck()