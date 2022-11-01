def is_similar_with(name1, name2):
    if name1 == name2:
        return True

    if not len(name1) == len(name2):
        return False

    difference = 0
    for idx, chr in enumerate(name1):
        if not chr.lower() == name2[idx].lower():
            difference += 1

    if difference > 1:
        return False

    return True

cl = input().split()

n = int(cl[0])
m = int(cl[1])

secret_classes = []
student = []
message = []

# Initialize secret courses
for i in range(n):
    secret_classes.append([])

# Collect messages
for i in range(m):
    student_message = input()
    message.append(student_message)

# Parse messages
for m in message:
    course, name = m.split(" ")
    course_idx = int(course) - 1
    
    # When enrolled names are empty
    if not secret_classes[course_idx]:
        #print("h", secret_classes[course_idx])
        secret_classes[course_idx].append(name)
        #print("e", secret_classes[course_idx])
        #print("here", secret_classes)
        continue

    # When enrolled names are not empty
    is_enrolled = False
    for enrolled_names in secret_classes[course_idx]:
        #print("enrolled name: ", enrolled_names, name, is_similar_with(enrolled_names, name))
        if not is_similar_with(name, enrolled_names):
            is_enrolled = True
            #print(secret_classes)
        
    if is_enrolled:
        secret_classes[course_idx].append(name)

# Print the result
for enrolled_names_by_course in secret_classes:
    print(" ".join(enrolled_names_by_course))
