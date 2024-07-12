
# Import necessary libraries
from flask import Flask, render_template, request, redirect, url_for

# Create a Flask application instance
app = Flask(__name__)

# Route for the main page
@app.route('/')
def index():
    """Renders the index page."""
    return render_template('index.html')

# Route for calculating and displaying results
@app.route('/calculate', methods=['POST'])
def calculate():
    """Performs Bernoulli's theorem calculations and displays results."""

    # Extract data from the request
    density = float(request.form.get('density'))
    velocity = float(request.form.get('velocity'))
    height = float(request.form.get('height'))

    # Perform Bernoulli's theorem calculations
    pressure = 0.5 * density * velocity**2
    potential_energy = density * 9.81 * height

    # Render the results page
    return render_template('results.html', pressure=pressure, potential_energy=potential_energy)


# Run the application
if __name__ == '__main__':
    app.run(debug=True)
