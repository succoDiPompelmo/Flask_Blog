import os
import string
import random
from PIL import Image
from flask import current_app
from flask_mail import Message
from flaskblog import mail


def id_generator(size=6, chars=string.ascii_uppercase + string.digits):
    return ''.join(random.choice(chars) for _ in range(size))


def save_picture(form_picture):
    random_hex = id_generator(8)
    _, f_ext = os.path.splitext(form_picture.filename)
    picture_filename = random_hex + f_ext
    picture_path = os.path.join(current_app.root_path, 'static/profile_pics', picture_filename)

    output_size = (125, 125)
    i = Image.open(form_picture)
    i.thumnail(output_size)

    i.save(picture_path)

    return picture_filename


def send_reset_email(user):
    token = user.get_reset_token()
    msg = Message('Password Reset Request',
                  sender='noreply@demo.com',
                  recipients=[user.email])
    msg.body = ""
    mail.send(msg)