def optimal_change(item_cost, amount_paid):
    change = 100 * (amount_paid - item_cost)
    change_dict = {}
    
    dollars = {
          "one hundred": 10000,
          "fifty": 5000,
          "twenty": 2000,
          "ten": 1000,
          "five": 500,
          "one": 100,
          "quarter": 25,
          "dime": 10,
          "nickel": 5,
          "penny": 1,
          }

    for currency in dollars:
        while change >= dollars[currency]:

          if currency in change_dict:
            change_dict[currency] += 1
          else:
            change_dict[currency] = 1
          change -= dollars[currency]
    
    print(change_dict)

print(optimal_change(44.31, 100))