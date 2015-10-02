#! / usr / bin / python
# -*- coding: utf-8 -*-
"""Register Machine"""
import os
import sys

ARTICLis={}
Dictionari_quantity={}

def insert_product():
    limpiar()
    while True:
        OPTION =raw_input("You want to enter a product? y/n: ")
        if OPTION.isalpha()==True:
            if OPTION.lower()=="y":
                while True:
                    limpiar()
                    product=raw_input("Insert a product: ")
                    product = product.lower()
                    if product.isalpha():
                        break
                    else:
                        print"unrecognized data numeric"
                        
                while True:
                    try:
                        PRICE=float(raw_input("Insert the price of the product: "))
                        ARTICLis[product]=PRICE
                        break
                    except ValueError:
                        print"unrecognized data"
            elif OPTION.lower()=="n":
                break
        else:
            print "their existing articlis  are:"

    for KEY in ARTICLis:
        print KEY,":", "%.2f\t" % (ARTICLis[KEY])
    raw_input("press enter to continue")
    limpiar()
    menu()

def sell_articles():
    ARTICLis2 = []
    if ARTICLis != {}:
        product = "Key"
        for KEY in ARTICLis:
                print KEY,":",ARTICLis[KEY]
        while  True:
            product=raw_input("products that want to take? ")
            product = product.lower()
            ARTICLis2.append(product)
            print "you chose %s"%(product)
            print "Compras: " + str(ARTICLis2)
            if product == "Done" or product == "DONE" or product == "done":
                limpiar()
                TOTAL_PRICE = 0.00
                for i in ARTICLis:
                    CashTotal = float(ARTICLis[i]) * float(ARTICLis2.count(i))
                    unit = ARTICLis2.count(i)
                    print "Price of your " + str(unit) +" "+ i + "(s) is: ""$.""%.2f" %float(CashTotal) +"\n"
                    TOTAL_PRICE += CashTotal
                print ("Sub Total: $. %.2f\t") % TOTAL_PRICE
                #raw_input("press enter to continue")
                if "GOLD" in ARTICLis2 or "gold" in ARTICLis2 or "Gold" in ARTICLis2:
                    gold(TOTAL_PRICE)
                elif "silver" in ARTICLis2 or "Silver" in ARTICLis2 or "SILVER" in ARTICLis2:
                    silver(TOTAL_PRICE)
                elif ("GOLD" in ARTICLis2 or "gold" in ARTICLis2 or "Gold" in ARTICLis2) and ("silver" in ARTICLis2 or "Silver" in ARTICLis2 or "SILVER" in ARTICLis2):
                    gold(TOTAL_PRICE)
                elif ("Gold" != ARTICLis2 and "Silver" != ARTICLis2):
                    any1(TOTAL_PRICE)

    else:
        print "No existing products"
        raw_input("press enter to continue")
        limpiar()
        menu()

def ASD():
    CASH = ""
    while type(CASH) == str:
        try:
            CASH = float(raw_input("CASH :  "))
        except Exception, e:
            pass

    return CASH

def gold(TOTAL_PRICE):
    CASH = 0.00
    print "Gold Card"
    print "The client has a 5%  discount:"
    IVA = TOTAL_PRICE * 0.12
    DISCOUNT = (TOTAL_PRICE*0.05)
    ALLTOTAL = TOTAL_PRICE + IVA - DISCOUNT
    print "_____________________________________________________________"
    j = True
    while j == True:
        CLient_name = raw_input("Client name:  ")
        if CLient_name.isalpha()== True:
            nit = raw_input("NIT: ")
            TOTAIV = TOTAL_PRICE + IVA
            print "_____________________________________________________________"
            print ("Subtotal without iva is: - - - - - - -  %.2f\t") % TOTAL_PRICE
            print ("IVA is:- - - - - - - - - - - - - - - -  %.2f\t") % IVA
            print "_____________________________________________________________"
            print ("SUbtotal with iva is:- - - - - - - - -  %.2f\t") % TOTAIV
            print ("your discount with the card is:- - - -  %.2f\t") % DISCOUNT
            print "_____________________________________________________________"
            print ("Total with card discount:- - - - - - -  %.2f\t") % ALLTOTAL
            CASH = ASD()
            CHANGE = CASH - ALLTOTAL

            print ("CASH:- - - - - - - - - - - - - - - - -  %.2f\t") % CASH
            print "_____________________________________________________________"
            print ("CHANGE:- - - - - - - - - - - - - - - -  %.2f\t" )%CHANGE
            j = False
            print"Thank you for your purchase, come back soon."
            raw_input("press enter to continue")
            limpiar()
            menu()
    

def silver(TOTAL_PRICE):
    CASH = 0.00
    print "Silver Card"
    print "The client has a 2%  discount:"
    IVA = TOTAL_PRICE * 0.12
    DISCOUNT = (TOTAL_PRICE*0.02)
    ALLTOTAL = TOTAL_PRICE + IVA - DISCOUNT
    print "_____________________________________________________________"
    j = True
    while j == True:
        CLient_name = raw_input("Client name:  ")
        if CLient_name.isalpha()== True:
            nit = raw_input("NIT: ")
            TOTAIV = TOTAL_PRICE + IVA
            print "_____________________________________________________________"
            print ("Subtotal without iva is: - - - - - - -  %.2f\t") % TOTAL_PRICE
            print ("IVA is:- - - - - - - - - - - - - - - -  %.2f\t") % IVA
            print "_____________________________________________________________"
            print ("SUbtotal with iva is:- - - - - - - - -  %.2f\t") % TOTAIV
            print ("your discount with the card is:- - - -  %.2f\t") % DISCOUNT
            print "_____________________________________________________________"
            print ("Total with card discount:- - - - - - -  %.2f\t") % ALLTOTAL
            CASH = ASD()
            CHANGE = CASH - ALLTOTAL

            print ("CASH:- - - - - - - - - - - - - - - - -  %.2f\t") % CASH
            print "_____________________________________________________________"
            print ("CHANGE:- - - - - - - - - - - - - - - -  %.2f\t" )%CHANGE
            j = False
            print"Thank you for your purchase, come back soon."
            raw_input("press enter to continue")
            limpiar()
            menu()

def any1(TOTAL_PRICE):
    CASH = 0.00
    print "Only Cash"
    print "The client has a 0%  discount:"
    IVA = (TOTAL_PRICE*0.12)
    ALLTOTAL = TOTAL_PRICE + IVA
    print "_____________________________________________________________"
    j = True
    while j == True:
        CLient_name = raw_input("Client name:  ")
        if CLient_name.isalpha()== True:
            nit = raw_input("NIT: ")
            TOTAIV = TOTAL_PRICE + IVA
            print "_____________________________________________________________"
            print ("Subtotal without iva is: - - - - - - -  %.2f\t") % TOTAL_PRICE
            print ("IVA is:- - - - - - - - - - - - - - - -  %.2f\t") % IVA
            print "_____________________________________________________________"
            print ("SUbtotal with iva is:- - - - - - - - -  %.2f\t") % TOTAIV
            CASH = ASD()
            CHANGE = CASH - TOTAIV

            print ("CASH:- - - - - - - - - - - - - - - - -  %.2f\t") % CASH
            print "_____________________________________________________________"
            print ("CHANGE:- - - - - - - - - - - - - - - -  %.2f\t" )%CHANGE
            j = False
            print"Thank you for your purchase, come back soon."
            raw_input("press enter to continue")
            limpiar()
            menu()

def limpiar():
    os.system("reset")


def salir():
    sys.exit()

def menu():
    whily = True
    while whily == True:
        print "Cash Register"
        print "¿What would you do?"
        print "1.) Insert_product"
        print "2.) Shopping"
        print "3.) Exit"
        opmenu = raw_input("insert numeric of Menu: ")
        limpiar()
        if opmenu.isalpha()==False:
            if opmenu =="1":
                insert_product()
            elif opmenu =="2":
                sell_articles()
            elif opmenu =="3":
                print "Good bye"
                sys.exit()
                whily = False
                break
                whily = False
                break
        elif opmenu != "1"or opmenu != "2" or opmenu != "3": 
            print "enter a valid option"

menu()