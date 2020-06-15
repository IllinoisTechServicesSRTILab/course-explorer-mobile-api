from flask_restx import Namespace, fields


class CourseDto:
    api = Namespace('course')
    term = api.model('term',
                     {
                         'term_name': fields.String(required=True),
                         'A':fields.Integer(),
                         'B':fields.Integer(),
                         'C': fields.Integer(),
                         'D': fields.Integer(),
                         'F': fields.Integer(),
                     }
                     )

    professor = api.model('professor',
                          {
                              'professor_name': fields.String(required=True),
                              'professor_avg': fields.Float(),
                              'terms': fields.List(fields.Nested(term)),

                          }
                          )

    course = api.model('course',
              {
                  'course_id': fields.String(required=True),
                  'course_name': fields.String(required=True),
                  'avg_gpa': fields.Float(),
                  'professors': fields.List(fields.Nested(professor)),
              })
