from flask_api import FlaskAPI

app = FlaskAPI(__name__)


@app.route('/', methods=['GET'])
def example():
    return {'hello': 'world'}


if __name__ == '__main__':
    app.run(debug=True)
