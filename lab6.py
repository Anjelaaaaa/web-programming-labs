from flask import Blueprint, render_template, request, session

lab6 = Blueprint('lab6', __name__)

offices = []
for i in range(1, 11):
    offices.append({"number": f"Офис {i}", "tenant": "", "price": 900 + i % 3 * 50})


@lab6.route('/lab6/')
def lab():
    return render_template('lab6/lab6.html')


@lab6.route('/lab6/json-rpc-api/', methods=['POST'])
def api():
    data = request.json
    id = data['id']
    login = session.get('login')

    if not login:
        if data['method'] == 'info':
            return {
                'jsonrpc': '2.0',
                'result': {
                    'offices': offices,
                    'current_user': None  
                },
                'id': id
            }

        return {
            'jsonrpc': '2.0',
            'error': {
                'code': 1,
                'message': 'Unauthorized'
            },
            'id': id
        }

    if login not in session:
        session[login] = {'total_cost': 0}

    if data['method'] == 'info':
        return {
            'jsonrpc': '2.0',
            'result': {
                'offices': offices,
                'current_user': login  
            },
            'id': id
        }

    if data['method'] == 'booking':
        office_number = data['params']
        for office in offices:
            if office['number'] == office_number:
                if office['tenant'] != '':  
                    return {
                        'jsonrpc': '2.0',
                        'error': {
                            'code': 2,
                            'message': 'Already booked'
                        },
                        'id': id
                    }

                office['tenant'] = login
                session[login]['total_cost'] += office['price']  
                return {
                    'jsonrpc': '2.0',
                    'result': 'success',
                    'id': id
                }

    if data['method'] == 'cancellation':
        office_number = data['params']
        for office in offices:
            if office['number'] == office_number:
                if office['tenant'] == '':  
                    return {
                        'jsonrpc': '2.0',
                        'error': {
                            'code': 3,
                            'message': 'Not booked'
                        },
                        'id': id
                    }

                if office['tenant'] != login:  
                    return {
                        'jsonrpc': '2.0',
                        'error': {
                            'code': 4,
                            'message': 'Someone already booking'
                        },
                        'id': id
                    }

                office['tenant'] = ''  
                session[login]['total_cost'] -= office['price']  
                return {
                    'jsonrpc': '2.0',
                    'result': 'success',
                    'id': id
                }

    return {
        'jsonrpc': '2.0',
        'error': {
            'code': -32601,
            'message': 'Method not found'
        },
        'id': id
    }

