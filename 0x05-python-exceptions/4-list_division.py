#!/usr/bin/python3
def list_division(my_list_1, my_list_2, list_length):
    result = 0
    newlist = []

    for element in range(0, list_length):
        try:
            result = (my_list_1[element] / my_list_2[element])

        except ZeroDivisionError:
            print("division by 0")
            result = 0
        except TypeError:
            print("wrong type")
            result = 0
        except IndexError:
            print("out of range")
            result = 0

        finally:
            newlist.append(result)

    return newlist
