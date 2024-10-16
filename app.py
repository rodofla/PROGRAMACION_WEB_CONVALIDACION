from flask import Flask, jsonify, render_template, request

app = Flask(__name__)

users = {
    "juan": {"password": "admin", "role": "Administrador"},
    "pepe": {"password": "user", "role": "Usuario"}
}

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/ejercicio1', methods=['GET', 'POST'])
def ejercicio1():
    if request.method == 'POST':
        nombre = request.form['nombre']
        edad = int(request.form['edad'])
        cantidad = int(request.form['cantidad'])

        precio_por_tarro = 9000
        total_sin_descuento = cantidad * precio_por_tarro

        if 18 <= edad <= 30:
            descuento = 0.15
        elif edad > 30:
            descuento = 0.25
        else:
            descuento = 0

        total_con_descuento = total_sin_descuento * (1 - descuento)
        descuento_aplicado = total_sin_descuento * descuento


        return render_template('ejercicio1.html',
                               nombre=nombre,
                               total_sin_descuento=total_sin_descuento,
                               descuento_aplicado=descuento_aplicado,
                               total_con_descuento=total_con_descuento),
    return render_template('ejercicio1.html')

@app.route('/ejercicio2', methods=['GET', 'POST'])
def ejercicio2():
    if request.method == 'POST':
        username = request.form['nombre']
        password = request.form['password']

        if username in users and users[username]['password'] == password:
            role = users[username]['role']
            message = f"Bienvenido {role.lower()} {username}"
        else:
            message = "Nombre o contraseña incorrectos"

        return render_template('ejercicio2.html', message=message)

    return render_template('ejercicio2.html')


if __name__ == "__main__":
    app.run(debug=True)
