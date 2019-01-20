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
    __tablename__ = 'blog_article'

    # User Name
    title = db.Column(db.String(50), nullable=False)

    # Email
    body = db.Column(db.String(), nullable=False)

    def __init__(self, title, body):
        self.title = title
        self.body = body

    def __repr__(self):
        return f'[Blog {self.title}]'

    def remove(self):
        """
        Remove this model from the db
        params:
            self
        returns:
            the removed article
        """

        this = self
        db.session.delete(this)
        db.session.commit()

        return self

    def save(self):
        """
        Save that model into the db
        params:
            self
        returns:
            The created article
        """

        db.session.add(self)
        db.session.commit()

        return self
