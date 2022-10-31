from flask import Flask

gus_app = Flask(__name__)

@gus_app.route("/")
def hello():
    return "Hello World!"

# run the app.
if __name__ == "__main__":
    gus_app.run()
