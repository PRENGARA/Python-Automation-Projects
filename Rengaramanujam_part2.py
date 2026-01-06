##### FINAL - Part 2 #####
##### CSEC-380/480 - Kurt Wickboldt ####

'''
2) 10 Points: Flask/Jinja/Regex/Logging. See PDF for Instructions.
'''

from flask import Flask, render_template, request, redirect, url_for
import re
import logging


# Instantiate Flask app and setup logging
app = Flask(__name__
)

logging.basicConfig(
    filename='web_log.log',
    level = logging.DEBUG,
    format='%(asctime)s | %(levelname)s | %(message)s'
)
# Add Flask route that targets the root directory
@app.route('/')
def index():
    fields = {
        'first_name': {
            'name': 'firstname',
            'description': 'First Name:',
            'placeholder': 'Enter your first name'
        },
        'last_name': {
            'name': 'lastname',
            'description': 'Last Name:',
            'placeholder': 'Enter your last name'
        },
        'phone': {
            'name': 'phone',
            'description': 'Phone Number:',
            'placeholder': 'Enter your phone number'
        },
        'email': {
            'name': 'email',
            'description': 'Email Address:',
            'placeholder': 'Enter your email address'
        },
    }

    departments = [
        {'id': 'HR', 'name': 'Human Resources'},
        {'id': 'IT', 'name': 'Information Technology'},
        {'id': 'Finance', 'name': 'Finance'},
        {'id': 'Marketing', 'name': 'Marketing'},
        {'id': 'Sales', 'name': 'Sales'}
    ]

    # Logging debug message that states the template is being rendered
    logging.debug("Rendering Template...")
    # Render Jinja template
    return render_template('register.j2', fields=fields, departments=departments)


# Add Flask route that lets user post form data
@app.route('/register', methods=['POST'])
def register():
    # Get form data
    firstname = request.form.get('firstname', '')
    lastname = request.form.get('lastname', '')
    phone = request.form.get('phone', '')
    email = request.form.get('email', '')
    department = request.form.get('department', '')

    # Logging debug message that displays the collected form data
    logging.debug(
        f"Form Data | First Name: {firstname}, Last Name: {lastname}, "
        f"Phone: {phone}, Email: {email}, Department: {department}"
    )
    # Define email regex
    email_regex = r'^[\w\.-]+@[\w\.-]+\.\w+$'

    # Validate Email. If validation fails, call the error function and include an error message.
    # Logging error message that states the incorrect email.
    if not re.match(email_regex, email):
        logging.error(f"Email Regex did not match. Email Given: {email}")
        message = "Invalid email format. Please enter a valid email (e.g., user@domain.com)."
        return redirect(url_for('error', message=message))

    # Define phone regex
    phone_regex = r'^\d{10}$'

    # Validate Phone. If validation fails, call the error function and include an error message. 
    # Logging error message that states the incorrect phone number.
    if not re.match(phone_regex, phone):
        logging.error(f"Phone Regex did not match. Phone Given: {phone}")
        message = "Invalid phone number. Please enter a valid phone number."
        return redirect(url_for('error', message=message))


    # If all inputs are valid, redirect to root/index
    # Logging info message that states the user is registered successfully. (This is instead of performing a registration action)
    logging.info(
        f"User Registered! | First Name: {firstname}, Last Name: {lastname}, "
        f"Phone: {phone}, Email: {email}, Department: {department}"
    )
    return redirect(url_for('index'))


# Add a Flask route that displays an error if incorrect format is submitted
@app.route('/error')
def error():
    # Get error message from URL parameter
    # Logging info message stating the error template has been rendered
    # Render error HTML code that displays error message from parameter
    message = request.args.get(
        'message',
        'An error occurred. Please go back and correct your input.'
    )

    logging.info("Error template rendered")
    return render_template('error.j2', message=message)
if __name__ == '__main__':
    # Run webserver
    logging.info("Webserver is starting on http://127.0.0.1:5000")
    # Logging info message that states the webserver is running
    app.run(debug=True)