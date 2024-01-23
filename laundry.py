import readchar, os
from datetime import date


def main():
    #set default items
    today = date.today()
    items = {"1":{"shirt":1}, "2":{"short":1}}
    final = []
    #display items and number
    display(items)
    count = 0
    back = False
    old = items
    while True:
        count += 1
    #press key and add number and display
        try:
            new = False
            k = readchar.readkey()
            if k.isnumeric():
                if count > 1:
                    old = items
                 #display new item if user wants to
                if int(k) == (len(items.keys()) + 1):

                    add_new(items,k)
                    if add_new == False:
                        continue
                    new=True
                else:
                    add_quant(items,k)
                    new = True
            elif k == readchar.key.BACKSPACE:
                back = True
                items = old
            elif k == readchar.key.ENTER:
                ans = input("are you sure? y/n ")
                if ans == 'n':
                    continue
                else:
                    break
            if new:
                #display items and number
                os.system('cls')
                display(items)
                if k.isnumeric():
                    for key,value in items[k].items():
                        print(f"1 added to {key}")
                        prev_add =key
                        prev_key = k
            elif back == True:
                os.system('cls')
                sub_quant(items, prev_key)
                back = False
                display(items)
                print(f"1 subtracted from {prev_add}")


        except KeyError:
            pass

    laundry_file = open("Laundry_list.txt", 'w')
    laundry_file.write(today.strftime("%B %d, %Y\n"))
    for k in items.keys():
        for key,value in items[k].items():
            print(f"appending {key} to list...")
            laundry_file.write(f"{key} : {value}\n")
    
    laundry_file.close()
            
    #write to file
    #save to directory

    
    




def display(d):
    for n, item in d.items():
        for name in item:
            print(f'{n} ' +name, item[name], sep =":")

def add_quant(d,k):
    for key, value in d[k].items():
        d[k].update({key:value+1})
    return

def sub_quant(d,k):
    for key, value in d[k].items():
        d[k].update({key:value-1})

def add_new(d,k):
    print ("press enter to continue")
    word = input()
    if word.strip() == '':
        return False
    else:
        item = {word:1}
        new_num = str(len(d)+1)
        d.update({new_num:item})

main()
