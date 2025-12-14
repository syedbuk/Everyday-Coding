from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import  DeclarativeBase, Mapped, mapped_column




class Base(DeclarativeBase):
    pass




db= SQLAlchemy(model_class=Base)

app=Flask(__name__)


app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///new-books-collection.db"

db.init_app(app)


class Books(db.Model):
    id: Mapped[int] = mapped_column(primary_key=True)
    title: Mapped[str] = mapped_column(unique=True)
    author: Mapped[str] = mapped_column(nullable=False)
    rating: Mapped[float] = mapped_column(nullable=False)


with app.app_context():
    db.create_all()


with app.app_context():
    # book=Books( id=1, title="Harry Potter",author="J.K. Rowling",rating=9.3)
    # db.session.add(book)
    # db.session.commit()

    result = db.session.execute(db.select(Books).order_by(Books.title))
    all_books = result.scalar()
    print(all_books.title)


