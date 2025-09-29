def NULL_not_found(object: any) -> int:
    if object is None:
        print("Nothing:",object, type(object))
        return 0
    if isinstance(float("nan"), type(object)):
        print("Cheese:",object,type(object))
        return 0
    if object is 0:
        print("Zero:",object, type(object))
        return 0
    if object is "":
        print("Empty:",object, type(object))
        return 0
    if isinstance(bool(object), type(object)):
        print("Fake:",object,type(object))
        return 0
    else:
        print("Type not found")
        return 1