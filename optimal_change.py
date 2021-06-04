def optimal_change(item_cost, amount_paid):
    
    return_str = ""      # creates string that will return information about change (or lack thereof).
    
    
    # converts all dollar amounts into cents, so units are uniform (e.g. $10 == 1000 cents), and finds change; difference of item_cost and amount_paid.
    
    change = 100 * (amount_paid - item_cost) 
    
    change_dict = {}                # blank dictionary created to store change currency and quantity.
    
    dollars = {      
          "$100 bill": 10000,       # currency (keys) listed alongside dollar amounts in cents (values).
          "$50 bill": 5000,
          "$20 bill": 2000,
          "$10 bill": 1000,
          "$5 bill": 500,
          "$1 bill": 100,
          "quarter": 25,
          "dime": 10,
          "nickel": 5,
          "penn": 1,
          }


# assesses whether exact change or insufficient funds are tendered.

    if item_cost > amount_paid:      
        return_str += "Insufficient funds.  Please add money to make a purchase."
    elif item_cost == amount_paid and item_cost > 0:
        return_str += "Thank you for using exact change.  Have a nice day!"
    elif item_cost == amount_paid and item_cost == 0:
        return_str += "Please make a selection."
    else:


# interate through "dollars" dictionary, looking to match currency denomination with corresponding value converted into cents.

        for currency in dollars: 
            while change >= dollars[currency]:    # assessing change on hand with dollars dictionary.
                                                
                if currency in change_dict:       # assessing if currency exists in change_dict.
                    change_dict[currency] += 1   
                else:
                    change_dict[currency] = 1     # addidng to change_dict, accordingly.
                change -= dollars[currency]       # finally, subtract dictionary value used from change.
                
                
        return_str += f"The optimal change for an item that costs ${item_cost} with an amount paid of ${amount_paid} is " # adds to return_str with change information.
          
        for change_amount in change_dict: # iterates through change_dict & adds to string with its value.
            
            if change_dict[change_amount] == 1 and change_amount != "penn":
                return_str += f"{change_dict[change_amount]} {change_amount}, " 
            elif change_dict[change_amount] > 1 and change_amount != "penn":
                return_str += f"{change_dict[change_amount]} {change_amount}s, "
            elif change_dict[change_amount] == 1 and change_amount == "penn":
                return_str += f"and {change_dict[change_amount]} {change_amount}y."
            elif change_dict[change_amount] > 1 and change_amount == "penn":
                return_str += f"and {change_dict[change_amount]} {change_amount}ies."
          
    return return_str # returns constructed string indicating change & subsequent currency denominations.

