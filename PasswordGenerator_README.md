
# Password Generator 🔐

## 📌 Purpose
This project is a simple **Password Generator** written in Python.  
It creates strong, random passwords containing **letters, numbers, and symbols** to improve security.

---

## ⚙️ How It Works
1. User enters the desired **password length**.  
2. The program ensures:  
   - At least **1 letter (uppercase/lowercase)**  
   - At least **1 number**  
   - At least **1 symbol**  
3. Fills the rest of the password with random characters.  
4. Shuffles the characters for maximum randomness.  
5. Displays the generated password.  

---

## 🔑 Requirements
- Python 3.x  

No extra libraries are required since it uses Python’s built-in `random` module.

---

## 🚀 Usage
Run the program with:
```bash
python "pass gen.py"
```

Enter the password length when prompted.  

---

## 📊 Example Run
**Input:**  
```
Enter length: 10
```

**Output:**  
```
GENERATE PASSWORD: A3k!sD7p@Q
```

---

## 📝 Notes
- Password length must be **at least 3**, otherwise the program shows an error.  
- You can customize the set of symbols by editing the `symbol` variable in the code.  

---
