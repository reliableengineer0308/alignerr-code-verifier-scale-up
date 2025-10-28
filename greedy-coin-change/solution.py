def greedy_coin_change(coins, amount):
    """
    Compute minimum number of coins to make amount using greedy strategy.
    
    Args:
        coins (List[int]): Sorted list of coin denominations (ascending)
        amount (int): Target amount (non-negative)
    
    Returns:
        int: Minimum coins using greedy selection, or -1 if impossible
    """
    if amount == 0:
        return 0
    if not coins or amount < 0:
        return -1

    # Ensure coins are sorted descending for greedy
    sorted_coins = sorted(coins, reverse=True)
    total_coins = 0

    for coin in sorted_coins:
        if coin > amount:
            continue  # Skip coins larger than remaining amount
        count = amount // coin
        total_coins += count
        amount -= count * coin

    return total_coins if amount == 0 else -1
