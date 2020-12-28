# This is a sample Python script.

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows,
# actions, and settings.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print("Hom many k did you run today?")
    kms = input()
    miles = float(kms) / 1.60
    miles = round(miles, 2)
    print(f"You said you ran {kms} kilometers which is {miles} miles")
# See PyCharm help at https://www.jetbrains.com/help/pycharm/
