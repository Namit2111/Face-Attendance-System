student=[]
def write(name):
    print(name)
    name , r = name.split("_")
    if name not in student:
        student.append(name)
        f = open('Frontend\\my-app\\src\\Dataforface.js','w')     
        f.write("const C = [\n"  )
        student.sort()
        for i in student:
            if i == "Unknown":
                continue
            f.write("\n{ Name : " + '"'+i + '"'+", RollNO : " + r + "},")
        f.write("\n]; export default C")

        f.close()
        
        
