#!/usr/bin/python3

def isWinner(x, nums):
  """
  Determines the winner of a prime number game between Maria and Ben.

  Args:
    x: The number of rounds played.
    nums: An array of integers representing the maximum number in each round.

  Returns:
    The name of the player who won the most rounds. If there is no clear winner,
    returns None.
  """

  maria_wins = 0
  ben_wins = 0

  for n in nums:
    # Initialize the set of remaining numbers
    remaining = set(range(1, n + 1))

    # Keep track of the current player
    current_player = "Maria"

    while remaining:
      # Find the smallest prime number in the remaining set
      prime = min(remaining)

      # Remove the prime and its multiples
      remaining -= set(range(prime, n + 1, prime))

      # Switch players
      current_player = "Ben" if current_player == "Maria" else "Maria"

    # Determine the winner of this round
    if current_player == "Maria":
      maria_wins += 1
    else:
      ben_wins += 1

  # Determine the overall winner
  if maria_wins > ben_wins:
    return "Maria"
  elif ben_wins > maria_wins:
    return "Ben"
  else:
    return None
