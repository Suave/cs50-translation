# Parse first line
t = input("How many are students and events?\(2 integers, and seperate by space\) ")
student_n, event_m = t.split(" ")
student_n = int(student_n)
event_m = int(event_m)
print("Students", student_n)
print("Total Events", event_m)

# Parse second line
groups = input("Input students' group arragement: ").split(" ")
print(groups)

# Input 3~N lines
events = []
n = 0
while n < event_m:
    events.append(input("Input event: "))
    n += 1
print(events)

# Parse events
score = {"A": 0, "B": 0}
for e in events:
    print("Event is ", e)
    action_group = e.split(" ")
    print(score)
    if action_group[0] == "cite":
        author = action_group[1]
        cited = action_group[2]
        author_group = groups[int(author)-1] # 'A' or 'B'
        cited_group = groups[int(cited)-1]
        if author_group == cited_group:
            score[author_group] += 1
        else:
            score[cited_group] += 5
    elif action_group[0] == "change":
        author = action_group[1]
        author_group = groups[int(author)-1] # 'A' or 'B'
        if author_group == "A":
            groups[int(author)-1] = "B"
        elif author_group == "B":
            groups[int(author)-1] = "A"
        print(groups)
print(score)