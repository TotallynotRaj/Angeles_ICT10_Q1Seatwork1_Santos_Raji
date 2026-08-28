from pyscript import document 
 
 
name = "Raji Santos" 
age = 15 
height = 157.48 
countries_visit_ = ["Japan", "Korea", "America"] 
student_type = True 
student_info = {"color": "Blue", "car_brand": "Nissan", "shoe_size": 9.5, "best_friend": "Lucas Tanglao"} 
fruits = {"Apple", "Grapes", "Orange", "Banana", "Mango"} 
days = ("Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday") 
 
# name = string
# age = integer
# height = float
# countries_visit_ = list
# student_type = boolean
# student_info = dictionary
# fruits = set
# days = tuple
 
output = f""" 
<p> name= {name} {type(name).__name__} </p> 
<p> age= {age} {type(age).__name__} </p> 
<p> height= {height} {type(height).__name__} </p> 
<p> countries_visit_= {countries_visit_} {type(countries_visit_).__name__} </p> 
<p> student_type= {student_type} {type(student_type).__name__} </p> 
<p> student_info= {student_info} {type(student_info).__name__} </p> 
<p> fruits= {fruits} {type(fruits).__name__} </p> 
<p> days= {days} {type(days).__name__} </p> 
""" 
document.querySelector("#output").innerHTML = output