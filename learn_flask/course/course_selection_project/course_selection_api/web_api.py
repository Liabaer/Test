# -*- coding: utf-8 -*-
from flask import request
from flask import Flask

from learn_flask.course.course_selection_project.course_selection_api.course import Course
from learn_flask.course.course_selection_project.course_selection_api.school_user import SchoolUser
from learn_flask.course.course_selection_project.course_selection_api.school_user_service import SchoolUserService
from learn_flask.course.course_selection_project.course_selection_api.stu_choose_service import StuChooseCls

app = Flask(__name__)


@app.route('/school_user/login', methods=['POST'])
def user_login():
    id = request.json.get('id')
    name = request.json.get('name')
    pwd = request.json.get('password')
    school_user = SchoolUser(id=id, name=name, password=pwd)
    token = SchoolUserService.user_login(school_user)
    return {
        'token': token
    }


@app.route('/school_user/choose_cls', methods=['POST'])
def stu_choose_cls():
    token = request.json.get('token')
    course_id = request.json.get('class_id')
    StuChooseCls.choose_course(token=token, course_id=course_id)
    return {
        'res': True
    }


@app.route('/school_user/register', methods=['POST'])
def user_register():
    url = request.json.get('url')
    SchoolUserService.user_register(url=url)
    return {
        'res': True
    }


@app.route('/school_user/get_cls', methods=['GET'])
def get_cls():
    course_list = StuChooseCls.get_course()
    return {
        'data': course_list
    }


@app.route('/school_user/create_cls', methods=['POST'])
def create_cls():
    token = request.json.get('token')
    name = request.json.get('name')
    teach_id = request.json.get('teach_id')
    count = request.json.get('count')
    start_time = request.json.get('start_time')
    end_time = request.json.get('end_time')
    cls = Course(name=name, teach_id=teach_id, count=count, start_time=start_time,
                 end_time=end_time)
    StuChooseCls.create_course(token=token, course=cls)
    return {
        'res': True
    }


app.run(host="127.0.0.1", port=8080, debug=True)
