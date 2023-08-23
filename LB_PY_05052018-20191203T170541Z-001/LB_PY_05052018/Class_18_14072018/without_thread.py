

def write_file(filename,data):
    fileobj=open(filename,"w")
    for x in range(data):
        fileobj.write(str(x))
        fileobj.write('\n')

    fileobj.close()
    print("\n>>>>>>completed<<<<<<\n")

filename1=input("Enter the file name")
write_file(filename1,1000)

filename2=input("Enter the file name")
write_file(filename2,1000)
