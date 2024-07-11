from flask import Flask, render_template, send_file
import os

app = Flask(__name__)
app.config['SCRIPTS_DIR'] = os.path.join(os.path.dirname(__file__), 'scripts')
app.config['PLOT_IMAGES_DIR'] = os.path.join(os.path.dirname(__file__), 'static', 'plot_images')


@app.route('/')
def index():
    try:
        return render_template('index.html')
    except Exception as e:
        return f"Error loading index.html: {str(e)}"


@app.route('/visualization/<script_name>')
def show_visualization(script_name):
    try:
        script_path = os.path.join(app.config['SCRIPTS_DIR'], script_name)
        if not os.path.exists(script_path):
            return f"Error: Visualization script '{script_name}' not found."

        # Execute the script (adjust as necessary)
        os.system(f'python {script_path}')

        # Find the generated plot image
        plot_filename = os.path.join(app.config['PLOT_IMAGES_DIR'], os.path.splitext(script_name)[0] + '.png')
        if os.path.exists(plot_filename):
            return send_file(plot_filename, mimetype='image/png')
        else:
            return f"Error: Plot image not found for '{script_name}'."
    except Exception as e:
        return f"Error displaying visualization: {str(e)}"


if __name__ == '__main__':
    app.run(debug=True)
