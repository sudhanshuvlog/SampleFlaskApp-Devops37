from flask import Flask


def create_app():
    app = Flask(__name__)
    print("inside create_app function")
    
    @app.route('/')
    def home():
        print("inside home function")
        return 'Hurray Sudhanshu Updated1233333455555555!'

    @app.route('/test')
    def test():
        return "test 123456789 abcdefg79239279273927393923982938239239"
        
    @app.route('/test2')
    def test1():
        return "test 2"
    @app.route('/test3')
    def test2():
        return "test 1234"

    return app


if __name__ == '__main__':
    app = create_app()
    
    app.run(host='0.0.0.0', port=80, debug=True)