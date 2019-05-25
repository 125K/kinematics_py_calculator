#!/usr/bin/env python
# -*- coding: utf-8 -*-
def main():
    print("V")
    print("D")
    print("T")

    choice = input ("Please make a choice: ")

    if choice == "V":
        print("V = D / T")
        D = float( input ("D = ") )
        T = float( input ("T = ") )
        print("V = "),
        print(D/T)
    elif choice == "D":
        print("D = V * T")
        V = float( input ("V = ") )
        T = float( input ("T = ") )
        print("D = "),
        print(V*T)
    elif choice == "T":
        print("T = D / V")
        D = float( input ("D = ") )
        V = float( input ("V = ") )
        print("T = "),
        print(D/V)
        print("hours"),
        print( (D/V) * 60 )
        print("minutes")
    else:
        print("I don't understand your choice.")
main()
