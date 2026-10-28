emp1_skills = {"Python", "SQL", "Excel"}
emp2_skills = {"Python", "Java", "AWS"}
print("Common skills:", emp1_skills & emp2_skills)
print("Unique to Employee 1:", emp1_skills - emp2_skills)
print("Unique to Employee 2:", emp2_skills - emp1_skills)
print("All available skills:", emp1_skills | emp2_skills)