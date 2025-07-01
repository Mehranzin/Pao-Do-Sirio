import os
from flask import Flask, request, jsonify, render_template, redirect, url_for
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

database_url = os.environ.get('DATABASE_URL')
if not database_url:
    raise RuntimeError("DATABASE_URL não está definida")

if database_url.startswith('postgres://'):
    database_url = database_url.replace('postgres://', 'postgresql://', 1)

app.config['SQLALCHEMY_DATABASE_URI'] = database_url
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

class Pedido(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(120))
    pacotes = db.Column(db.String(50))
    tamanho = db.Column(db.String(20))
    valor = db.Column(db.String(20))
    vencimento = db.Column(db.String(20))
    status = db.Column(db.String(50))

with app.app_context():
    db.create_all()

@app.route('/')
def index():
    status = request.args.get('status', 'Pendentes')
    pedidos = Pedido.query.filter_by(status=status).all()
    return render_template('index.html', pedidos=pedidos, status=status)

@app.route('/add', methods=['POST'])
def add_pedido():
    data = request.form
    pedido = Pedido(
        nome=data['nome'],
        pacotes=data['pacotes'],
        tamanho=data['tamanho'],
        valor=data['valor'],
        vencimento=data['vencimento'],
        status=data['status']
    )
    db.session.add(pedido)
    db.session.commit()
    return redirect(url_for('index'))

@app.route('/feito/<int:pedido_id>')
def marcar_feito(pedido_id):
    pedido = Pedido.query.get(pedido_id)
    if pedido:
        pedido.status = 'Já Feitos'
        db.session.commit()
    return redirect(url_for('index', status=request.args.get('status', 'Pendentes')))

@app.route('/delete/<int:pedido_id>')
def apagar_pedido(pedido_id):
    pedido = Pedido.query.get(pedido_id)
    if pedido:
        db.session.delete(pedido)
        db.session.commit()
    return redirect(url_for('index', status=request.args.get('status', 'Pendentes')))
