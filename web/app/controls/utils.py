from flask import render_template, current_app, Blueprint
from threading import Thread
from flask_mail import Message, Mail


class Utils():
    def __init__(self):
        self.mail = None
    
    def async_send_mail(self, app, msg):
        self.mail = Mail(app)
        with app.app_context():
            self.mail.send(msg)

    def send_mail(self, app, subject, recipient, template, name, senha):
        msg = Message(subject, sender=current_app.config['MAIL_DEFAULT_SENDER'], recipients=[recipient])
        msg.html = render_template(template, name=name, senha=senha)

        thr = Thread(target=self.async_send_mail, args=[current_app._get_current_object(), msg])
        thr.start()

        return thr

