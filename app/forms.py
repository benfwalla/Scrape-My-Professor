from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, SelectField


class CourseForm(FlaskForm):
    department = SelectField('Department')
    course_subject = StringField('Course Subject')
    course_number = StringField('Course Number')
    class_number = StringField('Class Number')
    instructor = StringField('Instructor')
    submit = SubmitField('Search')
