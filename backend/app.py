from flask import Flask, jsonify

app = Flask(__name__)

products = [
    {"id": 1, "name": "Laptop", "price": 899},
    {"id": 2, "name": "Phone", "price": 599},
    {"id": 3, "name": "Headphones", "price": 99}
]

@app.route("/")
def home():
    return jsonify({
        "message": "E-Commerce API running successfully"
    })

@app.route("/products")
def get_products():
    return jsonify(products)

@app.route("/health")
def health():
    return jsonify({"status": "healthy"})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)