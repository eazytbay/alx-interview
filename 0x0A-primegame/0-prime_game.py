#!/usr/bin/python3
'''A Prime Game'''


def isWinner(x, nums):
    '''finds the winner'''
    winnerCounter = {'Maria': 0, 'Ben': 0}

    for y in range(x):
        roundWinner = isRoundWinner(nums[y], x)
        if roundWinner is not None:
            winnerCounter[roundWinner] += 1

    if winnerCounter['Maria'] > winnerCounter['Ben']:
        return 'Maria'
    elif winnerCounter['Ben'] > winnerCounter['Maria']:
        return 'Ben'
    else:
        return None


def isRoundWinner(n, x):
    '''find round winner'''
    list = [y for y in range(1, n + 1)]
    players = ['Maria', 'Ben']

    for y in range(n):
        # fetch current player
        currentPlayer = players[y % 2]
        selectedIdxs = []
        prime = -1
        for idx, num in enumerate(list):
            # if a prime number has already been picked then
            # find if it is a multiple of the prime num
            if prime != -1:
                if num % prime == 0:
                    selectedIdxs.append(idx)
            # otherwise, check if num is prime then pick it
            else:
                if isPrime(num):
                    selectedIdxs.append(idx)
                    prime = num
        # if failed to pick then current player lost
        if prime == -1:
            if currentPlayer == players[0]:
                return players[1]
            else:
                return players[0]
        else:
            for idx, val in enumerate(selectedIdxs):
                del list[val - idx]
    return None


def isPrime(n):
    # 0, 1, even numbers greater than 2 are NOT PRIME
    if n == 1 or n == 0 or (n % 2 == 0 and n > 2):
        return False
    else:
        # It is not a prime number if it is divisable by another number less
        # than or equal to the square root of itself.
        # n**(1/2) returns square root of n
        for y in range(3, int(n**(1/2))+1, 2):
            if n % y == 0:
                return "Not prime"
        return True
