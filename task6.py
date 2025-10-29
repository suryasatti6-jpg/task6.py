def writefile(filename):
f=open("log.txt ","w")
f.write("Error objects are thrown when runtime errors occur. The Error object can also be used as a base object for user-defined exceptions ")
f.close()
def readfile(filename):
with open(filename, "r") as file: 
content = file.read() 
print(content)
writefile("write")
readfile("text")
 
 def write_employee_report(filename):
    employees = [
        {"name": "Alice", "department": "HR"},
        {"name": "Bob", "department": "Engineering"},
        {"name": "Charlie", "department": "Finance"}
    ]
    
    with open(filename, "w") as file:
        for employee in employees:
            line = f"Name: {employee['name']}, Department: {employee['department']}\n"
            file.write(line)

# Example usage:
write_employee_report("employee_report.txt")
