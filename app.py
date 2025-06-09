from flask import Flask, render_template, request, jsonify
import functools

app = Flask(__name__)

def factorial(n):
    return 1 if n == 0 else functools.reduce(lambda x, y: x * y, range(1, n + 1))

def calculate_permutations(n_items, chosen_items):
    """P(n,r) = n!/(n-r)!"""
    factorial_n = factorial(n_items)
    factorial_n_r = factorial(n_items - chosen_items)
    permutations_result = factorial_n / factorial_n_r
    return int(permutations_result)

def calculate_combinations(n_items, chosen_items):
    """C(n,r) = n!/(r!(n-r)!)"""
    divisor = factorial(chosen_items) * factorial(n_items - chosen_items)
    factorial_n = factorial(n_items)
    combinations_result = factorial_n / divisor
    return int(combinations_result)


def count_inversions(permutation):
    """Cuenta las inversiones en una permutación"""
    inversions = 0
    n = len(permutation)
    for i in range(n):
        for j in range(i + 1, n):
            if permutation[i] > permutation[j]:
                inversions += 1
    return inversions

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/calculate', methods=['POST'])
def calculate():
    try:
        data = request.json
        operation = data.get('operation')
        
        if operation in ['permutations', 'combinations']:
            n_items = int(data.get('n_items'))
            chosen_items = int(data.get('chosen_items'))
            
            # Validaciones
            if n_items < 0 or chosen_items < 0:
                return jsonify({'error': 'Los números deben ser positivos'}), 400
            
            if chosen_items > n_items:
                return jsonify({'error': 'El número de elementos a elegir no puede ser mayor al total'}), 400
            
            if operation == 'permutations':
                result = calculate_permutations(n_items, chosen_items)
                formula = f"P({n_items},{chosen_items}) = {n_items}!/({n_items}-{chosen_items})!"
            elif operation == 'combinations':
                result = calculate_combinations(n_items, chosen_items)
                formula = f"C({n_items},{chosen_items}) = {n_items}!/({chosen_items}!×({n_items}-{chosen_items})!)"
            
            return jsonify({
                'result': result,
                'formula': formula,
                'operation': operation.capitalize()
            })
        
        elif operation == 'inversions':
            permutation_str = data.get('permutation')
            try:
                permutation = list(map(int, permutation_str.split()))
                result = count_inversions(permutation)
                return jsonify({
                    'result': result,
                    'permutation': permutation,
                    'operation': 'Inversiones'
                })
            except ValueError:
                return jsonify({'error': 'Formato de permutación inválido. Use números separados por espacios'}), 400
        
        else:
            return jsonify({'error': 'Operación no válida'}), 400
            
    except Exception as e:
        return jsonify({'error': str(e)}), 500

# API endpoints adicionales
@app.route('/api/permutations/<int:n>/<int:r>')
def api_permutations(n, r):
    try:
        result = calculate_permutations(n, r)
        return jsonify({'result': result, 'formula': f'P({n},{r})'})
    except Exception as e:
        return jsonify({'error': str(e)}), 400

@app.route('/api/combinations/<int:n>/<int:r>')
def api_combinations(n, r):
    try:
        result = calculate_combinations(n, r)
        return jsonify({'result': result, 'formula': f'C({n},{r})'})
    except Exception as e:
        return jsonify({'error': str(e)}), 400

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)