from flask import Flask, render_template, request, jsonify
from functools import lru_cache
import time

app = Flask(__name__)

# Sample data - kept server-side only
# PROTECTED_DATA = {
#     "apple": {"type": "fruit", "color": "red", "price": 1.20},
#     "apricot": {"type": "fruit", "color": "orange", "price": 1.50},
#     "banana": {"type": "fruit", "color": "yellow", "price": 0.50},
#     "blueberry": {"type": "fruit", "color": "blue", "price": 3.20},
#     "carrot": {"type": "vegetable", "color": "orange", "price": 0.80},
#     "cucumber": {"type": "vegetable", "color": "green", "price": 1.20},
#     "broccoli": {"type": "vegetable", "color": "green", "price": 1.50},
#     "milk": {"type": "dairy", "color": "white", "price": 2.30},
#     "mozzarella": {"type": "dairy", "color": "white", "price": 3.50},
# }

@app.route('/')
def index():
    return render_template('live_search.html')

@app.route('/search', methods=['POST'])
def search():
    # search_term = request.form.get('search_term', '').lower().strip()
    
    # # Find partial matches
    # results = {}
    # for key, value in PROTECTED_DATA.items():
    #     if search_term in key:
    #         results[key] = value


    PROTECTED_DATA = {
    "apple": {"type": "fruit", "color": "red", "price": 1.20},
    "apricot": {"type": "fruit", "color": "orange", "price": 1.50},
    "banana": {"type": "fruit", "color": "yellow", "price": 0.50},
    "blueberry": {"type": "fruit", "color": "blue", "price": 3.20},
    "carrot": {"type": "vegetable", "color": "orange", "price": 0.80},
    "cucumber": {"type": "vegetable", "color": "green", "price": 1.20},
    "broccoli": {"type": "vegetable", "color": "green", "price": 1.50},
    "milk": {"type": "dairy", "color": "white", "price": 2.30},
    "mozzarella": {"type": "dairy", "color": "white", "price": 3.50},
    }
    
    search_term = request.form.get('search_term', '').lower().strip()
    results = {}
    for key, value in PROTECTED_DATA.items():
        if search_term in key:
            results[key] = value    
    
    return jsonify({"results": results})
    

if __name__ == '__main__':
    app.run(debug=True, port=5000)