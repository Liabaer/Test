# -*- coding: utf-8 -*-
from flask import Flask, request

from course_selection_project.course_selection_api.book import Book
from course_selection_project.course_selection_api.book_service import BookService
from course_selection_project.course_selection_api.student_card import StudentCard
from course_selection_project.course_selection_api.student_service import StudentService

app = Flask(__name__)


@app.route('/create_book', methods=['POST'])
def create_book():
    name = request.json.get('name')
    book_category = request.json.get('book_category')
    count = request.json.get('count')
    book = Book(book_category=book_category, name=name, count=count)
    res = BookService.create_book(book)
    return {
        'res': True
    }


@app.route('/create_book_cate', methods=['POST'])
def create_category():
    # book_category = request.json.get('book_cate')
    name = request.json.get('name')
    book_category = request.json.get('book_category')
    count = request.json.get('count')
    bc = Book(book_category=book_category, name=name, count=count)
    res = BookService.create_book_category(bc)
    return {
        'res': res
    }


@app.route('/create_card', methods=['POST'])
def create_card():
    name = request.json.get('name')
    amount = request.json.get('amount')
    card = StudentCard(amount=amount, name=name)
    StudentService.create_card(card)
    return {
        'res': True
    }


@app.route('/use_card', methods=['POST'])
def use_card():
    type = request.json.get('type')
    amount = request.json.get('amount')
    card_id = request.json.get('card_id')
    StudentService.use_card(type=type, amount=amount, card_id=card_id)
    return {
        'res': True
    }


@app.route('/borrow', methods=['POST'])
def borrow():
    book_id = request.json.get('book_id')
    card_id = request.json.get('card_id')
    StudentService.borrow_book(book_id=book_id, card_id=card_id)
    return {
        'res': True
    }


@app.route('/return_book', methods=['POST'])
def return_book():
    book_id = request.json.get('book_id')
    card_id = request.json.get('card_id')
    StudentService.return_book(book_id=book_id, card_id=card_id)
    return {
        'res': True
    }


app.run(host='127.0.0.1', port=8080, debug=True)
