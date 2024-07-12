## Flask Application Design for Bernoulli's Theorem

**HTML Files**

- **index.html**: This is the main HTML file that will be rendered when the user visits the application. It will contain the user interface for interacting with the application.
- **results.html**: This HTML file will be responsible for displaying the results of the Bernoulli's theorem calculations.

**Routes**

- **@app.route('/')**: This route maps to the **index.html** file and will be responsible for handling user input and displaying the main interface.
- **@app.route('/calculate', methods=['POST'])**: This route will be triggered when the user submits the form on the **index.html** page. It will perform the Bernoulli's theorem calculations and then redirect the user to the **results.html** page.

**Code Sample**

```python
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
```

**Bootstrap**

For the frontend, Bootstrap can be integrated into the HTML files to enhance the user interface. Bootstrap provides pre-styled components and CSS classes that can be easily incorporated into the HTML code.

For example, in the **index.html** file, Bootstrap classes can be added to style the form and its elements:

```html
<!-- Input field for density -->
<div class="mb-3">
  <label for="density" class="form-label">Density (kg/m³):</label>
  <input type="number" class="form-control" id="density" name="density" required>
</div>

<!-- Input field for velocity -->
<div class="mb-3">
  <label for="velocity" class="form-label">Velocity (m/s):</label>
  <input type="number" class="form-control" id="velocity" name="velocity" required>
</div>

<!-- Button to submit the form -->
<button type="submit" class="btn btn-primary">Calculate</button>
```