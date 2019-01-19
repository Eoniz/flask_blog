from app import db


class Base(db.Model):
    __abstract__ = True

    id = db.Column(db.Integer, primary_key=True)
    date_created = db.Column(db.DateTime, default=db.func.current_timestamp())
    date_modified = db.Column(
        db.DateTime,
        default=db.func.current_timestamp(),
        onupdate=db.func.current_timestamp())


class Blog(Base):
    __tablename__ = 'blog'

    # User Name
    title = db.Column(db.String(50), nullable=False)

    # Email
    body = db.Column(db.String(), nullable=False)

    def __init__(self, title, body):
        self.title = title
        self.body = body

    def __repr__(self):
        return f'[Blog {self.title}]'