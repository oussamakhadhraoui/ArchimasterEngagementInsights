from flask import Blueprint, render_template, request, redirect, current_app
import requests

role_view_bp = Blueprint('role_view', __name__, url_prefix='/roles')

@role_view_bp.route('/new', methods=['GET'])
def new():
    return render_template('rolesList.html')

@role_view_bp.route('/', methods=['POST'])
def create():
    data = request.form.to_dict()
    api_url = f'{current_app.config["API_BASE_URL"]}/roles'
    response = requests.post(api_url, json=data)
    return redirect('/roles')

@role_view_bp.route('/', methods=['GET'])
def index():
    page = request.args.get('page', 1, type=int)
    per_page = 5
    api_url = f'{current_app.config["API_BASE_URL"]}/roles'
    response = requests.get(api_url)
    roles_data = response.json()

    total_items = len(roles_data['items'])
    total_pages = (total_items + per_page - 1) // per_page
    start_index = (page - 1) * per_page
    end_index = min(start_index + per_page, total_items)
    roles = roles_data['items'][start_index:end_index]

    return render_template('rolesList.html', roles=roles, pagination={
        'has_prev': page > 1,
        'has_next': page < total_pages,
        'prev_num': page - 1,
        'next_num': page + 1,
        'current_page': page,
        'total_pages': total_pages,
    })

@role_view_bp.route('/<int:id>', methods=['GET'])
def show(id):
    api_url = f'{current_app.config["API_BASE_URL"]}/roles/{id}'
    role = requests.get(api_url).json()

@role_view_bp.route('/<int:id>/edit', methods=['GET'])
def edit(id):
    api_url = f'{current_app.config["API_BASE_URL"]}/roles/{id}'
    role = requests.get(api_url).json()
    return render_template('rolesList.html', role=role)

@role_view_bp.route('/<int:id>', methods=['POST'])
def update(id):
    data = request.form.to_dict()
    api_url = f'{current_app.config["API_BASE_URL"]}/roles/{id}'
    response = requests.put(api_url, json=data)
    return redirect('/roles')

@role_view_bp.route('/<int:id>', methods=['POST'])
def delete(id):
    api_url = f'{current_app.config["API_BASE_URL"]}/roles/{id}'
    response = requests.delete(api_url)
    return redirect('/roles')