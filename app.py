from flask import Flask


def create_app():
    app = Flask(__name__)
    # x = 10
    # y = x-10
    print("inside create_app function")

    @app.route('/')
    def home():
        print("inside home function")
        return 'Hurray Sudhanshu Updated!'

    @app.route('/test')
    def test():
        return " 123"

    return app


if __name__ == '__main__':
    app = create_app()
    app.run(host='0.0.0.0', port=80, debug=True)
