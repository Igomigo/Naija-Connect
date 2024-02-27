import os
import secrets
from PIL import Image
from application import mail
from flask import url_for, current_app
from flask_mail import Message


def save_picture(form_picture):
    """
       Function that takes the form picture as argument and generates a
       unique secret hexadecimal string to form the picture name together with the
       image file extention, it creates a file path and saves the image to
       that path. It then finally returns the uniquely created picture name.
    """
    random_hex = secrets.token_hex(8)
    _, f_ext = os.path.splitext(form_picture.filename)
    picture_fn = random_hex + f_ext
    picture_path = os.path.join(current_app.root_path, 'static/profile_pics',
                                picture_fn)

    # resize the image to perfectly sit in the profile's dp
    """output_size = (125, 125)
    i = Image.open(form_picture)
    i.thumbnail(output_size)
    i.save(picture_path)"""

    form_picture.save(picture_path)
    return picture_fn


def send_reset_email(user):
    """
       This function calls the class method that generates the token from
       the user id and uses this token to send a message that contains the
       password reset link.
    """
    token = user.get_reset_token()
    msg = Message('Password Reset Request',
                  sender='igomigofatai@gmail.com',
                  recipients=[user.email])
    msg.body = f"""To reset your password, visit the following link:
{url_for('users.reset_token', token=token, _external=True)}

If you did not make this request then simply ignore this email and no changes
will be made.
"""
    mail.send(msg)