# 📚 Learning Progress

✍️ **Author:** Sk Sohag Khan  
🎓 CSE Student | Future Full Stack Developer 🚀

---

## 📅 Week 1

---

### 🔹 Day 01

<details>
<summary>View Details</summary>

### ✅ Day 1 Progress (25 February 2026)

#### 🔧 Environment Setup

* Created and activated a virtual environment
* Installed Django using pip
* Initialized a new Django project

#### 📂 Project Structure Analysis

* **manage.py** – Command-line utility
* **settings.py** – Configuration
* **urls.py** – Routing
* **asgi.py & wsgi.py** – Deployment
* SQLite database (`db.sqlite3`) created automatically

#### ▶️ Execution

* Ran development server
* Opened Django welcome page

✅ Environment ready for development

</details>

---

### 🔹 Day 02

<details>
<summary>View Details</summary>

### 📅 Day 02 Progress

#### 📚 Topics Covered

* Django Settings Explained
* How Django Works
* URLs & HTTPResponse
* Django Template
* Bootstrap Integration

#### 🎯 What I Learned

* Request processing in Django
* URL → View connection
* Template rendering
* Bootstrap integration

</details>

---

### 🔹 Day 03

<details>
<summary>View Details</summary>

### 📅 Day 03 Progress

#### 📚 Topics Covered

##### 🔹 Static Files

* STATIC_URL, STATIC_ROOT, STATICFILES_DIRS
* `{% load static %}`

##### 🔹 Django Apps

* Created apps (`startapp`)
* App structure understanding

##### 🔹 Admin Panel

* Created superuser
* Registered models

##### 🔹 Models

* Created models
* Field types (CharField, IntegerField)
* `__str__()` method

##### 🔹 Migrations

* makemigrations
* migrate

#### 🛠️ Commands

```
python manage.py startapp appname
python manage.py makemigrations
python manage.py migrate
python manage.py createsuperuser
python manage.py runserver
```

</details>

---

### 🔹 Day 04

<details>
<summary>View Details</summary>

### 📅 Day 04 Progress – HTML Learning

#### 🚀 Overview

Completed HTML (Level 1 → Pro)

#### 📚 Topics Covered

##### 🔹 Basic Structure

* HTML Boilerplate
* `<html>`, `<head>`, `<body>`
* Meta & Title

##### 🔹 Text & Formatting

* Headings (h1-h6)
* Paragraph `<p>`
* `<b>`, `<i>`, `<u>`
* `<br>`, `<hr>`
* `<sub>`, `<sup>`
* `<pre>`

##### 🔹 Links & Media

* `<a>`
* `<img>`
* `<video>`
* `<iframe>`

##### 🔹 Layout

* `<header>`, `<main>`, `<footer>`
* `<section>`, `<article>`, `<aside>`
* `<div>`, `<span>`

##### 🔹 Lists

* `<ul>`, `<ol>`
* Nested list

##### 🔹 Tables

* `<table>`, `<tr>`, `<td>`, `<th>`
* `<thead>`, `<tbody>`, `<caption>`

##### 🔹 Forms

* `<form>`
* `<input>` (text, password, radio, checkbox)
* `<textarea>`
* `<select>`

#### 🎯 Outcome

✅ Built complete HTML page  
✅ Strong foundation in HTML

</details>

---

### 🔹 Day 05

<details>
<summary>View Details</summary>

### 📅 Day 05 Progress – CSS Learning

#### 📚 Topics Covered

##### 🎯 CSS Selectors
* Universal Selector (`*`)
* ID Selector (`#box`)
* Class Selector (`.heading`)

##### 🎯 Text Properties
* Text decoration (underline)
* Font weight (bold)
* Line height
* Text transform (capitalize)

##### 🎯 Box Model
* Width & Height
* Padding & Margin
* Border & Border-radius

##### 🎯 Display Property
* Inline
* Block
* None

##### 🎯 Opacity
* RGBA color transparency

##### 🎯 Positioning
* Relative Position
* Absolute Position
* Top, Left properties

##### 🎯 Z-index
* Layer control using z-index

##### 🎯 Flexbox
* `display: flex`
* `justify-content`
* `align-items`

##### 🎯 Background
* Background Image
* Background Size (cover)

##### 🎯 Transition
* Smooth hover effect
* Transform (scale)

##### 🎯 Animation
* `@keyframes`
* Infinite rotation (Loader)

##### 🎯 Media Queries (Responsive Design)
* Different screen sizes:
  * max-width: 300px
  * 300px–400px
  * 400px–600px
  * 600px+

</details>

---

### 🔹 Day 06

<details>
<summary>View Details</summary>

### 📅 Day 06 Progress – Python Learning

#### 📂 Project Files

* firstProgramme.py
* printSum.py
* Variables.py
* DataType.py
* TypeConversion.py
* Input in python.py
* Arithmetic operators.py
* String and conditional statements.py
* List in Python.py
* Tuple in python.py
* Dictionary and Set in python.py
* Practice.py

#### 📚 Topics Covered

**📌 First Programme**
```python
print("Hello World")
```

* Variables & Data Types
* Type Conversion
* Input Handling
* Operators
* String & Conditionals
* List, Tuple, Dictionary, Set

</details>

---

### 🔹 Day 07

<details>
<summary>View Details</summary>

### 📅 Day 07 Progress – Python Advanced

#### 📂 Files

* ExceptionHandling.py
* File Basic.py
* File_handling.py
* Function.py

#### 📚 Topics Covered

**🔸 Function**
* Function definition (`def`)
* Parameters & arguments
* Return values

**🔸 File Handling**
* open(), read(), write()
* File modes (`r`, `w`, `a`)
* with open() (best practice)

**🔸 Exception Handling**
* try-except block
* Multiple exceptions
* Common errors:
  * ZeroDivisionError
  * IndexError
  * FileNotFoundError
  * ValueError
* General exception (`Exception as e`)

#### 🧠 Practice

* Function তৈরি ও ব্যবহার
* File read/write করা
* Error handle করা

#### 🚀 Conclusion

Today I learned how to write **clean, structured, and error-free Python programs**.

</details>

---

## 📅 Week 2

---

### 🔹 Day 01

<details>
<summary>View Details</summary>

### 📅 Day 01 Progress – OOP in Python

#### 📚 Topics Learned

##### 🧱 OOP Core Practice
* Class & Object implementation
* Constructor (`__init__`) and string representation (`__str__`)
* Updating object attributes using methods

##### 🔢 Custom Class Example
* Fraction class with:
  * Validation (denominator ≠ 0)
  * Simplification using `math.gcd()`
  * Operator overloading (`__add__`)

##### ⚙️ Special Methods (Dunder Methods)
* `__init__()` → Object initialization
* `__str__()` → Human-readable output
* `__add__()` → Operator overloading

##### 🏷️ Class Method & Static Method
* `@classmethod` → Access class variables
* `@staticmethod` → Utility method without class/object access

---

#### 🧬 Inheritance Types

* ✅ Single Inheritance
* ✅ Multiple Inheritance
* ✅ Multilevel Inheritance
* ✅ Hierarchical Inheritance
* ✅ Hybrid Inheritance

---

#### 🔁 Polymorphism
* Same method name, different behavior
* Example: `make_sound()` for different animals

---

#### ➕ Method Concepts
* Method Overloading (default arguments)
* Method Overriding (same method in child class)

---

#### 🔒 Encapsulation
* Private variable using `__balance`
* Controlled access via methods

---

#### 🎭 Abstraction
* Abstract Base Class using `abc`
* `@abstractmethod` enforcement

---

#### 🔌 Interface (Python Style)
* Implemented using abstract classes
* Only method definitions, no implementation

---

#### 🏗️ Design Patterns

**1️⃣ Singleton Pattern**
* Ensures only one instance exists

**2️⃣ Factory Pattern**
* Creates objects based on input

**3️⃣ Builder Pattern**
* Step-by-step object creation (method chaining)

---

#### 💡 Key Takeaways

* Strong understanding of OOP concepts
* Learned real-world class design
* Practiced inheritance & polymorphism deeply
* Explored design patterns for scalable code

---

#### 🚀 Practice Outcome

* Built multiple classes with real logic
* Implemented operator overloading
* Designed reusable and maintainable code structures

</details>

---

### 🔹 Day 02

<details>
<summary>View Details</summary>

### 📅 Day 02 Progress – Date/Time, JSON & API

#### 🕒 Date & Time in Python

```python
import datetime

# Current Date & Time
now = datetime.datetime.now().day
today = datetime.datetime.today()

print(now)
print(today)

# Custom Date
custom_date = datetime.datetime(2026, 4, 15, 4, 59, 0)
print(custom_date, type(custom_date))

# Datetime → String
d1 = today.strftime("%Y/%M/%d %H:%M:%S")
d2 = today.strftime("%d,%B,%Y %H:%M:%S")
d3 = today.strftime("%d,%b,%Y %H:%M:%S")
d4 = today.strftime("%d,%b,%Y -%A %H:%M:%S")
d5 = today.strftime("%d,%b,%Y -%a %I:%M:%S %p")

# String → Datetime
date_str = "15,Apr,2026 -Wed 05:23:09 PM"
date_obj = datetime.datetime.strptime(date_str, "%d,%b,%Y -%a %I:%M:%S %p")
print(date_obj, type(date_obj))

# Date Arithmetic
from datetime import timedelta

tommorow = today + timedelta(days=1)
yesterday = today - timedelta(days=1)
test = today + timedelta(hours=5)

present = datetime.datetime.strptime("20 Apr 2026", "%d %b %Y")
prev = datetime.datetime.strptime("10 Apr 2026", "%d %b %Y")
print(present - prev)
```

---

#### 🌐 JSON & API in Python

##### 📁 Files

* datetime.py
* json_basics.py
* serialization.py
* deserialization.py
* api_get.py
* api_post.py
* api_patch.py
* api_put.py
* api_delete.py
* api_data_handling.py

##### 📚 Topics

* Date & Time in Python
* JSON (JavaScript Object Notation)
* Serialization & Deserialization
* CRUD Operations
* API using requests

---

##### 💻 Code Examples

**🔹 Serialization**
```python
import json
data = {"user_id": 123, "post": "Hello", "edit": True}
print(json.dumps(data, indent=4))
```

**🔹 Deserialization**
```python
json_string = '{"user_id":123,"post":"Hello","edit":true}'
print(json.loads(json_string))
```

**🔹 GET**
```python
import requests
print(requests.get("https://jsonplaceholder.typicode.com/posts").json())
```

**🔹 POST**
```python
value = {"userId": 1, "id": 101, "title": "test", "body": "test"}
print(requests.post("https://jsonplaceholder.typicode.com/posts", value).json())
```

**🔹 PATCH**
```python
print(requests.patch("https://jsonplaceholder.typicode.com/posts/1", {"title": "test"}).json())
```

**🔹 PUT**
```python
value = {"userId": 1, "id": 101, "title": "test", "body": "test"}
print(requests.put("https://jsonplaceholder.typicode.com/posts/1", value).json())
```

**🔹 DELETE**
```python
print(requests.delete("https://jsonplaceholder.typicode.com/posts/1").json())
```

---

#### 🎯 Conclusion

* Learned Date & Time handling
* Practiced JSON conversion
* Understood CRUD & API

</details>

---

### 🔹 Day 03

<details>
<summary>View Details</summary>

### 📅 Day 03 Progress – JavaScript Practice

📘 Today I practiced JavaScript basics, arrays, functions, objects, and DOM manipulation.

---

#### 💎 JavaScript Basics

* `console.log()` usage
* Variables (`let`, `const`)

```js
let x = 10;
let str = "Sakib";
let num = 1212;
let y = 1234567890123456789n;
```

---

#### 💎 Operators & Conditions

```js
if (c == 10) {
    console.log("Value Matched");
}
```

---

#### 💎 Loops

```js
for (let color of colors) {
    console.log(color);
}
```

---

#### 💎 Arrays & Methods

```js
const names = ["raj", "Taj"];
const newNames = names.map(item => item + "___");
```

---

#### 💎 Functions

```js
const greet = () => {
    console.log("Hello");
};
```

---

#### 💎 Objects

```js
const person = {
    name: "Sohag",
    age: 25
};
```

---

#### 💎 DOM Manipulation

```js
const el = document.getElementById("lalala");
el.textContent = "Changed Text";
```

---

#### 💎 Events

```js
button.addEventListener("mouseover", colorBG);
```

---

#### 🚀 Mini Project

* Button hover → text change
* DOM manipulation practice

---

#### ⚠️ Challenges Faced

* `document is not defined`
* DOM confusion
* innerHTML vs textContent

---

#### ✅ Conclusion

* Learned JS fundamentals
* Practiced DOM

---

📌 **Next Goal:**
➡️ DOM advanced  
➡️ Small projects

</details>

---

### 🔹 Day 04

<details>
<summary>View Details</summary>

### 📅 Day 04 Progress – Tailwind CSS

#### 📌 What I Learned Today

Today I explored **Tailwind CSS** and learned how utility-first CSS works with real examples.

---

#### 🔹 Tailwind Setup

##### 📁 Files Used
* `index.html`
* `style.css`
* `style.out.css`

##### 💻 Tailwind Import

```css
@import "tailwindcss";
@custom-variant dark (&:where(.dark, .dark *));
```

#### 🎯 What I Learned

* Utility-first CSS approach
* Tailwind configuration and setup
* Responsive design with Tailwind classes
* Dark mode variant configuration

#### ✅ Outcome

✅ Set up Tailwind CSS project  
✅ Built responsive UI components with utility classes

</details>

---

### 🔹 Day 05

<details>
<summary>View Details</summary>

### 📅 Day 05 Progress – Portfolio Deployment 🚀

* Successfully deployed my portfolio website using Netlify 🌍
* Integrated contact form using Formspree 📧
* Fixed UI issues and improved design consistency 🎨
* Made the website fully responsive 📱
* Shared my portfolio on LinkedIn 💼

🔗 **Live Website:**  
https://sksohagkhan-portfolio.netlify.app/

</details>

---

<h3>🔹 Day 06</h3>

<details>
  <summary>▶ View Details</summary>

  <p>📘 Today I practiced advanced JavaScript concepts:</p>

  <ul>
    <li>Template Literals</li>
    <li>Destructuring (Array & Object)</li>
    <li>Spread Operator (...)</li>
    <li>Callback Functions</li>
    <li>Array Reduce()</li>
    <li>Promises (then, catch, finally)</li>
    <li>Fetch API (GitHub User Data)</li>
    <li>Scope & Closure</li>
  </ul>

  <pre><code>
// Example: Closure
function outerFun(){
  let outervariable = 10;

  function innerFun() {
    console.log(outervariable);
  }

  return innerFun;
}

const myclosure = outerFun();
myclosure(); // 10
  </code></pre>

</details>

<hr>
