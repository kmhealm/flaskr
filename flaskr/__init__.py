from flask import Flask 
import os

def create_app(test_config = None):
    app = Flask(__name__,instance_relative_config=True)
    app.config.from_mapping(
        SECRET_KEY='flaskr',
        DATABASE=os.path.join(app.instance_path,'flaskr.db'))

    @app.route('/hello')
    def hello():
        return 'hello'

    from . import db
    db.init_app(app)

    from . import blog,auth
    app.register_blueprint(blog.bp)
    app.register_blueprint(auth.bp)
    app.add_url_rule('/',endpoint='index')

    return app



