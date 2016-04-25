from collections import Counter
import operator

def splitinput(filename):
    with open(filename) as handfile:
        games = handfile.read().splitlines()
        games = [game.split() for game in games]
        p1 = [game[:5] for game in games]
        p2 = [game[5:] for game in games]
        return p1,p2

ORDER = ['2','3','4','5','6','7','8','9','T','J','Q','K','A']

def gethandrank(hand):
    hand = [list(card) for card in hand]
    hand.sort(key=lambda val: ORDER.index(val[0]))
    values = list((zip(*hand))[0])
    if all(x[1] == hand[0][1] for x in hand):
        # all same suit
        i = ORDER.index(hand[0][0])
        if values == ORDER[i:i+5]:
            if values[0] == 'T':
                #royal flush
                return 9,values[::-1]
            else:
                #straight flush
                return 8,values[::-1]
        else:
            #flush
            return 5,values[::-1]
    else:
        i = ORDER.index(hand[0][0])
        if values == ORDER[i:i+5]:
            #straight
            return 4,values[::-1]
        else:
            matches = sorted(Counter(values).items(), key=operator.itemgetter(1), reverse=True)
            if matches[0][1] == 4:
                #four of a kind
                comparables = [matches[0][0]]
                comparables.extend(values[::-1])
                return 7,comparables
            elif matches[0][1] == 3 and matches[1][1] == 2:
                #full house
                comparables = [matches[0][0], matches[1][0]]
                comparables.extend(values[::-1])
                return 6,comparables
            elif matches[0][1] == 3:
                #three of a kind
                comparables = [matches[0][0]]
                comparables.extend(values[::-1])
                return 3,comparables
            elif matches[0][1] == 2 and matches[1][1] == 2:
                #two pairs
                comparables = [matches[0][0], matches[1][0]]
                comparables.extend(values[::-1])
                return 2,comparables
            elif matches[0][1] == 2:
                #pair
                comparables = [matches[0][0]]
                comparables.extend(values[::-1])
                return 1,comparables
            else:
                #high card
                return 0,values[::-1]

def findwinner(p1hand, p2hand):
    p1rank,p1vals = gethandrank(p1hand)
    p2rank,p2vals = gethandrank(p2hand)
    # if p1 outranks, win
    if p1rank > p2rank:
        return 1
    elif p1rank < p2rank:
        return 0
    else:
        # go through the order of the cards until a winner is found
        for i in xrange(len(p1vals)):
            if ORDER.index(p1vals[i]) > ORDER.index(p2vals[i]):
                return 1
            elif ORDER.index(p1vals[i]) < ORDER.index(p2vals[i]):
                return 0


if __name__ == "__main__":
    p1,p2 = splitinput("p054_poker.txt")
    p1wins = 0
    for i in xrange(len(p1)):
        p1wins+=findwinner(p1[i],p2[i])
    print p1wins # 376

    
