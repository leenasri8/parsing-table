# Predictive Parsing Table Generator (LL(1)

## 📌 Project Description
This project implements Predictive Parsing Table construction using Python.

Predictive parsing is a top-down parsing technique used in compiler design.
It uses FIRST and FOLLOW sets to create an LL(1) parsing table.

---

## 🎯 Objectives
- Understand Predictive Parsing
- Implement LL(1) Parsing Table
- Use FIRST and FOLLOW sets
- Simulate compiler parsing phase

---

## 🧠 Concepts Used
- Context Free Grammar
- FIRST Set
- FOLLOW Set
- LL(1) Parsing
- Compiler Design

---

## 🛠 Requirements
- Python 3.x

---

## ▶ How to Run

1. Install Python
2. Save file as:
   predictive_parsing_table.py

3. Run:
   python predictive_parsing_table.py

---

## 📊 Example Grammar Used
E  -> T E'
E' -> + T E' | ε
T  -> F T'
T' -> * F T' | ε
F  -> ( E ) | id

---

## 📌 Output
Displays Predictive Parsing Table in matrix format.

---

## 🚀 Future Improvements
- Take grammar as user input
- Auto compute FIRST and FOLLOW
- Add string parsing simulation

---

## 👩‍💻 Author
Student Mini Project – Compiler Design Lab
