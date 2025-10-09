#Get user input of year and subject
year=int(input("Enter any year between 1-4"))


if year ==1 :
            semester=int(input("Enter any semester between 1-2"))
            if semester ==1:
                     print(f"Subjects for the {year} year {semester} semester :")
                     print ("Maths I,\nPhysics,\nChemistry,\nEnglish,\nEngineering Drawing")
            elif semester==2:
                    print(f"Subjects for the {year} year {semester} semester :")
                    print("Data Structures,\nDigital Electronics,\nDiscrete Mathematics,\nObject-Oriented Programming,\nDatabase Systems")
            else:print("Invalid Semester")
elif year ==2:
           semester=int(input("Enter any semester between 3-4"))
           if semester==3:
                    print(f"Subjects for the {year} year {semester} semester :")
                    print("Data Structures,\nDigital Electronics,\nDiscrete Mathematics,\nObject-Oriented Programming,\nDatabase Systems")
           elif semester ==4:
                    print(f"Subjects for the {year} year {semester} semester :")
                    print("Computer Networks,\n Operating Systems,\n Software Engineering,\n Microprocessors,\n Probability & Statistics")
           else:print("Invalid Semester")
elif year ==3 :
          semester=int(input("Enter any semester between 5-6"))
          if  semester==5:
                    print(f"Subjects for the {year} year {semester} semester :")
                    print("Web Technologies,\nComputer Architecture,\nCompiler Design,\nData Mining,\nMachine Learning")
          elif  semester ==6:
                    print(f"Subjects for the {year} year {semester} semester :")
                    print("Artificial Intelligence,\n Cloud Computing,\n IoT Fundamentals,\n Big Data Analytics,\n Cyber Security")
          else:print("Invalid Semester")
elif year ==4:
        semester=int(input("Enter any semester between 7-8"))
        if semester==7:
                   print(f"Subjects for the {year} year {semester} semester :")
                   print ("Advanced Database Systems,\n Mobile App Development,\n Project Work I,\n Elective I,\n Elective II")
        elif semester ==8:
                   print(f"Subjects for the {year} year {semester} semester :")
                   print("Project Work II,\n Seminar,\n Internship,\n Elective III,\n Professional Ethics")
        else: print ("Invalid Semester")
else: print("Invalid year ")

             
