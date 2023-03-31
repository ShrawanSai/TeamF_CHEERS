# TeamF_CHEERS
Official Git repository of TEAM-F for the CHEERS project as part of the project component for the subject "Advanced Programming Practices" under the guidance of Professor Pankaj Kamthan


# Steps to run code
### Incarnation 1
 - Make sure the following folder structure is maintained:
[TeamF_CHEERS/Incarnation1.png at main · ShrawanSai/TeamF_CHEERS (github.com)](https://github.com/ShrawanSai/TeamF_CHEERS/blob/main/images/Incarnation1.png)
 - The Math functions are implemented in "main.py" and the driver code is called "user_input.py"
 - The "pi_at_1000_rounds.pkl" file is used for accessing the value of PI faster instead of computing it from scratch every time.
 - The driver code runs 2 functions which are:
				 - sample_outputs(): which runs the code on a set of sample radii which comprise of [5, 10, 15, 20, 25, 30, 35, 40, 45, 50]
				 - main() which expects a single user input of a radius and outputs the length of the required line segment

 -NOTE: All libraries (pickle for example) used in Incarnation 1 are used only for the non-functional requirements and are not used achieve any functional requirements


### Incarnation 2
 - Make sure the following folder structure is maintained:
[TeamF_CHEERS/Incarnation2.png at main · ShrawanSai/TeamF_CHEERS (github.com)](https://github.com/ShrawanSai/TeamF_CHEERS/blob/main/images/Incarnation2.png)
 - The only python file "main.py" is the driver code that has the full implementation of the incarnation
 - The driver code runs 2 functions which are:
				 - sample_outputs(): which runs the code on a set of sample radii which comprise of [5, 10, 15, 20, 25, 30, 35, 40, 45, 50]
				 - main() which expects a single user input of a radius and outputs the length of the required line segment

 -NOTE: All libraries (pickle for example) used in Incarnation 1 are used only for the non-functional requirements and are not used achieve any functional requirements


#### Unit Test cases for D2:
| Test Case  | Input | Expected Output |
| ------------- | ------------- | ------------- |
| Regular  | 5  | 5.95884937 |
| Regular  | 10  | 11.91769874 |
| Regular  | 15 | 17.87654811 |
| Zero Radius  | 0  | 0 |
| Large Radius  | 1000000  | 1191769.87445515 |
| Small Radius  | 0.0001 | 0.000119176987 |
| Negative Radius  | -10 | Invalid Input |
