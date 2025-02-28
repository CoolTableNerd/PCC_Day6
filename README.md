### **Python User Input & While Loops (Chapter 7)**  
---

#### **Summary**  
This chapter introduces **user input** with the `input()` function and **while loops** for repetitive tasks. Key concepts include handling numerical input, loop control (`break`, `continue`), and modifying data structures (lists/dictionaries) dynamically.

---

### **Python Keywords & Syntax**  
#### **`input()`**  
- **Definition**: Pauses the program to collect user input.  
- **Syntax**:  
  ```python  
  name = input("Enter your name: ")  # Returns input as a string  
  ```  
- **Use Case**: Collecting user data (e.g., names, preferences).  
- **Numerical Input**: Convert strings to integers/floats:  
  ```python  
  age = int(input("How old are you? "))  
  ```  

#### **`while`**  
- **Definition**: Repeats a block of code as long as a condition is `True`.  
- **Syntax**:  
  ```python  
  while condition:  
      # Code to execute  
  ```  
- **Use Case**: Running a game until the user quits.  

#### **`break`**  
- **Definition**: Exits a loop immediately.  
- **Syntax**:  
  ```python  
  while True:  
      if exit_condition:  
          break  
  ```  
- **Use Case**: Ending a loop when the user types "quit".  

#### **`continue`**  
- **Definition**: Skips the rest of the loop iteration and restarts the loop.  
- **Syntax**:  
  ```python  
  while condition:  
      if skip_condition:  
          continue  
  ```  
- **Use Case**: Skipping even numbers in a count.  

#### **`+=` Operator**  
- **Definition**: Adds a value to a variable and reassigns the result.  
- **Syntax**:  
  ```python  
  counter += 1  # Equivalent to counter = counter + 1  
  ```  
- **Use Case**: Incrementing a counter in a loop.  

#### ** `%` (Modulo)**  
- **Definition**: Returns the remainder of division.  
- **Syntax**:  
  ```python  
  remainder = 7 % 3  # Returns 1  
  ```  
- **Use Case**: Checking for even/odd numbers.  

---

### **Key Concepts**  
#### **User Input**  
- **Prompt Formatting**: Add a space at the end of prompts for readability.  
  ```python  
  prompt = "Enter your age: "  
  age = input(prompt)  
  ```  

#### **While Loops**  
- **Flag Variable**: Control loop execution with a Boolean.  
  ```python  
  active = True  
  while active:  
      if exit_condition:  
          active = False  
  ```  

#### **Modifying Lists**  
- **Remove All Instances**:  
  ```python  
  pets = ["dog", "cat", "cat"]  
  while "cat" in pets:  
      pets.remove("cat")  
  ```  

#### **Storing Data in Dictionaries**  
- **Dynamic Data Collection**:  
  ```python  
  responses = {}  
  while polling_active:  
      name = input("Name: ")  
      response = input("Favorite mountain: ")  
      responses[name] = response  
  ```  

---

### **Project: Interactive Polling System**  
#### **Objective**  
Create a program that collects user responses to a question and displays results.  

#### **Requirements**  
1. **Collect Responses**:  
   - Use `input()` to ask a question (e.g., "What's your dream vacation spot?").  
   - Store responses in a dictionary with names as keys.  

2. **Loop Control**:  
   - Allow users to quit by typing "exit".  
   - Use a `while` loop to keep the poll active until the user quits.  

3. **Data Validation**:  
   - Ensure no duplicate names are allowed.  
   - Handle numerical input (e.g., age) with error checking.  

4. **Display Results**:  
   - Print all responses in a formatted list after polling ends.  

#### **Example Output**  
```  
Welcome to the Poll!  
Enter 'exit' to quit.  
Name: Alice  
Response: Iceland  
Name: Bob  
Response: Japan  
Name: exit  

Results:  
- Alice: Iceland  
- Bob: Japan  
```  

---

### **Study Questions**  
1. How does the `input()` function handle numerical data, and how can you fix it?  
2. Write a `while` loop that counts from 1 to 10 and skips even numbers.  
3. What happens if you forget to increment the counter in a `while` loop?  
4. How would you modify a list to remove all instances of "apple"?  
5. Explain the difference between `break` and `continue`.  
6. Write code to collect user ages until they type "done" and calculate the average.  
7. Why might you use a dictionary instead of a list to store poll responses?  

--- 

##Blog Post
[Becoming Loopy](https://medium.com/@CoolTableNerd/becoming-loopy-b21dec6d0192)