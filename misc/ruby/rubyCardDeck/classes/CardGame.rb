require_relative 'CardPile'

##
# abstraction for a card game
#
class CardGame 

    @@deck=nil
    @@piles=Hash.new
    numPlayers=2
    currentPlayer=1
    cardPointer=0

    ##
    # constructor, supports an optional array of options to customize the deck of cards
    #
    # example:
    #d3=CardGame.new(:cardValues=> %w[W B] , 
    #                :suitValues => %w[S M L] , 
    #                :cardNames=>%w[White Black],
    #                :suitNames=>%w[Small Medium Large]
    #                )
    def initialize(opts = {})
        deckRules={}

        @@cardValues=opts[:cardValues] ||  %w[A 2 3 4 5 6 7 8 9 10 J Q K]
        @@cardNames=opts[:cardNames] ||  @cardValues
        @@suitValues=opts[:suitValues] || %w[S P D H]
        @@suitNames=opts[:suitNames] || @suitValues
        self.reset()
    end

    ##
    # function to return a pile contents
    #
    # example:
    #   myGame.getPile('deck')
    def getPile(pileName)
        if(@@piles.key?pileName)
            @@piles[pileName].getDeck()
        else
            nil
        end
    end

    ##
    # used when you want to restart the game
    def reset()
        @deck=@@cardValues.product(@@suitValues)
        @@piles={}
        @@piles['deck']=CardPile.new(@deck)
        @@piles['deck'].shuffle()
    end

    ##
    # shuffles the current game. generally used at the beginning of the game
    #  
    # example:
    #   myGame.ShuffleDeck()
    def ShuffleDeck
        @@piles['deck'].shuffle()
    end

    ##
    # stub for the method that would deal the cards to the current player
    #
    # example:
    #   myGame.Deal()
    def Deal
    end

    ##
    # returns the current player
    #
    # example:
    #   myGame.getCurrentPlayer()

    def getCurrentPlayer()
        currentPlayer
    end

    ##
    # add a card to the bottom of the deck
    #
    # example:
    #   myGame.push(pile,newCard)
    def push(pile,card)
        @@piles[pile].push(card)
    end

    ##
    # removes a card from the bottom of the deck
    #
    # example:
    #   myGame.push(pile)
    def pop(pile)
        @@piles[pile].pop()
    end

    ##
    # removes a card to the to of pthe deck
    #
    # example:
    #   myGame.push(pile)
    def shift(pile)
        @@piles[pile].shift()
    end

    ##
    # add a card to the top of the deck
    #
    # example:
    #   myGame.push(newCard)
    def unshift(pile,card)
        @@piles[pile].unshift(card)
    end

    ##
    # this method returns all cards that match a value for a particular column
    #
    # example:
    #   myPile.getCardsByColumn('deck',1,'H') - returns the hearts 
    #   myPile.getCardsByColumn('deck',0,5) - returns all cards with value 5
    def getCardsByColumn(pile,column,value)
        @@piles[pile].getCardsByColumn(column,value)
    end

    ##
    # this method returns all cards that match a value for a particular suit
    #
    # example:
    #   myPile.getCardsByColumn('deck','H') - returns the hearts 
    def getCardsBySuit(pile,value)
        @@piles[pile].getCardsByColumn(0,value)
    end

    ##
    # this method returns all cards that match a value for a particular column
    #
    # example:
    #   myPile.getCardsByValue('deck',5) - returns all cards with value 5
    def getCardsByValue(pile,value)
        @@piles[pile].getCardsByColumn(1,value)
    end

    ##
    # this method removes a card from a pile
    #
    # example:
    #   myPile.remove('deck',[5,'H']) - removes the five of hearts in a standard deck
    def remove(pile, card)
      @@piles[pile].remove(card)
    end
end
