from sys import argv

script , filename=argv

print(f"We're going to erase {filename}.")
print("if you don't want that,hit CTRL-F(^C).")
print("if you do want that, hit RETURN")

input("?")

print("opening the file...")
target=open(filename,"w")

print("truncating the file. goodbye.")
target.truncate()

print("now i'm going to ask you for three lines.")

line1=input("line 1:")
line2=input("line 2:")
line3=input("line 3:")

print("i'm going to write these to the file.")

q="\n"
target.write(line1+q+line2+q+line3+q)

print("And finally, we close it.")
target.close()



