from flask_app.config.mysqlconnection import connectToMySQL
from flask import flash

class Email:
    def __init__(self, data):
        self.id = data['id']
        self.email = data['email']

    
    @classmethod
    def create(cls, data):
        query = "INSERT INTO emails (email, created_at, updated_at) " \
        "VALUES (%(email)s, NOW(), NOW());"

        email_id = connectToMySQL("emails_schema").query_db(query, data)
        print(email_id, 'this is email id')
        return email_id



    @classmethod
    def get_emails(cls):
        query = "SELECT * FROM emails"
        emails = connectToMySQL("emails_schema").query_db(query)
        return emails
    
    @staticmethod
    # this function is used to validate emails
    # emailLength > 6
    def validate_email(post_data):
        print(post_data['email'], 'THIS IS POST DATA')


        emailString = str(post_data['email'])
        print(emailString, "THIS IS STRING THIS IS STRING")

        emailLength = len(emailString)
        print(emailLength, "THIS IS LENGTH THIS IS LENGTH")
        is_valid = True # we assume this is true

        if emailLength < 6:
            flash("Email must be longer")
            is_valid = False
            return is_valid
        
        print("RETURN TRUE", is_valid)
        return is_valid
