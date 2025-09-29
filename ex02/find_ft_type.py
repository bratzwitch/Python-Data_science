def all_thing_is_obj(object: any) -> int:

    if isinstance(object, (list)):
        print("List :",type(object))
    if isinstance(object, (tuple)):
        print("Tuple :",type(object))
    if isinstance(object, (set)):
        print("Set :",type(object))
    if isinstance(object, (dict)):
        print("Dict :",type(object))        
    if isinstance(object, (str)):
        print(object ,"is in kitchen :",type(object))
    if isinstance(object,(int)):
        print("Type not found")
    return 42