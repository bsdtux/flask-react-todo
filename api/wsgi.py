import os
from api import create_app


environ = os.environ.get('FLASK_ENV') or 'default'
app = create_app(environ=environ)
app.run(debug=app.config.get('DEBUG'))
