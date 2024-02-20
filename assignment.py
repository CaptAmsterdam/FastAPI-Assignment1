from fastapi import FastAPI
from uuid import UUID


app = FastAPI()

students = {}

student_data = {"id": 0, "name": "", "age": 0, "sex": "", "height(CM)":0 }

@app.get("/")
def index():
    return {"message": "Hello Welcome to the Students Database"}


# Add a Students data
@app.post("/students")
def add_student(
    name: str, age: int, sex: str, Height: int
):
    new_student = student_data.copy()
    new_student["id"] = str(UUID(int=len(students) + 1))
    new_student["name"] = name
    new_student["age"] = age
    new_student["sex"] = sex
    new_student["height"] = Height

    students[new_student["id"]] = new_student

    return {"message": "Student data added successfully", "data": new_student}

#getting all student resource
@app.get("/students")
def get_students():
    return students


# getting a student resoure
@app.get("/students/{id}")
def get_student_by_id(id: str):
    student =students.get(id)
    if not student:
        return {"error": "Student not found"}
    
    return student


#updating the student Resource 
@app.put("/students/{id}")
def update_student(
    id: str, name: str, age: int, sex: str, Height: int
):
    student = students.get(id)
    if not student:
        return {"error": "Book not found"}
    
    student["name"] = name
    student["age"] = age
    student["sex"] = sex
    student["height"] = Height

    return {"message": "Student Data updated Successfully", "data": student}

#Delete a Student
@app.delete("/students/{id}")
def delete_student(id:str):
    student = students.get(id)
    if not student:
        return {"error": "Student Data not found"}
    
    del students[id]

    return {"message": "Student data deleted Successfully"}