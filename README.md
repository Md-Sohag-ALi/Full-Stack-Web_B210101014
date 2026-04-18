# 📚 Learning Progress

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

## 🔹 Day 05
<details>
<summary>▶ View Details</summary>

### 📌 Topics Covered

#### 🎯 CSS Selectors
- Universal Selector (`*`)
- ID Selector (`#box`)
- Class Selector (`.heading`)

#### 🎯 Text Properties
- Text decoration (underline)
- Font weight (bold)
- Line height
- Text transform (capitalize)

#### 🎯 Box Model
- Width & Height
- Padding & Margin
- Border & Border-radius

#### 🎯 Display Property
- Inline
- Block
- None

#### 🎯 Opacity
- RGBA color transparency

#### 🎯 Positioning
- Relative Position
- Absolute Position
- Top, Left properties

#### 🎯 Z-index
- Layer control using z-index

#### 🎯 Flexbox
- `display: flex`
- `justify-content`
- `align-items`

#### 🎯 Background
- Background Image
- Background Size (cover)

#### 🎯 Transition
- Smooth hover effect
- Transform (scale)

#### 🎯 Animation
- `@keyframes`
- Infinite rotation (Loader)

#### 🎯 Media Queries (Responsive Design)
- Different screen sizes:
  - max-width: 300px
  - 300px–400px
  - 400px–600px
  - 600px+

</details>

---

### 🔹 Day 06
<details>
<summary>▶ View Details</summary>

#### 📘 Python Learning
This repository contains my Python learning practice organized by topics.

---

#### 📁 Project Files
- firstProgramme.py
- printSum.py
- Variables.py
- DataType.py
- TypeConversion.py
- Input in python.py
- Arithmetic operators.py
- String and conditional statements.py
- List in Python.py
- Tuple in python.py
- Dictionary and Set in python.py
- Practice.py

---

#### 📚 Topics Covered

**📌 First Programme**
```python
print("Hello World")

### 🔹 Day 06
<details>
<summary>▶ View Details</summary>

#### 📁 Files
- ExceptionHandling.py  
- File Basic.py  
- File_handling.py  
- Function.py  

---

#### 📚 Topics Covered

**🔸 Function**
- Function definition (`def`)
- Parameters & arguments
- Return values

**🔸 File Handling**
- open(), read(), write()
- File modes (`r`, `w`, `a`)
- with open() (best practice)

**🔸 Exception Handling**
- try-except block
- Multiple exceptions
- Common errors:
  - ZeroDivisionError
  - IndexError
  - FileNotFoundError
  - ValueError
- General exception (`Exception as e`)

---

#### 🧠 Practice
- Function তৈরি ও ব্যবহার  
- File read/write করা  
- Error handle করা  

---

#### 🚀 Conclusion
Today I learned how to write **clean, structured, and error-free Python programs** using functions, file handling, and exception handling.

</details>

## 🔹 Day 02

<details>
<summary>▶ View Details</summary>

### 🕒 Date & Time in Python

---

#### 💻 Code

```python
import datetime

# Current Date & Time
now = datetime.datetime.now().day
today = datetime.datetime.today()

print(now)
print(today)

# Custom Date
custom_date = datetime.datetime(2026,4,15,4,59,0)
print(custom_date, type(custom_date))

# Datetime → String
d1 = today.strftime("%Y/%M/%d %H:%M:%S")
d2 = today.strftime("%d,%B,%Y %H:%M:%S")
d3 = today.strftime("%d,%b,%Y %H:%M:%S")
d4 = today.strftime("%d,%b,%Y -%A %H:%M:%S")
d5 = today.strftime("%d,%b,%Y -%a %I:%M:%S %p")

print(d1)
print(d2)
print(d3)
print(d4)
print(d5)
print(type(d5))

# String → Datetime
date_str = "15,Apr,2026 -Wed 05:23:09 PM"
date_obj = datetime.datetime.strptime(date_str,"%d,%b,%Y -%a %I:%M:%S %p")
print(date_obj, type(date_obj))

# Date Arithmetic
from datetime import timedelta

today = datetime.datetime.today()

tommorow = today + timedelta(days=1)
yesterday = today - timedelta(days=1)
test = today + timedelta(hours=5)

print(tommorow)
print(yesterday)
print(test)

present = datetime.datetime.strptime("20 Apr 2026", "%d %b %Y")
prev = datetime.datetime.strptime("10 Apr 2026","%d %b %Y")

print(present - prev)
```

---

### 🌐 JSON & API (Python)

---

### 📁 Files

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

---

### 📚 Topics

* Date & Time in Python
* JSON (JavaScript Object Notation)
* Serialization & Deserialization
* CRUD Operations
* API using requests

---

### 💻 Code (API)

#### 🔹 Serialization

```python
import json
data = {"user_id":123,"post":"Hello","edit":True}
print(json.dumps(data, indent=4))
```

#### 🔹 Deserialization

```python
json_string = '{"user_id":123,"post":"Hello","edit":true}'
print(json.loads(json_string))
```

#### 🔹 GET

```python
import requests
print(requests.get("https://jsonplaceholder.typicode.com/posts").json())
```

#### 🔹 POST

```python
value = {"userId":1,"id":101,"title":"test","body":"test"}
print(requests.post("https://jsonplaceholder.typicode.com/posts", value).json())
```

#### 🔹 PATCH

```python
print(requests.patch("https://jsonplaceholder.typicode.com/posts/1", {"title":"test"}).json())
```

#### 🔹 PUT

```python
value = {"userId":1,"id":101,"title":"test","body":"test"}
print(requests.put("https://jsonplaceholder.typicode.com/posts/1", value).json())
```

#### 🔹 DELETE

```python
print(requests.delete("https://jsonplaceholder.typicode.com/posts/1").json())
```

---

### 🎯 Conclusion

* Learned Date & Time handling
* Practiced JSON conversion
* Understood CRUD & API

</details>

---

✍️ **Author:** Sk Sohag Khan
🎓 CSE Student | Future Full Stack Developer 🚀
