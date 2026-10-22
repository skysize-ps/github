def compute_total(prices, discount=0.0):
    """Return the sum of prices minus a percentage discount."""
    return sum(prices) * (1 - discount / 100)
