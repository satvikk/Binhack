def get_max_toys(prices, rupees):
  prices = sorted(prices)
  current_sum = 0
  for i in range(1, len(prices) + 1):
    if current_sum > rupees:
      return i - 1
    current_sum += prices[i]
  return len(prices)

if __name__ == '__main__':
  n, k = map(int, raw_input().split())
  prices = map(int, raw_input().split())
  print get_max_toys(prices, k)
