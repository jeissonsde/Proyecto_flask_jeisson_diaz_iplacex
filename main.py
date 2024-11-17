
from flask import Flask, render_template, request

app = Flask(__name__)

#@app.route('/') este bloque fue realizado para probar el apuntador
#def home():
#    return "¡Bienvenido a mi proyecto Flask! Jeisson Diaz Noviembre de 2024"

@app.route('/')
def home():
    return render_template('menu.html')


@app.route('/ejercicio1', methods=['GET', 'POST'])
def ejercicio1():
    if request.method == 'POST':
        nota1 = float(request.form['nota1'])
        nota2 = float(request.form['nota2'])
        nota3 = float(request.form['nota3'])
        asistencia = float(request.form['asistencia'])

        promedio = (nota1 + nota2 + nota3) / 3
        estado = 'Aprobado' if promedio >= 40 and asistencia >= 75 else 'Reprobado'

        return render_template('resultado1.html', promedio=promedio, estado=estado)
    return render_template('ejercicio1.html')


@app.route('/ejercicio2', methods=['GET', 'POST'])
def ejercicio2():
    if request.method == 'POST':
        nombre1 = request.form['nombre1']
        nombre2 = request.form['nombre2']
        nombre3 = request.form['nombre3']

        nombres = [nombre1, nombre2, nombre3]
        nombre_mas_largo = max(nombres, key=len)
        largo = len(nombre_mas_largo)

        return render_template('resultado2.html', nombre=nombre_mas_largo, largo=largo)
    return render_template('ejercicio2.html')



if __name__ == '__main__':
    app.run(debug=True) # con debug = true me permite identificar errores y trabajar mas rapido

