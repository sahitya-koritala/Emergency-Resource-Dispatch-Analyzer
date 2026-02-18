# Emergency-Resource-Dispatch-Analyzer

# Challenge Overview 
This challenge is based on emergency resource request analyzer that classifies the requests into different categories. This is built in python using loops, conditional statements, list slicing and in built functions. Additionally, personalization rules are also implemented. Therefore, the program generate different outputs for different users.

# Features 
1. Accepts multiple requests from user
2. Creates list using pre allocation method 
3. It detects the duplicate values if entered by user
4. Classifies the requests into their respective categories 
  - Low demand (1-20)
  - Moderate demand (21-50)
  - High demand (>50)
  - Invalid requests ( <0 )
  - No demand ( = 0) 
5. Counts the total number of valid, ignored and removed due to personalization requests.
6. Personalization rules are implemented
7. Among the requests values entered, identifies the peak value using max()
8. Displays the output before and after filtering, peak value and duplicate values if they are detected.

# Technologies used 
- Python
- Loops
- Conditional statements
- In-built functions ( replace() , max() , len() )
- List slicing
- Logical operator
- Modulo operator ( % )

# L value and PLI value
1. L Value :
L represents the length of the username after removing spaces using replace().
2. PLI Value (Personalized Logic Index) : 
PLI(personalized logic index) is calculated using : PLI = L % 3
3. The modulo operator % is used to generate a personalized value.

# Personalization rule explanation 

1. The personalization rule is implemented in this program by using the user's name.
2. Spaces are removed in name using replace().
3. Length of the name is calculated using len().
4. A personalised value is generated using :
    Length of name % 3
5. Based on the value: 
  - If the result is 0, then low demand is removed completely from output.
  - If the result is 1, then high demand is removed completely.
  - If the result is 2, then both high and low demands are removed. 
6. Among the entered values, if same values are entered more than one time, then it shows that duplicate values are detected.
7. Also, it displays the peak value from the entered request values.
8. This ensures that the output are different for different users.

# How it Works 
This program takes the multiple requests values from the user and stores them in a list using pre allocation method. It reads the values from a loop. It categories the request into low,moderate, high, invalid requests and no demand using conditional statements.

Next, it removes the spaces from the name entered if there are any spaces. And it calculates the L (length of name ) value . The PLI value is genrerated by using the modulo operator and doing with 3 ( % 3 ). Based on this PLI value, the total number of valid requests are counted and some specific categories are removed.

Finally, the program checks whether it has duplicate values or not and also it displays the highest valid request value using max(). The ouputs are displayed before and after filtering.

# How to Run 
1. Open the file main.py
2. Run the program in python
3. Enter the details that has been asked and check the outputs before and after the personalization rules applied.

# Learning outcomes
Through this challenge, I have learned how to take user input and using the pre-allocation method. I also learned how to use loops and conditional statements and finding the duplicate values using sets. This also improved my understanding of indexing, slicing, handling the lists, string manipulation and using the built-in functions like replace(), len() and max(). Mainly, I have learned how to write a meaningful and logical program based on the conditions given.
