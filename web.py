import flask
import jinja2

mipyt = flask.Blueprint('mipyt', __name__, template_folder='templates')


@mipyt.route('/')
def index():
    flask.current_app.logger.debug('Hlavni stranka se zobrazuje')
    link = flask.url_for('mipyt.hello', name='Marek', count=10)
    return flask.render_template('index.html', greet_link=link)


@mipyt.route('/greet/')
@mipyt.route('/greet/<name>/')
@mipyt.route('/greet/<name>/<int:count>/')
def hello(name=None, count=1):
    flask.current_app.logger.debug(f'Zdravím {name} celkem {count}krát')
    return flask.render_template('hello.html', name=name, count=count)


def create_app(answer=None):
    app = flask.Flask(__name__)
    app.logger.warning('Inicializoval jsem aplikaci')

    app.config['answer'] = answer


    @app.route('/answer/')
    def answer():
        return f'The ultimate answer is: {flask.current_app.config["answer"]}'


    @app.template_filter('fitmail')
    def ctu_email(username):
        return jinja2.Markup('<a href="mailto:')+ username.lower() + jinja2.Markup('@fit.cvut.cz">') + username + jinja2.Markup('</a>')


    app.register_blueprint(mipyt, url_prefix='/mi-pyt')

    return app

