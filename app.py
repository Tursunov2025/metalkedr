from flask import Flask, request
from flask_cors import CORS
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

CORS(app)

app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:01020512@localhost/metalkedir'

db = SQLAlchemy(app)

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    ism = db.Column(db.String(100))
    telefon = db.Column(db.String(20))
    parol = db.Column(db.String(200))
    role = db.Column(db.String(50))
# ORDERS TABLE
class Order(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    mijoz = db.Column(db.String(100))
    mahsulot = db.Column(db.String(100))
    soni = db.Column(db.Integer)
    status = db.Column(db.String(50))
@app.route("/")
def home():
    return {
        "message": "MetalKedir API ishlayapti"
    }

@app.route("/register", methods=["POST"])
def register():

    data = request.get_json()

    new_user = User(
        ism=data["ism"],
        telefon=data["telefon"],
        parol=data["parol"],
        role=data["role"]
    )

    db.session.add(new_user)
    db.session.commit()

    return {
        "message": "Foydalanuvchi qo‘shildi"
    }

@app.route("/login", methods=["POST"])
def login():

    data = request.json

    telefon = request.json["telefon"]
    parol = request.json["parol"]

    user = User.query.filter_by(
        telefon=telefon,
        parol=parol
    ).first()

    if user:
        return {
            "message": "Login muvaffaqiyatli",
            "user": {
                "id": user.id,
                "ism": user.ism,
                "role": user.role
            }
        }

    return {
        "message": "Telefon yoki parol noto‘g‘ri"
    }, 401

    data = request.get_json()

    telefon = data["telefon"]
    parol = data["parol"]

    user = User.query.filter_by(
        telefon=telefon,
        parol=parol
    ).first()

    if user:
        return {
            "message": "Login muvaffaqiyatli",
            "user": {
                "id": user.id,
                "ism": user.ism,
                "role": user.role
            }
        }

    return {
        "message": "Telefon yoki parol noto‘g‘ri"
    }, 401
# CREATE ORDER API
@app.route("/create-order", methods=["POST"])
def create_order():

    data = request.json

    new_order = Order(
        mijoz=data["mijoz"],
        mahsulot=data["mahsulot"],
        soni=data["soni"],
        status="Kesish"
    )

    db.session.add(new_order)
    db.session.commit()

    return {
        "message": "Buyurtma qo‘shildi"
    }# GET ORDERS API
@app.route("/orders", methods=["GET"])
def get_orders():

    orders = Order.query.all()

    result = []

    for order in orders:
        result.append({
            "id": order.id,
            "mijoz": order.mijoz,
            "mahsulot": order.mahsulot,
            "soni": order.soni,
            "status": order.status
        })

    return result
# UPDATE STATUS API
@app.route("/update-status/<int:id>", methods=["PUT"])
def update_status(id):

    data = request.json

    order = Order.query.get(id)

    if not order:
        return {
            "message": "Buyurtma topilmadi"
        }, 404

    order.status = data["status"]

    db.session.commit()

    return {
        "message": "Status yangilandi"
    }    
with app.app_context():
    db.create_all()

if __name__ == "__main__":
    app.run(debug=True)