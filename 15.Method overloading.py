def add(datatype,*args):
    if datatype=="int":
        answer=0

    if datatype=="float":
        answer=0.0

    if datatype=="str":
        answer=''

    for x in args:
        answer=answer+x
        print(answer)

print("Integer values")
add("int",25,15)

print("Float values")
add("float",2.0,4.0)

print("String values")
add("str","hello","python")
