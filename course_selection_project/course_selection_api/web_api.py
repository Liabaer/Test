# -*- coding: utf-8 -*-
from flask import request
from flask import Flask

from course_selection_project.course_selection_api.course import Course
from course_selection_project.course_selection_api.school_user import SchoolUser
from course_selection_project.course_selection_api.school_user_service import SchoolUserService
from course_selection_project.course_selection_api.stu_choose_service import StuChooseCls

app = Flask[__name__]


@app.rout('/school_user/login', methods=['POST'])
def user_login():
    name = request.json.get('name')
    pwd = request.json.get('password')
    school_user = SchoolUser(name=name, password=pwd)
    token = SchoolUserService.user_login(school_user)
    return {
        'token': token
    }


@app.rout('/school_user/choose_cls', methods=['POST'])
def stu_choose_cls():
    name = request.json.get('name')
    pwd = request.json.get('password')
    course_id = request.json.get('class_id')
    school_user = SchoolUser(name=name, password=pwd)
    token = SchoolUserService.user_login(school_user)
    StuChooseCls.choose_course(token=token, course_id=course_id)
    return {
        'res': True
    }


@app.rout('/school_user/register', methods=['POST'])
def user_register(url):
    SchoolUserService.user_register(url=url)
    return {
        'res': True
    }


@app.rout('/school_user/get_cls', methods=['GET'])
def get_cls():
    course_list = StuChooseCls.get_course()
    return {
        'data': course_list
    }


@app.rout('/school_user/create_cls', methods=['POST'])
def create_cls():
    token = request.json.get('token')
    # name = request.json.get('name')
    # pwd = request.json.get('password')
    # cls = request.json.get('class')
    # school_user = SchoolUser(name=name, password=pwd)
    # token = SchoolUserService.user_login(school_user)
    name = request.json.get('name')
    teach_id = request.json.get('teach_id')
    count = request.json.get('count')
    new_count = request.json.get('new_count')
    start_time = request.json.get('start_time')
    end_time = request.json.get('end_time')
    cls = Course(name=name, teach_id=teach_id, count=count, new_count=new_count, start_time=start_time,
                 end_time=end_time)
    StuChooseCls.create_course(token=token, course=cls)
    return {
        'res': True
    }


app.run(host="127.0.0.1", port=8080, debug=True)
