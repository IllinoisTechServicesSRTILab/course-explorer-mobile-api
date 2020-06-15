from flask import Response,request
from test.main.datasource.grademodel import Course,Professor
from flask_restx import Resource
from .dto import CourseDto
from bson import json_util

api = CourseDto.api


@api.route('/<course_id>')
@api.param('course_id')
@api.response(404, 'course not found.')
class CourseControl(Resource):
    def get(self, course_id):
        try:
            _course = Course.objects.get(course_id=course_id).to_json()
            #json_util.loads(_course.to_json())
            return Response(_course, mimetype="application/json", status=200)
        except Course.DoesNotExist:
            api.abort(404)

    def post(self,course_id):
        course_document = Course(
            course_id=course_id,
            course_name=request.json['course_name'],
            avg_gpa=0,
            professors=[],
        )
        course_document.save()
        return Response("Successfully added course", status=200)


@api.route('/professor/<course_id>')
@api.param('course_id')
@api.response(404, 'course not found.')
class TermControl(Resource):
    def post(self,course_id):
        try:
            _course = Course.objects.get(course_id=course_id)
            _professor = _course.professors.filter(professor_name=request.json['professor_name']).first()
            #if the professor has not been created
            if _professor == None:
                _course.professors.create(professor_name=request.json['professor_name'],professor_avg=0)
                _professor = _course.professors.filter(professor_name=request.json['professor_name']).first()
            _term = _professor.terms.filter(term_name=request.json['term_name']).first()
            #if the term has not been created
            if _term == None:
                _professor.terms.create(
                    term_name=request.json['term_name'],
                    A=request.json['A'],
                    B=request.json['B'],
                    C=request.json['C'],
                    D=request.json['D'],
                    F=request.json['F'],
                )
            else:
                _term.A=request.json['A']+_term.A
                _term.B=request.json['B']+_term.B
                _term.C=request.json['C']+_term.C
                _term.D=request.json['D']+_term.D
                _term.F=request.json['F']+_term.F
            #update professor_avg and course_avg
            p_student = _professor.professor_students
            new_avg = (p_student*_professor.professor_avg+request.json['term_avg']*request.json['term_students'])/(p_student+request.json['term_students'])
            _professor.professor_avg=new_avg
            _professor.professor_students=p_student+request.json['term_students']
            c_student = _course.course_students
            new_c_avg = (c_student*_course.avg_gpa+request.json['term_avg']*request.json['term_students'])/(c_student+request.json['term_students'])
            _course.update(course_students=c_student+request.json['term_students'], avg_gpa=new_c_avg)
            _course.save()
        except Course.DoesNotExist:
            api.abort(404)










