# About tutorIE
TutorIE is a platform where IE students who are struggling on certain subjects can connect with other students who are reliable in their knowledge and willing to tutor others. It is a platform by and for students that aims to enhance the academic expirience of all users. It is primarily designed for first year students in order to facilitate their integration to IE University and a way for them to get used to the academic methods used by this university. 
# Why tutorIE
This platform is designed by students for students to aid in the struggle of finding relaible support. All tutors will be students who have previously taken the specific course and are qualified by IE professors as well as rated by students that have previously used their service. To give credibility to all tutors, you will be able to have information as to what degree they are studying, the year they are in and their overall GPA. 
# What you need
In order to use the platform, the user must have python programming language, any version between 3.6 - 3.8
  - Besides this, no other package will be needed.
# User experience
When accesing the platform, the program will first show a numbered list of all the available degrees -> 
  - User input : The user will be asked to select the number corresponding to their degree. In the scenario where the number is not valid, the system will ask the student again until their input corresponds to a bachelor offered by the university. 
  - Output : The user will recieve a message confirming the degree they have selected. 

After the user selects the degree, the program will show a list of all its corresponding courses for the first year of the degree -> 
  - User input : The user will be asked to write the course they need help with. 
  - Output : The user will be directed to the next selection. 

After selcting the course, the program will show all the tutors available for teaching that specific course -> 
  - Each option will provide the tutor's name, degree, year, and GPA. 
  - User input : The user will be asked to select the number corresponding to the tutor they want. 
  - Output : The user will recieve a confirmation message stating the tutor that they have choosen and will then be directed to the next steps in order to contact their chosen tutor. 

After selcting the tutor, the program will ask for some of the user's basic information ->
  - User input : The user will be asked for their full name, their bachelor, year, email, phone number, and a brief description of what they need help in.
  - Output : The user will be shown a brief summary of all their information and a confirmation message telling them that the information has correctly been sent   and the tutor will be in contact with them. 
# About the code
The program was created using dictionaries and a simple search algorithm ->
  - Dictionaries: There is a dictionary corresponding to the courses for the first year of all bachelors. Each key has a value with the datatype of a list with all of its corresponding subjects. 
  - Simple Search Algorithm: This algorithm is used to search the selected bachelor in the dictionary and in that way show the available courses tutorIE offers classes from.
# Creators
  Daniela Saldarriaga
  
  Elard Meier
  
  Noah Feiger
  
  Sofia Martinez
  
  Tomas Ploquin
  
  Valeria Lopez
