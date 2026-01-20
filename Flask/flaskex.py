from flask import Flask, jsonify

# Define the Food class
class Food:
    def __init__(self, id, food_name):
        self.id = id
        self.food_name = food_name

    def to_dict(self):
        """Convert Food object to dictionary for JSON response"""
        return {"id": self.id, "food_name": self.food_name}


# Create Flask app
app = Flask(__name__)

# Sample food items
food_items = [
    Food(1, "Pizza"),
    Food(2, "Burger"),
    Food(3, "Pasta"),
    Food(4, "Salad")
]

@app.route("/")
def home():
    return "Hello Flask!"

@app.route("/test")
def test():
    return "Test Method!"

@app.route("/nums")
def nums():
    nums = [10, 20, 30]
    return jsonify(nums)   # jsonify makes it a proper JSON response

@app.route("/foods")
def display_food_items():
    """Return all food items as JSON"""
    return jsonify([food.to_dict() for food in food_items])


if __name__ == "__main__":
    app.run(debug=True)
