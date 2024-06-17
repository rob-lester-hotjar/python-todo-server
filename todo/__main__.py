from flask import Flask

from .app import create_app


def run():
    app = create_app()

    app.run(host='0.0.0.0', port=5555, debug=True)


if __name__ == '__main__':
    run()
