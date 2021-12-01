tutors_BAM = [("Tutor 1","Roberta", "3rd Year BAM Student", "GPA: 99"), ("Tutor 2", "Lorenza", "2nd Year BAM Student", "GPA: 92"), ("Tutor 3","Emilia", "2nd Year BAM Student", "GPA: 88")]
tutors_BAS = [("Tutor 1", "Jose", "4th Year BAS Student", "GPA: 91"), ("Tutor 2","Constanza", "2nd Year BAS Student", "GPA: 94"), ("Tutor 3","Laura", "2nd Year BAS Student", "GPA: 89")]
tutors_BBSS = [("Tutor 1","Pablo", "3rd Year BBSS Student", "GPA: 93"), ("Tutor 2","Valeria", "4th Year BBSS Student", "GPA: 97"), ("Tutor 3","Daniela", "3rd Year BBSS Student", "GPA: 89")]
tutors_BBA = [("Tutor 1","Valentina", "3rd Year BBA Student", "GPA: 92"), ("Tutor 2","Lucas", "4th Year BBA Student", "GPA: 99"), ("Tutor 3","Fernando", "3rd Year BBA Student", "GPA: 91")]
tutors_BCDM = [("Tutor 1","Lucia", "3rd Year BCDM Student", "GPA: 92"), ("Tutor 2","Ana", "4th Year BCDM Student", "GPA: 100"), ("Tutor 3","Sofia", "3rd Year BCDM Student", "GPA: 90")]
tutors_BCSAI= [("Tutor 1","Gilberto", "2nd Year BCSAI Student", "GPA: 94"), ("Tutor 2","Carlota", "2nd Year BCSAI Student", "GPA: 91"), ("Tutor 3","Tomas", "2nd Year BCSAI Student", "GPA: 98")]
tutors_BDBA = [("Tutor 1","Noah", "2nd Year BDBA Student", "GPA: 95"), ("Tutor 2","Elard", "2nd Year BBA and BDBA Student", "GPA: 95"), ("Tutor 3","Jimena", "4th Year BDBA Student", "GPA: 92")]
tutors_BiD = [("Tutor 1","Daph", "2nd Year Design Student", "GPA: 94"), ("Tutor 2","Sophie", "2nd Year Design Student", "GPA: 91"), ("Tutor 3","Patricio", "3rd Year Design Student", "GPA: 88")]
tutors_BiE = [("Tutor 1","Daniel", "2nd Year Economics Student", "GPA: 93"), ("Tutor 2","Pedro", "3rd Year Economics Student", "GPA: 89"), ("Tutor 3","Oscar", "2nd Year Economics Student", "GPA: 97")]
tutors_BIR = [("Tutor 1","Cata", "2nd Year IR Student", "GPA: 99"), ("Tutor 2","Cande", "2nd Year BBA and IR Student", "GPA: 91"), ("Tutor 3","Mauricio", "4th Year IR Student", "GPA: 90")]
tutors_PPLE = [("Tutor 1","Isabel", "2nd Year PPLE Student", "GPA: 87"), ("Tutor 2","Natalia", "2nd Year PPLE Student", "GPA: 96"), ("Tutor 3","Laura", "4th Year PPLE Student", "GPA: 93")]
tutors_LAW = [("Tutor 1","Camila", "3rd Year Law Student", "GPA: 97"), ("Tutor 2","Bernando", "2nd Year Law Student", "GPA: 87"), ("Tutor 3","Ana Paula", "2nd Year Law Student", "GPA: 90")]


list_bachelors = ["Bachelor in Applied Mathematics","Bachelor in Architectural Studies", "Bachelor in Behavior and Social Sciences", "Bachelor in Business Administration",
                  "Bachelor in Communiation and Digital Media", "Bachelor in Computer Science and Artificial Intelligence", "Bachelor in Data and Business Analytics",
                  "Bachelor in Deisgn", "Bachelor in Economics", "Bachelor in International Relations", "Bachelor in Philosophy, Politics, Economics and Law",
                  "Bachelor in Law"]

first_year = dict()

first_year = {"Bachelor in Applied Mathematics": ["1. Mathematical Fundamentals","2. Fundamentals of Algebra",
                                                  "3. Differential Calculus", "4. Probability and Statistics", "5. Research Methods and Design",
                                                  "6. Applied Maths: Energy and Sustainability", "7. Linear Algebra", "8. Discrete Mathematics",
                                                  "9. Integral Calculus", "10. Programming for Applied Mathematics", "11. Applied Math: Finance & Banking"],
              "Bachelor in Architectural Studies": ["1. Design Studio 1", "2. Graphic Communication 1", "3. Applied Mathematics in Architecture 1",
                                                    "4. Architecture Histories and Contexts", "5. Interpersonal Skills", "6. Design Studio 2","7. Graphic Communication 2",
                                                    "8. Architectural Geometry 1", "9. Applied Physics in Architecture 1", "10. Business Management",
                                                    "11. Digital Tools and Operations"],
              "Bachelor in Behavior and Social Sciences": ["1. Learning to Observe, Experiment and Survey","2. Fundamentals of Social Science",
                                                           "3. Writing Skills","4. Data Insights and Visualizations", "5. Introduction to Business Managment",
                                                           "6. Fundamentals of Statistics and Probability", "7. Technology Trends Today", "8. Fundamentals of Data Analysis",
                                                           "9. Simulating and Modeling to Understand Change", "10. The Big History of Ideas and Innovation",
                                                           "11. Fundamentals of Human Behavior"],
              "Bachelor in Business Administration": ["1. Financial Accounting", "2. Managment Tools and Principles", "3. Applied Business Mathematics",
                                                      "4. Marketing Fundamentals", "5. Building Powerful Relationships", "6. Research & Academic Writing Skills",
                                                      "7. Cost Accounting", "8. Mathematics for Management", "9. Introduction to Programming", "10. Corporate Finance",
                                                      "11. Microeconomics"],
              "Bachelor in Communiation and Digital Media": ["1. Communication Foundations", "2. Photography", "3. Globalization and Cross-Cultural Communication",
                                                             "4. Writing for Media", "5. Oral Skills", "6. Public Opinion, Persuasion and Engagement",
                                                             "7. Visual and Digital Media Culture", "8. Graphic Design and Infographics", "9. Public Affairs and Non-Market Strategies",
                                                             "10. Technology Fluency", "11. Introduction to Management"],
              "Bachelor in Computer Science and Artificial Intelligence":["1. Fundamentals of Human Behavior","2. Fundamentals of Social Science", "3. Fundamentals of Technology & Innovation",
                                                                          "4. Introduction to Management", "5. Fundamentals of Probability Statistics", "6. Learning to Observe, Experiment & Survey",
                                                                          "7. Simulating and Modeling to Understand Change", "8. The Big History of Ideas & Innovation", "9. Principles of Programming",
                                                                          "10. Data Insights and Visualization", "11. Physics"],
              "Bachelor in Data and Business Analytics":["1. Learning to Observe, Experiment and Survey", "2. Fundamentals of Social Science",
                                                         "3. Data Insights & Visualizations", "4. Introduction to Business Management", "5. Fundamnetals of Statistics and Probability",
                                                         "6. Technology Trends Today", "7. Fundamentals of Data Analysis", "8. Simulating and Modeling to Understand Change", "9. The Big History of Ideas & Innovation",
                                                         "10. Presentation Skills", "11. Fundamentals of Human Behavior"],
              "Bachelor in Deisgn": ["1. Intro to Design Studio 1", "2. Design History 1", "3. Design Skills 1", "4. Psychology and User Center Design", "5. Presentation Skills",
                                     "6. Writing Skills", "7. Intro to Design Studio 2", "8. Design History 2", "9. Visualization and Representation Techniques", "10. Sociology and Culture",
                                     "11. Design Techniques"],
              "Bachelor in Economics": ["1. Mathematics for Economists", "2. Foundation of Microeconomics", "3. Foundations of Macroeconomics", "4. Economic History",
                                        "5. Impact Writing Lab", "6. Programming for Economists", "7. Development and Growth Economics", "8. International Trade and Monetary System",
                                        "9. Probability and Statistics", "10. Game Theory", "11. Research Methods for Economists"],
              "Bachelor in International Relations": ["1. History of International Relations up to 1945", "2. Introduction to Political Science", "3. Microeconomics",
                                                      "4. Political Theory", "5. Languages 1", "6. Unplugged 1: Introduction to Agenda 2030", "7. Contemporary Global History",
                                                      "8. Macroeconomics", "9. Languages 2", "10. Unplugged 2: Systems Thinking", "11. International Relations Theory"],
              "Bachelor in Philosophy, Politics, Economics and Law": ["1. Mathematics", "2. Elementary Logic", "3. European Legal History", "4. Introduction to Political Science", "5. Writing Skills",
                                                                      "6. Research Methods and Data Analysis", "7. Microeconomics", "8. Social Seminar 1", "9. History of Ancient and Medieval Philosophy",
                                                                      "10. Constitutional Law", "11. Government and Comparative Politics"],
              "Bachelor in Law": ["1. European Legal History", "2. Constitutional Law", "3. Introduction to Private Law: Civil Law", "4. Economics", "5. Unplugged 1",
                                  "6. Accounting and Finance", "7. Criminal Law 1", "8. Civil Law Contracts", "9. Unplugged 2", "10. Legal Thought", "11. Administrative Law 1"]}


def class_search(bachelor):
    for key, value in first_year.items():
        if key==bachelor:
          classes = value
          for i in classes:
            print(i, end = "\n" )


class Student():
    def __init__(self):
        pass

    def choose_bachelor(self):
        print(
            "Welcome to TutorIE, a platform designed for and by students to give classes and maximize academic performance.")
        print()
        print(
            "Choose the bachelor you are taking (If you are doing a dual degree choose the bachelor linked to the subject you need help with).")
        print(
            "Your options are as follows: \n 1. Bachelor in Applied Mathematics \n 2. Bachelor in Architectural Studies"
            "\n 3. Bachelor in Behavior and Social Sciences \n 4. Bachelor in Business Administration, \n 5. Bachelor in Communication and Digital Media"
            "\n 6. Bachelor in Computer Science and Artificial Intelligence \n 7. Bachelor in Data and Business Analytics"
            "\n 8. Bachelor in Design \n 9. Bachelor in Economics \n 10. Bachelor in International Relations"
            "\n 11. Bachelor in Philosophy, Politics, Economics and Law \n 12. Bachelor in Law")
        self.bachelor = eval(input("What number corresponds to the bachelor you need help with?"))

        while self.bachelor != "":
            if self.bachelor == 1:
                print()
                print("The bachelor you have selected is:", list_bachelors[0])
                print()
                print("Your bachelor has the following class options:")
                print()
                class_search(list_bachelors[0])
                break
            elif self.bachelor == 2:
                print()
                print("The bachelor you have selected is:", list_bachelors[1])
                print()
                print("Your bachelor has the following class options:")
                print()
                class_search(list_bachelors[1])
                break
            elif self.bachelor == 3:
                print()
                print("The bachelor you have selected is:", list_bachelors[2])
                print()
                print("Your bachelor has the following class options:")
                print()
                class_search(list_bachelors[2])
                break
            elif self.bachelor == 4:
                print()
                print("The bachelor you have selected is:", list_bachelors[3])
                print()
                print("Your bachelor has the following class options:")
                print()
                class_search(list_bachelors[3])
                break
            elif self.bachelor == 5:
                print()
                print("The bachelor you have selected is:", list_bachelors[4])
                print()
                print("Your bachelor has the following class options:")
                print()
                class_search(list_bachelors[4])
                break
            elif self.bachelor == 6:
                print()
                print("The bachelor you have selected is:", list_bachelors[5])
                print()
                print("Your bachelor has the following class options:")
                print()
                class_search(list_bachelors[5])
                break
            elif self.bachelor == 7:
                print()
                print("The bachelor you have selected is:", list_bachelors[6])
                print()
                print("Your bachelor has the following class options:")
                print()
                class_search(list_bachelors[6])
                break
            elif self.bachelor == 8:
                print()
                print("The bachelor you have selected is:", list_bachelors[7])
                print()
                print("Your bachelor has the following class options:")
                print()
                class_search(list_bachelors[7])
                break
            elif self.bachelor == 9:
                print()
                print("The bachelor you have selected is:", list_bachelors[8])
                print()
                print("Your bachelor has the following class options:")
                print()
                class_search(list_bachelors[8])
                break
            elif self.bachelor == 10:
                print()
                print("The bachelor you have selected is:", list_bachelors[9])
                print()
                print("Your bachelor has the following class options:")
                print()
                class_search(list_bachelors[9])
                break
            elif self.bachelor == 11:
                print()
                print("The bachelor you have selected is:", list_bachelors[10])
                print()
                print("Your bachelor has the following class options:")
                print()
                class_search(list_bachelors[10])
                break
            elif self.bachelor == 12:
                print()
                print("The bachelor you have selected is:", list_bachelors[11])
                print()
                print("Your bachelor has the following class options:")
                print()
                class_search(list_bachelors[11])
                break
            else:
                print("The bachelor you have selected is not valid. Try again.")

                print(
                    "Your options are as follows: \n 1. Bachelor in Applied Mathematics \n 2. Bachelor in Architectural Studies"
                    "\n 3. Bachelor in Behavior and Social Sciences \n 4. Bachelor in Business Administration, \n 5. Bachelor in Communication and Digital Media"
                    "\n 6. Bachelor in Computer Science and Artificial Intelligence \n 7. Bachelor in Data and Business Analytics"
                    "\n 8. Bachelor in Design \n 9. Bachelor in Economics \n 10. Bachelor in International Relations"
                    "\n 11. Bachelor in Philosophy, Politics, Economics and Law \n 12. Bachelor in Law")
                self.bachelor = eval(input("What number corresponds to the bachelor you need help with?"))

    def class_tutor(self):
        print()
        course = int(input("Write the number correspoding to the class you want to tutoring from:"))

        while course != "":
            if course in range(1, 11):
                print("The class you have entered is valid.")
                break
            else:
                print("The class you have entered is not valid.")

                print()
                print("Write the name exactly how it appears in the list (Program is case sensitive)")
                course = int(input("Write the number correspoding to the class you want to tutoring from:"))

        print()

    def tutors_available(self):
        if self.bachelor == 1:
            print()
            print("These are the available tutors for your class and degree:")
            print(tutors_BAM)
        elif self.bachelor == 2:
            print()
            print("These are the available tutors for your class and degree:")
            print(tutors_BAS)
        elif self.bachelor == 3:
            print()
            print("These are the available tutors for your class and degree:")
            print(tutors_BBSS)
        elif self.bachelor == 4:
            print()
            print("These are the available tutors for your class and degree:")
            print(tutors_BBA)
        elif self.bachelor == 5:
            print()
            print("These are the available tutors for your class and degree:")
            print(tutors_BCDM)
        elif self.bachelor == 6:
            print()
            print("These are the available tutors for your class and degree:")
            print(tutors_BCSAI)
        elif self.bachelor == 7:
            print()
            print("These are the available tutors for your class and degree:")
            print(tutors_BDBA)
        elif self.bachelor == 8:
            print()
            print("These are the available tutors for your class and degree:")
            print(tutors_BiD)
        elif self.bachelor == 9:
            print()
            print("These are the available tutors for your class and degree:")
            print(tutors_BiE)
        elif self.bachelor == 10:
            print()
            print("These are the available tutors for your class and degree:")
            print(tutors_BIR)
        elif self.bachelor == 11:
            print()
            print("These are the available tutors for your class and degree:")
            print(tutors_PPLE)
        elif self.bachelor == 12:
            print()
            print("These are the available tutors for your class and degree:")
            print(tutors_LAW)

    def choose_tutor_validation(self):
        print()
        self.tutor_n = eval(input("What is the number of the tutor you are interested in? (only include the number)"))
        print()

        while self.tutor_n != "":
            if self.tutor_n in range(1, 3):
                print("That is a valid tutor.")
                print()
                break
            else:
                print("That is not a valid tutor.")
                print()

                self.tutor_n = eval(
                    input("What is the number of the tutor you are interested in? (only include the number)"))

    def choose_tutor(self):
        if self.bachelor == 1:
            print("Your choosen tutor is:", tutors_BAM[(self.tutor_n - 1)])
        elif self.bachelor == 2:
            print("Your choosen tutor is:", tutors_BAS[(self.tutor_n - 1)])
        elif self.bachelor == 3:
            print("Your choosen tutor is:", tutors_BBSS[(self.tutor_n - 1)])
        elif self.bachelor == 4:
            print("Your choosen tutor is:", tutors_BBA[(self.tutor_n - 1)])
        elif self.bachelor == 5:
            print("Your choosen tutor is:", tutors_BCDM[(self.tutor_n - 1)])
        elif self.bachelor == 6:
            print("Your choosen tutor is:", tutors_BCSAI[(self.tutor_n - 1)])
        elif self.bachelor == 7:
            print("Your choosen tutor is:", tutors_BDBA[(self.tutor_n - 1)])
        elif self.bachelor == 8:
            print("Your choosen tutor is:", tutors_BiD[(self.tutor_n - 1)])
        elif self.bachelor == 9:
            print("Your choosen tutor is:", tutors_BiE[(self.tutor_n - 1)])
        elif self.bachelor == 10:
            print("Your choosen tutor is:", tutors_BIR[(self.tutor_n - 1)])
        elif self.bachelor == 11:
            print("Your choosen tutor is:", tutors_PPLE[(self.tutor_n - 1)])
        elif self.bachelor == 12:
            print("Your choosen tutor is:", tutors_LAW[(self.tutor_n - 1)])

    def contact_tutor(self):
        print()
        print("It is time to contact your tutor!")
        print("This information will be sent directly to your choosen tutor:")
        print("All this information is confidential between you and your tutor.")
        print()
        your_name = input("What is your full name (include last name)?")
        your_bachelor = input("What is your bachelor?")
        your_year = input("What year are you in?")
        email = input("Enter your email:")
        phone = input("What is your phone number?")
        help = input("Briefly describe in what ways you need help with:")
        student_info = [your_name, your_bachelor, your_year, email, phone, help]
        print()
        print("Summary of Information:", student_info)
        print()
        print("Your information has been correctly sent to your tutor!")
        print("Now, you have to wait until you receive a message from them.")


student = Student()
student.choose_bachelor()
student.class_tutor()
student.tutors_available()
student.choose_tutor_validation()
student.choose_tutor()
student.contact_tutor()
