#Scenario 1: You are a teacher and you have given your students a test. You want to calculate the total of their test scores.
#List of student_scores
student_scores = [150,142,185,120,171,184,149,24,59,68,199,78,65,89,86,55,91,64,89]

#sum of student_scores
total_exam_score = sum(student_scores)    #Result: 2068



#sum of student_scores with for loop
sum = 0
for score in student_scores:
     sum += score
print(sum)                                #Result: 2068


#Scenario 2: You are a teacher and you have given your students a test. You want to calculate the max of their test scores.
#List of student_scores
student_scores = [150,142,185,120,171,184,149,24,59,68,199,78,65,89,86,55,91,64,89]

print(max(student_scores))              #Result: 199




#max of student_scores with for loop
max_score = 0

for score in student_scores:
       if score > max_score:
           max_score = score
print(max_score)                        #Result: 199 
   
