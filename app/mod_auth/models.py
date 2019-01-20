from app import db
from werkzeug import generate_password_hash


class Base(db.Model):
    __abstract__ = True

    id = db.Column(db.Integer, primary_key=True)
    date_created = db.Column(db.DateTime, default=db.func.current_timestamp())
    date_modified = db.Column(
        db.DateTime,
        default=db.func.current_timestamp(),
        onupdate=db.func.current_timestamp())


class User(Base):
    __tablename__ = 'auth_user'

    # User Name
    name = db.Column(db.String(20), nullable=False)

    # Email
    email = db.Column(db.String(128), nullable=False)

    # Password
    password = db.Column(db.String(128), nullable=False)

    def __init__(self, name, email, password):
        self.name = name.lower()
        self.email = email.lower()
        self.password = generate_password_hash(password)

    def __repr__(self):
        return f'[User {self.name}]'

    def remove(self):
        db.session.delete(self)
        db.session.commit()

        return self

    def save(self):
        db.session.add(self)
        db.session.commit()

        return self