from flask import Flask, render_template,request,redirect
import mysql.connector


# DATABASE CONNECTION
def initdb():
    conn = mysql.connector.connect(
        host="localhost",
        user="root",
        password="",
        database="student_db"
    )

    cursor = conn.cursor()

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS students (
            id INT AUTO_INCREMENT PRIMARY KEY,
            name VARCHAR(30) NOT NULL,
            age INT NOT NULL,
            course VARCHAR(20) NOT NULL,
            email VARCHAR(25) UNIQUE
        )
    """)

    conn.commit()

    cursor.close()
    conn.close()
initdb()

app = Flask(__name__)

@app.route("/")
def home():
    conn = mysql.connector.connect(
        host="localhost",
        user="root",
        password="",
        database="student_db"
    )

    cursor = conn.cursor()

    cursor.execute(
        "SELECT COUNT(*) FROM students"
    )

    total_students = cursor.fetchone()[0]

    cursor.close()
    conn.close()

    return render_template(
        "index.html",
        total_students=total_students
    )

@app.route("/add_student",methods = ["GET","POST"])
def add_student():
    if request.method == "POST":
        id = request.form["id"]
        name = request.form["name"]
        age = request.form["age"]
        course = request.form["course"]
        email = request.form["email"]

        conn = mysql.connector.connect(
            host="localhost",
            user="root",
            password="",
            database="student_db"
        )

        cursor = conn.cursor()

        query = "INSERT INTO students values (%s,%s,%s,%s,%s)"
        values = (id,name,age,course,email)

        cursor.execute(query,values)
        
        conn.commit()
        cursor.close()
        conn.close()

        return redirect("/students")

    return render_template("add_student.html")


@app.route("/students")
def students():

    search = request.args.get("search", "")

    conn = mysql.connector.connect(
        host="localhost",
        user="root",
        password="",
        database="student_db"
    )

    cursor = conn.cursor()

    if search:
        cursor.execute(
            "SELECT * FROM students WHERE name LIKE %s",
            (f"%{search}%",)
        )

    else:
        cursor.execute(
            "SELECT * FROM students"
        )

    students = cursor.fetchall()

    cursor.close()
    conn.close()

    return render_template(
        "students.html",
        students=students
    )

@app.route("/edit/<int:id>", methods=["GET", "POST"])
def edit_student(id):

    conn = mysql.connector.connect(
        host="localhost",
        user="root",
        password="",
        database="student_db"
    )

    cursor = conn.cursor()

    # UPDATE DATA
    if request.method == "POST":
        name = request.form["name"]
        age = request.form["age"]
        course = request.form["course"]
        email = request.form["email"]

        cursor.execute(
            """
            UPDATE students
            SET name=%s,
                age=%s,
                course=%s,
                email=%s
            WHERE id=%s
            """,
            (name, age, course, email, id)
        )

        conn.commit()

        cursor.close()
        conn.close()

        return redirect("/students")

    # GET STUDENT DATA
    cursor.execute(
        "SELECT * FROM students WHERE id=%s",
        (id,)
    )
    
    student = cursor.fetchone()

    cursor.close()
    conn.close()

    return render_template(
        "edit_student.html",
        student=student
    )

@app.route("/delete/<int:id>")
def delete_student(id):

    conn = mysql.connector.connect(
        host="localhost",
        user="root",
        password="",
        database="student_db"
    )

    cursor = conn.cursor()

    cursor.execute(
        "DELETE FROM students WHERE id=%s",
        (id,)
    )

    conn.commit()

    cursor.close()
    conn.close()

    return redirect("/students")
    


if __name__ == "__main__":
    app.run(debug=True)