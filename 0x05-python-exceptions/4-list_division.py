#!/usr/bin/python3


def list_division(my_list_1, my_list_2, list_length):
    result = []
    for i in range(list_length):
        try:
            if i >= len(my_list_1) or i >= len(my_list_2):
                raise IndexError("Out of range")

            value_1 = my_list_1[i]
            value_2 = my_list_2[i]

            if not (isinstance(value_1, (int, float))
                    and isinstance(value_2, (int, float))):
                raise ValueError("wrong type")

            if value_2 == 0:
                raise ZeroDivisionError("division by 0")

            result.append(value_1 / value_2)
        except ZeroDivisionError:
            print("division by 0")
            result.append(0)
        except ValueError:
            print("wrong type")
            result.append(0)
        except IndexError:
            print("out of range")
            result.append(0)
        finally:
            pass

    return result
