#Create dictionary of shopping lists with list nicknames
shopping_list = {"Target" : ['socks', 'soap', 'detergent', 'sponges '], 
                "Safeway" : ['butter', 'cake', 'cookies', 'bread '], 
                "PeterGrocery" : ['apples', 'organges', 'bananas', 'milk '], 
                "JaneGrocery": ['oreos', 'brownies', 'soda ' ]} 

#Create a menu of options for modifying the shopping lists
menu = {0: "Main Menu", 
        1: "Show all lists", 
        2: "Show a specific list", 
        3: "Add a new shopping list", 
        4: "Add a new item to a shopping list", 
        5: "Remove an item from a shopping list", 
        6: "Remove a list by nickname", 
        7: "Exit when you are done."}




#Code menu options for pulling lists, adding items, removing items, removing lists, etc.

#Code exit option

def show_list():
    pass

def main():
    print menu
    while(True):
        answer = int(raw_input("Please make a numerical selection from the menu. \n"))   
        if answer == 0:
            print menu
        elif answer == 1:
            print shopping_list
        elif answer == 2:
            print shopping_list.keys()
            list_choice = raw_input("Which list do you want to see?")
            print shopping_list[list_choice]
        elif answer == 3:
            new_nickname = raw_input("What nickname would you like to give this list? ")
            shopping_list[new_nickname]= []
        elif answer == 4:
            nickname = raw_input("Which list would you like to append?")
            get_list = shopping_list[nickname]
            new_item = raw_input("Which item would you like to add?")
            get_list.append(new_item)
        elif answer == 5:
            get_item = shopping_list[raw_input("Which list would you like to remove an item from? ")]
            item_removed = raw_input("What item would you like to remove? ")
            get_item.remove(item_removed)
        elif answer == 6:
            remove_nickname()
        elif answer == 7: 
            break


if __name__ == '__main__':
    main()

