import multiprocessing
import gunicorn.app.base
from __init__ import app as handler_app

def number_of_workers():
    _ = multiprocessing.cpu_count()
    return (4 if _ > 4 else _) * 2 + 1

class StandaloneApplication(gunicorn.app.base.BaseApplication):

    def __init__(self, app, options=None):
        self.options = options or {}
        self.application = app
        super().__init__()

    def load_config(self):
        config = {key: value for key, value in self.options.items()
                  if key in self.cfg.settings and value is not None}
        for key, value in config.items():
            self.cfg.set(key.lower(), value)

    def load(self):
        return self.application


if __name__ == '__main__':
    options = {
        'bind': '%s:%s' % ('0.0.0.0', '8080'),
        'workers': number_of_workers(),
    }
    StandaloneApplication(handler_app, options).run()