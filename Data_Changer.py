student=[]
def write(name):
    name , r = name.split("_")
    if name not in student:
        student.append(name)
        f = open('Frontend\\src\\component\\Dataforface.js','w')     
        f.write("const C = [\n"  )
        student.sort()
        for i in student:
            if i == "Unknown":
                continue
            f.write("\n{ Name : " + '"'+i + '"'+", RollNO : " + r + "},")
        f.write("\n]; export default C")

        f.close()
        
        
