from flask import Flask


def create_app():
    app = Flask(__name__)
    print("inside create_app function")
    
    @app.route('/')
    def home():
        print("inside home function")
        test2()
        return 'Hurray Sudhanshu Updated1233333455555555!'

    @app.route('/test')
    def test():
        return "test 123456789"

if __name__ == '__main__':
    app = create_app()
    
    app.run(host='0.0.0.0', port=80, debug=True)
