def read_persons_file(filename):
    try:
        #1.read and open file
        with open(filename) as file:
            file2 = file.read().split("\n")

        appear = []
        persons = []
        #2.convert file to matrix
        for i in range(len(file2)):
            new = []
            file2[i] = file2[i].split()
            if i == 0:
                appear = file2[i]
            else:
                for j in range(len(file2[i])):
                    if j == 0:
                        name = file2[i][j]
                        new.append(name)
                    else:
                        app = int(file2[i][j])
                        new.append(app)
            if len(new) > 0:
                persons.append(new)
        
        #convert matrix to dictionary
        person2 = {}
        
        for t in range(len(persons)):
            person2[persons[t][0]] = {appear[0]:persons[t][1],appear[1]:persons[t][2],appear[2]:persons[t][3]}
        
        return person2
  
    except FileExistsError as err:
        print(err)

def print1_result(students):
    
    fat = 0
    fat_person = None
    
    tall = 0
    tall_preson = None

    old = 0
    old_preson = None

    for key,value in students.items():
        
        if value['weight'] > fat:
            fat = value['weight']
            fat_person = key
        
        if value['height'] > tall:
            tall = value['height']
            tall_person = key
        
        if value['age'] > old:
            old = value['age']
            old_person = key
        
    print(f"The tallest person is {tall_person} with a height  of {tall} meters")
    
    print("The fattest perosn is",fat_person,"with a weight of",fat,"kilo")
    
    print("The oldest who has %d"%old,"yers old is %s"%old_person)



def main():
    
    students = read_persons_file("apeeraence.txt")
    print1_result(students)

if __name__ == "__main__":
    main()