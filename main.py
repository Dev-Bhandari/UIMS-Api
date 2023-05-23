from uims_api import SessionUIMS
from uims_api.config import configChecker
from uims_api.exceptions import *
from flask import Flask, request, jsonify
import os

app = Flask(__name__)
Flask.secret_key = os.urandom(12).hex()


@app.route('/api/attendance', methods=['GET', 'POST'])
def attendance():
    if request.method == 'POST':
        UID = request.args.get('uid')
        Password = request.args.get('password')
    try:
        account = SessionUIMS(UID, Password)
    except Exception as e:
        if e.__class__ == IncorrectCredentialsError:
            return jsonify({'error': 'Incorrect Credentials'})
        elif e.__class__ == IncorrectCaptcha:
            return jsonify({'error': 'Incorrect Captcha'})

    try:
        userAttendance = account.attendance
    except Exception as e:
        if e.__class__ == UIMSInternalError:
            return jsonify({'error': 'UIMS Internal Error'})
        else:
            return jsonify({'error': 'Something went wrong'})
    return jsonify(userAttendance)


@app.route('/api/full_attendance', methods=['GET', 'POST'])
def full_attendance():
    if request.method == 'POST':
        UID = request.args.get('uid')
        Password = request.args.get('password')
    try:
        account = SessionUIMS(UID, Password)
    except Exception as e:
        if e.__class__ == IncorrectCredentialsError:
            return jsonify({'error': 'Incorrect Credentials'})
        elif e.__class__ == IncorrectCaptcha:
            return jsonify({'error': 'Incorrect Captcha'})

    try:
        userFullAttendance = account.full_attendance
    except Exception as e:
        if e.__class__ == UIMSInternalError:
            return jsonify({'error': 'UIMS Internal Error'})
        else:
            return jsonify({'error': 'Something went wrong'})
    return jsonify(userFullAttendance)


@app.route('/api/timetable', methods=['GET', 'POST'])
def timetable():
    if request.method == 'POST':
        UID = request.args.get('uid')
        Password = request.args.get('password')
    try:
        account = SessionUIMS(UID, Password)
    except Exception as e:
        if e.__class__ == IncorrectCredentialsError:
            return jsonify({'error': 'Incorrect Credentials'})
        elif e.__class__ == IncorrectCaptcha:
            return jsonify({'error': 'Incorrect Captcha'})

    try:
        userTimetable = account.timetable
    except Exception as e:
        if e.__class__ == UIMSInternalError:
            return jsonify({'error': 'UIMS Internal Error'})
        else:
            return jsonify({'error': 'Something went wrong'})
    return jsonify(userTimetable)


@app.route('/api/full_name', methods=['GET', 'POST'])
def full_name():
    if request.method == 'POST':
        UID = request.args.get('uid')
        Password = request.args.get('password')
    try:
        account = SessionUIMS(UID, Password)
    except Exception as e:
        if e.__class__ == IncorrectCredentialsError:
            return jsonify({'error': 'Incorrect Credentials'})
        elif e.__class__ == IncorrectCaptcha:
            return jsonify({'error': 'Incorrect Captcha'})

    try:
        userName = account.full_name
    except Exception as e:
        if e.__class__ == UIMSInternalError:
            return jsonify({'error': 'UIMS Internal Error'})
        else:
            return jsonify({'error': 'Something went wrong'})
    return jsonify({'name': userName})


if __name__ == '__main__':
    app.run(debug=True)
