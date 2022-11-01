from flask import Flask
from df import process_data
gus_app = Flask(__name__)

@gus_app.route("/")
def hello():
    df = process_data('foo.csv')
    assert df.columns.to_list() == ['id', 'customer_name', 'total_purchases']
    return "Hello, Gus - tests passed"

# run the app.
if __name__ == "__main__":
    gus_app.run(host="0.0.0.0", port=8050)
