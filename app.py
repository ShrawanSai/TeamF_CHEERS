from flask import Flask, render_template, request,send_file
from decimal import Decimal
from incarnation_1.v1_0_4.main import Math
from incarnation_2.v1_0_4 import main
import math

app = Flask(__name__)

def inc1_testcases(sample_radii=[5, 10, 15, 20, 25, 30, 35, 40, 45, 50]):
    alpha = find_alpha()
    tcs_from_inc1 = []
    for radius in sample_radii:
        length = compute_length_inc1(radius, alpha)
        tcs_from_inc1.append(length)
    return tcs_from_inc1

def get_radius(r):
    try:
        r = Decimal(r)
        if r < 0:
            raise ValueError
        return r
    except ValueError:
        return "Invalid Input! radius cannot be less than 0. Please try again"
    except Exception:
        return "Invalid Input! Please enter a correct value (a number)"

def find_alpha():
    # Function to find the value of alpha using Bisection method
    # Returns the value of alpha as a Decimal object

    try:
        # Calling the Bisection method from scratch
        alpha = Math.bisection_solver(0, 10)
        if alpha is None:
            raise ValueError("Alpha cannot be calculated.")
    except Exception as e:
        return e

    return alpha

def compute_length_inc1(radius, alpha):
    # Function to compute the length of the segment X1X2
    # Returns the length as a Decimal object
    length = 2 * radius * (1 - (Math.cos(alpha / 2)))
    return length

@app.route('/download-xml')
def download_xml():
    # Generate the XML file content
    
    # Return the XML file as a download attachment
    return send_file('output.xml', as_attachment=True)

@app.route('/', methods=['GET', 'POST'])
def home():
    if request.method == 'POST':
        option = request.form['option']
        length = request.form['length']
        processed_radius = get_radius(length)
        if not isinstance(processed_radius,Decimal):
            # Return error message and input value to re-populate form
            return render_template('index.html', error=processed_radius, length_input=length)
        length = processed_radius
        
        if option == 'incarnation1':
            alpha = find_alpha()
            length_to_move = compute_length_inc1(length, alpha)
            length_to_move = str(length_to_move)[:12]
            option = "Incarnation 1 results"
        elif option == 'incarnation2':
            alpha = main.find_alpha()
            length_to_move = main.compute_length(float(length), alpha)
            length_to_move = str(length_to_move)[:12]
            main.write_to_xml(alpha, length)
            option = "Incarnation 2 results"
        else:
            alpha = find_alpha()
            alpha2 = main.find_alpha()
            length_to_move_inc1 = compute_length_inc1(length, alpha)
            length_to_move_inc2 = main.compute_length(float(length), alpha2)
            length_to_move_inc2 = str(length_to_move_inc2)[:12]
            length_to_move_inc1 = str(length_to_move_inc1)[:12]
            length_to_move = f'{length_to_move_inc1} units for Incarnation 1 &  \n {length_to_move_inc2} units for Incarnation 2'
            option = "Results from both Incarnation 1 and 2"
        alpha = str(alpha)[:12]
        return render_template('index.html', length_to_move=length_to_move,alpha = alpha,option = option, radius = length )
    else:
        return render_template('index.html')
    
@app.route('/testcase', methods=['POST'])
def test_cases():
    radii = [5, 10, 15, 20, 25, 30, 35, 40, 45, 50]
    tcs_from_inc1 = inc1_testcases()
    tcs_from_inc2 = main.sample_outputs()

    table = []

    for i in range(len(radii)):
        table.append([i+1,radii[i], str(tcs_from_inc1[i])[:12], str(tcs_from_inc2[i])[:12] ])
    return render_template('index.html',table = table)
if __name__ == '__main__':
    app.run(debug=True)
