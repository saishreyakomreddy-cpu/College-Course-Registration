from flask import Flask, render_template, request

app = Flask(__name__)

courses = {
    "A": {
        "name": "AI",
        "capacity": 50,
        "fee": 5000,
        "students": []
    },
    "B": {
        "name": "ML",
        "capacity": 40,
        "fee": 4500,
        "students": []
    },
    "C": {
        "name": "CN",
        "capacity": 45,
        "fee": 4800,
        "students": []
    },
    "D": {
        "name": "APP",
        "capacity": 35,
        "fee": 5200,
        "students": []
    },
    "E": {
        "name": "JAVA",
        "capacity": 30,
        "fee": 4700,
        "students": []
    },
    "F": {
        "name": "DL",
        "capacity": 25,
        "fee": 5300,
        "students": []
    }
}


@app.route("/", methods=["GET", "POST"])
def index():
    student_id = request.form.get("student_id", "").strip()
    student_name = request.form.get("student_name", "").strip()
    year = request.form.get("year", "").strip()
    dept = request.form.get("dept", "").strip()
    section = request.form.get("section", "").strip()
    cgpa = request.form.get("cgpa", "").strip()

    try:
        cgpa_value = float(cgpa) if cgpa else None
    except ValueError:
        cgpa_value = None

    message = ""
    message_type = ""

    action = request.form.get("action")
    course_id = request.form.get("course_id")

    if request.method == "POST":
        if action == "register":
            if not student_id or not student_name or not year or not dept or not section or cgpa == "":
                message = "Please complete all student details before registering."
                message_type = "error"
            elif cgpa_value is None or cgpa_value < 7.5:
                message = "Registration not allowed: CGPA must be at least 7.5."
                message_type = "error"
            elif course_id not in courses:
                message = "Invalid course selected."
                message_type = "error"
            else:
                course = courses[course_id]
                if student_id in course["students"]:
                    message = f"You are already registered for {course['name']}."
                    message_type = "warning"
                elif len(course["students"]) >= course["capacity"]:
                    message = f"{course['name']} is full. Please choose another course."
                    message_type = "error"
                else:
                    course["students"].append(student_id)
                    message = f"Successfully registered for {course['name']}!"
                    message_type = "success"

        elif action == "drop":
            if not student_id or not student_name:
                message = "Please enter your student details before dropping a course."
                message_type = "error"
            elif course_id not in courses:
                message = "Invalid course selected."
                message_type = "error"
            else:
                course = courses[course_id]
                if student_id in course["students"]:
                    course["students"].remove(student_id)
                    message = f"Successfully dropped {course['name']}."
                    message_type = "success"
                else:
                    message = f"You are not registered for {course['name']} ."
                    message_type = "warning"

        elif action is None:
            if not student_id and not student_name and not year and not dept and not section and not cgpa:
                message = ""
            elif not student_id or not student_name or not year or not dept or not section or not cgpa:
                message = "Student ID, name, year, department, section, and CGPA are required."
                message_type = "error"
            elif cgpa_value is not None and cgpa_value < 7.5:
                message = "CGPA must be at least 7.5 to continue."
                message_type = "error"
            else:
                message = "Student information saved successfully."
                message_type = "success"

    registered_courses = []
    total_fee = 0
    if student_id:
        for course_key, course in courses.items():
            if student_id in course["students"]:
                course_data = {
                    "id": course_key,
                    "name": course["name"],
                    "fee": course["fee"]
                }
                registered_courses.append(course_data)
                total_fee += course["fee"]

    return render_template(
        "index.html",
        courses=courses,
        student_id=student_id,
        student_name=student_name,
        year=year,
        dept=dept,
        section=section,
        cgpa=cgpa,
        registered_courses=registered_courses,
        total_fee=total_fee,
        message=message,
        message_type=message_type,
    )


if __name__ == "__main__":
    app.run(debug=True)