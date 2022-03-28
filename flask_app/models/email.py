from flask_app.config.mysqlconnection import connectToMySQL
import re
from flask import flash

EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')

class Email:
    def __init__(self, data):
        self.id = data['id']
        self.email = data['email']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']

    @classmethod
    def create_email(cls,data):
        query = 'INSERT INTO emails (email, created_at, updated_at) VALUES(%(email)s, NOW(), NOW());'
        results = connectToMySQL('email_schema').query_db(query, data)
        return results

    @classmethod
    def get_all_emails(cls):
        query = 'SELECT  * FROM emails ORDER BY id DESC;'
        results = connectToMySQL('email_schema').query_db(query)
        emails = []
        print(emails)
        for row in results:
            emails.append(cls(row))
        return emails

    @classmethod
    def delete_email(cls, data):
        query = 'DELETE FROM emails WHERE id = %(id)s;'
        results = connectToMySQL('email_schema').query_db(query, data)
        return results


    @staticmethod
    def validate(email):
        query = 'SELECT * FROM emails WHERE email = %(email)s;'
        results = connectToMySQL('email_schema').query_db(query, email)
        is_valid = True
        if not EMAIL_REGEX.match(email['email']):
            flash('Invalid email!', 'email')
            is_valid = False
        if len(results) >= 1:
            flash ('Email is already being used!', 'email')
            is_valid = False
        return is_valid