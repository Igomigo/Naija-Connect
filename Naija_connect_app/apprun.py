""" This module is the location where the app is run from """

from application import create_app

app = create_app()

if __name__ == "__main__":
    app.run(debug=True)