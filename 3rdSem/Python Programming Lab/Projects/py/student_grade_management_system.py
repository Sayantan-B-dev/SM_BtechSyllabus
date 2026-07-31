# =====================================================
#  STUDENT GRADE MANAGEMENT SYSTEM  (menu-driven project)
#  Add / View / Search / Update / Delete student grades
# =====================================================

WIDTH = 100

BANNER = r"""
███████╗████████╗██╗   ██╗██████╗ ███████╗███╗   ██╗████████╗
██╔════╝╚══██╔══╝██║   ██║██╔══██╗██╔════╝████╗  ██║╚══██╔══╝
███████╗   ██║   ██║   ██║██║  ██║█████╗  ██╔██╗ ██║   ██║   
╚════██║   ██║   ██║   ██║██║  ██║██╔══╝  ██║╚██╗██║   ██║   
███████║   ██║   ╚██████╔╝██████╔╝███████╗██║ ╚████║   ██║   
╚══════╝   ╚═╝    ╚═════╝ ╚═════╝ ╚══════╝╚═╝  ╚═══╝   ╚═╝
 ██████╗ ██████╗  █████╗ ██████╗ ███████╗
██╔════╝ ██╔══██╗██╔══██╗██╔══██╗██╔════╝
██║  ███╗██████╔╝███████║██║  ██║█████╗  
██║   ██║██╔══██╗██╔══██║██║  ██║██╔══╝  
╚██████╔╝██║  ██║██║  ██║██████╔╝███████╗
 ╚═════╝ ╚═╝  ╚═╝╚═╝  ╚═╝╚═════╝ ╚══════╝
███╗   ███╗ █████╗ ███╗   ██╗ █████╗  ██████╗ ███████╗███╗   ███╗███████╗███╗   ██╗████████╗
████╗ ████║██╔══██╗████╗  ██║██╔══██╗██╔════╝ ██╔════╝████╗ ████║██╔════╝████╗  ██║╚══██╔══╝
██╔████╔██║███████║██╔██╗ ██║███████║██║  ███╗█████╗  ██╔████╔██║█████╗  ██╔██╗ ██║   ██║   
██║╚██╔╝██║██╔══██║██║╚██╗██║██╔══██║██║   ██║██╔══╝  ██║╚██╔╝██║██╔══╝  ██║╚██╗██║   ██║   
██║ ╚═╝ ██║██║  ██║██║ ╚████║██║  ██║╚██████╔╝███████╗██║ ╚═╝ ██║███████╗██║ ╚████║   ██║   
╚═╝     ╚═╝╚═╝  ╚═╝╚═╝  ╚═══╝╚═╝  ╚═╝ ╚═════╝ ╚══════╝╚═╝     ╚═╝╚══════╝╚═╝  ╚═══╝   ╚═╝
███████╗██╗   ██╗███████╗████████╗███████╗███╗   ███╗
██╔════╝╚██╗ ██╔╝██╔════╝╚══██╔══╝██╔════╝████╗ ████║
███████╗ ╚████╔╝ ███████╗   ██║   █████╗  ██╔████╔██║
╚════██║  ╚██╔╝  ╚════██║   ██║   ██╔══╝  ██║╚██╔╝██║
███████║   ██║   ███████║   ██║   ███████╗██║ ╚═╝ ██║
╚══════╝   ╚═╝   ╚══════╝   ╚═╝   ╚══════╝╚═╝     ╚═╝
"""

# ---------- BOX DRAWING ----------
def box_top(w=WIDTH):
    return "+" + "-" * (w - 2) + "+"

def box_bottom(w=WIDTH):
    return "+" + "-" * (w - 2) + "+"

def box_divider(w=WIDTH):
    return "+" + "-" * (w - 2) + "+"

def box_line(text, w=WIDTH):
    pad = max(w - 4 - len(text), 0)
    return f"| {text}{' ' * pad} |"

def print_boxed(lines, w=WIDTH):
    print(box_top(w))
    for line in lines:
        print(box_line(line, w))
    print(box_bottom(w))

# ---------- DATA ----------
STUDENTS = {}

SUBJECTS = ["Python", "DBMS", "COA"]

# ---------- GRADE FUNCTIONS ----------
def calculate_grade(percentage):
    if percentage >= 90:
        return "A+"
    elif percentage >= 80:
        return "A"
    elif percentage >= 70:
        return "B+"
    elif percentage >= 60:
        return "B"
    elif percentage >= 50:
        return "C"
    elif percentage >= 40:
        return "D"
    else:
        return "F"

def add_student(roll, name, marks):
    STUDENTS[roll] = {"name": name, "marks": marks}

def get_report(roll):
    student = STUDENTS[roll]
    total = sum(student["marks"].values())
    max_total = 100 * len(SUBJECTS)
    percentage = (total / max_total) * 100
    grade = calculate_grade(percentage)
    return student, total, percentage, grade

def format_report(roll):
    student, total, percentage, grade = get_report(roll)
    lines = [
        f"  Roll no  : {roll}",
        f"  Name     : {student['name']}",
        "",
    ]
    for subject in SUBJECTS:
        lines.append(f"  {subject:<10}: {student['marks'].get(subject, 0)}")
    lines.append("")
    lines.append(f"  Total         : {total}")
    lines.append(f"  Percentage    : {percentage:.2f}%")
    lines.append(f"  Grade         : {grade}")
    return lines

# ---------- MENU ----------
def main():
    print(BANNER)
    print("      Terminal Student Grade Management System".center(WIDTH))
    print()

    while True:
        print_boxed([
            "  [1] Add Student",
            "  [2] View All Students",
            "  [3] Search Student",
            "  [4] Update Marks",
            "  [5] Delete Student",
            "  [6] Exit"
        ])
        option = input("> Enter option: ").strip()

        if option == "1":
            roll = input("> Enter roll number: ").strip()
            if roll in STUDENTS:
                print()
                print_boxed(["ERROR: Roll number already exists."])
                print()
                continue
            name = input("> Enter student name: ").strip()
            marks = {}
            for subject in SUBJECTS:
                try:
                    value = float(input(f"> Enter marks in {subject} (out of 100): ").strip())
                    if not 0 <= value <= 100:
                        print_boxed([f"ERROR: Marks for {subject} must be between 0 and 100."])
                        print()
                        value = -1
                        break
                    marks[subject] = value
                except ValueError:
                    print_boxed([f"ERROR: Invalid marks for {subject}."])
                    print()
                    value = -1
                    break
            if -1 in marks.values() or len(marks) != len(SUBJECTS):
                continue
            add_student(roll, name, marks)
            print()
            print_boxed([
                "STUDENT ADDED:",
                "",
                f"  Roll no : {roll}",
                f"  Name    : {name}"
            ])
            print()

        elif option == "2":
            if not STUDENTS:
                print()
                print_boxed(["No students registered yet."])
                print()
                continue
            lines = [f"  {'Roll':<12}{'Name':<20}{'Total':<8}{'Percent':<12}{'Grade':<6}",
                     "-" * (WIDTH - 8)]
            for roll in STUDENTS:
                _, total, percentage, grade = get_report(roll)
                lines.append(f"  {roll:<12}{STUDENTS[roll]['name']:<20}{total:<8}{percentage:<12.2f}{grade:<6}")
            print()
            print_boxed(lines)
            print()

        elif option == "3":
            roll = input("> Enter roll number: ").strip()
            if roll not in STUDENTS:
                print()
                print_boxed(["ERROR: Student not found."])
                print()
                continue
            print()
            print_boxed(format_report(roll))
            print()

        elif option == "4":
            roll = input("> Enter roll number: ").strip()
            if roll not in STUDENTS:
                print()
                print_boxed(["ERROR: Student not found."])
                print()
                continue
            subject = input(f"> Enter subject to update ({', '.join(SUBJECTS)}): ").strip()
            if subject not in SUBJECTS:
                print()
                print_boxed(["ERROR: Invalid subject."])
                print()
                continue
            try:
                value = float(input(f"> Enter new marks in {subject} (out of 100): ").strip())
                if not 0 <= value <= 100:
                    print_boxed(["ERROR: Marks must be between 0 and 100."])
                    print()
                    continue
            except ValueError:
                print_boxed(["ERROR: Invalid marks."])
                print()
                continue
            STUDENTS[roll]["marks"][subject] = value
            print()
            print_boxed([
                "MARKS UPDATED:",
                "",
                f"  {subject} = {value}"
            ])
            print()

        elif option == "5":
            roll = input("> Enter roll number: ").strip()
            if roll not in STUDENTS:
                print()
                print_boxed(["ERROR: Student not found."])
                print()
                continue
            del STUDENTS[roll]
            print()
            print_boxed([f"Student {roll} deleted successfully."])
            print()

        elif option == "6":
            print()
            print_boxed(["Goodbye!"])
            print()
            break

        else:
            print_boxed(["Invalid option, try again."])
            print()

if __name__ == "__main__":
    main()
