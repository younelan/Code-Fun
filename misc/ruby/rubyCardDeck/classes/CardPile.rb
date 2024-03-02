##
# this is the base class for all card samples. this is used by the CardGame class under the hood
class CardPile
    ##
    # constructor, supports an optional array of cards to initialize the array
    #
    # example:
	#  suits=%w(A B C)
	#  cards=%w(1 2 3 4 5)
	#  pile=CardPile.new(cards.product(suits))

    def initialize(pileContents = {})
        @@pile = pileContents || {}
    end

    ##
    # return the current state of the deck of cards
    def getDeck
        @@pile
    end

    ##
    # this method returns all cards that match a value for a particular column
    #
    # example:
    #   myPile.getCardsByColumn(1,'H') - returns the hearts 
    #   myPile.getCardsByColumn(0,5) - returns all cards with value 5
    def getCardsByColumn(column,value)
        res=[]
        @@pile.each { |current| 
            if current[column]==value 
                res.push( current ) 
            end
        }
        res
    end

    ##
    # empties the current pile. A typical use scenario is when you want to restart the game
    def clear()
        @@pile={}
    end

    ##
    # add a card to the bottom of the deck
    #
    # example:
    #   myDeck.push(newCard)
    def push(card)
        @@pile.push(card)
    end

    ##
    # removes a card from the bottom of the deck    
    #
    # example:
    #   card1=myDeck.pop()
    def pop()
        @@pile.pop
    end

    ##
    # removes a card to the top of the deck
    #
    # example:
    #   card1=myDeck.shift()
    def shift()
        @@pile.shift
    end

    ##
    # add a card to the top of the deck
    #
    # example:
    #   myDeck.unshift(newCard)
    def unshift(card)
        @@pile.unshift(card)
    end

    ##
    # removes a card from the current deck if it exists
    #
    # example:
    #   myDeck.remove([2,'H'])
    def remove(card)
      @@pile.delete_if {|current| current == card }
    end

    ##
    # shuffle a deck
    #
    # example:
    #   myDeck.shuffle()
    
    def shuffle()
        @@pile=@@pile.shuffle()
    end

end

