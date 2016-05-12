__author__ = 'SKings'

table = input("Enter your table name: ");
print ("Your table name  is : ", table)

paramline = input("Enter all parameter split them with ',' \nuse '#' for make increment number\n")
parameters = [x.strip() for x in paramline.split(',')]

for i in range(0, parameters.__len__()):
    print("parameter(", i, ")) => ", parameters[i])

result = "";
repeat = input("insert number of repeat : ");
repeat = int(repeat)

for i in range(0, repeat):
    result += 'insert into '+table+" values("

    for j in range(0, parameters.__len__()):
        result += parameters[j].replace("#", str(i))
        result += ","

    result = result[:-1]
    result += ");\n"
result = result[:-1]

print("this result save to output ***************")
print(result)
print()


output = input("insert output file dir witout(.txt) : ")
fileOutput = open(output+".txt", "w+")
fileOutput.write(result);
fileOutput.close();