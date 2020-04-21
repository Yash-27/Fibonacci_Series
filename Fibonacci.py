f1=0
f2=1
z=1
print("f"+"[1]"+"="+str(f1))
print("f"+"[2]"+"="+str(f2))
for i in range(12):
    fn=f1+f2
    f1=f2
    f2=fn
    print("f"+"["+str(i+3)+"]"+"="+str(fn))

print("\U0001F60F")