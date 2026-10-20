from flask import Blueprint, jsonify, request
from app.math_utils import kurang, tambah

main = Blueprint('main', __name__)


@main.route('/')
def home():
  return jsonify({'message': 'Aplikasi DevSecOps Python Aktif'})


@main.route('/hitung')
def hitung():
  a = int(request.args.get('a', 0))
  b = int(request.args.get('b', 0))
  return jsonify({'hasil_tambah': tambah(a, b), 'hasil_kurang': kurang(a, b)})
