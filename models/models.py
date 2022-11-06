from app import db
from sqlalchemy.orm import validates


class Plant(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(255), nullable=False)
    location = db.Column(db.String(255), nullable=False)
    employee = db.relationship("Employee", back_populates="plant")


class Employee(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(255), nullable=False)
    last_name = db.Column(db.String(255), nullable=False)
    email = db.Column(db.String(255), unique=True)
    plant_id = db.Column(db.Integer, db.ForeignKey("plant.id"), nullable=False)
    plant = db.relationship("Plant", back_populates="employee")


class User(db.Model):
    __tablename__ = "users"
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(255), nullable=False, unique=True)
    password = db.Column(db.String(255), nullable=False)
    email = db.Column(db.String(255), nullable=False, unique=True)
    first_name = db.Column(db.String(255), nullable=False)
    last_name = db.Column(db.String(255), nullable=False)

    @validates("first_name")
    def validate_first_name(self, key, first_name):
        if first_name == "":
            raise ValueError("You need add first_name")
        return first_name

    @validates("last_name")
    def validate_last_name(self, key, last_name):
        if last_name == "":
            raise ValueError("You need add last_name")
        return last_name

    @validates(username)
    def validate_username(self, key, username):
        if username == "":
            raise ValueError("You need add last_name")
        elif User.username == username:
            raise ValueError("This username is taken please select another")
        return username

    @validates("email")
    def validate_email(self, key, email):
        if email == "":
            raise ValueError("You need add email")
        elif "@" not in email:
            raise ValueError("Email need has '@' ")
        return email

    @validates(password)
    def validate_password(self, key, password):
        pass
        return password

