# Match case Statements:
# Match case satements are like Switch case statemnts in Java
# They take in a value and match it with different cases.
# Default case is execueted if none of the cases are matched. Default case is declared using an underscore (case _:)\

flavor = input("Enter the Falvor:")
flavor = flavor.lower()


match flavor:

    case "vanilla":
        print("You Chose Vanilla!!")

    case "chocolate":
        print("You Chose Chocolate!!")

    case "butterscotch":
        print("You Chose Butterscotch!!")

    case _:
        print("Flavor Out of Stock!!")        