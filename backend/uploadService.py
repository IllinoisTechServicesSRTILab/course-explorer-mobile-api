import requests
import pandas
import time

#upload course information if any new course is added
#c_dict = {
#    'course_name':""
#}
#course = pandas.read_csv('uiuc_course.csv')
#for i in range(len(course)):
#    c = course.iloc[i]
#    course_id = c[0] + str(c[1])
#    c_dict['course_name'] = c[2]
#    requests.post("http://127.0.0.1:5000/course/" + course_id, json=c_dict)
#    time.sleep(2)

##upload the grade for new term. update the course avg, student avg and professor avg
df = pandas.read_csv('uiuc-gpa-dataset.csv')
a_plus = 4.0
a = 4.0
a_minus = 3.67
b_plus = 3.33
b = 3
b_minus = 2.67
c_plus = 2.33
c = 2
c_minus = 1.67
d_plus = 1.33
d = 1
d_minus = 0.67
f=0

grade_scale = [a_plus,a,a_minus,b_plus,b,b_minus,c_plus,c,c_minus,d_plus,d,d_minus,f]

dict_term={'professor_name':"",
           "term_avg":0.00,
           'term_name':"",
           'term_students':0,
           'A':0,
           'B':0,
           'C':0,
           'D':0,
           'F':0}

for i in range(10,100):
    entry = df.iloc[i]
    term_pts = 0
    student_count = 0
    for j in range(6, 19):
        term_pts += grade_scale[j - 6] * entry[j]
        student_count += entry[j]
    dict_term['term_avg'] = term_pts / student_count
    dict_term['A'] = sum(entry[6:9])
    dict_term['B'] = sum(entry[9:12])
    dict_term['C'] = sum(entry[12:15])
    dict_term['D'] = sum(entry[15:18])
    dict_term['F'] = entry[18]
    dict_term['professor_name'] = entry[20]
    dict_term['term_name'] = entry[2]
    dict_term['term_students'] = student_count
    course_id = entry['Subject'] + str(int(entry['Number']))
    #print(course_id)
    requests.post("http://127.0.0.1:5000/course/professor/"+course_id, json=dict_term)
    time.sleep(1)
