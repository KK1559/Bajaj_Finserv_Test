from flask import Flask, request, jsonify
import re

app = Flask(__name__)

@app.route('/bfhl', methods=['POST'])
def bfhl():
    try:
        data = request.get_json()

        if not data or 'data' not in data or not isinstance(data['data'], list):
            return jsonify({
                "is_success": False,
                "message": "Invalid input format. 'data' array is required."
            }), 400

        input_array = data['data']

        odd_numbers = []
        even_numbers = []
        alphabets = []
        special_characters = []
        numbers_sum = 0
        all_alphabets_for_concat = []

        for item in input_array:
            try:
                num = int(item)
                numbers_sum += num
                if num % 2 == 0:
                    even_numbers.append(str(num))
                else:
                    odd_numbers.append(str(num))
            except ValueError:
                if item.isalpha():
                    alphabets.append(item.upper())
                    for char in item:
                        all_alphabets_for_concat.append(char)
                else:
                    special_characters.append(item)

        temp_concat_string = "".join(all_alphabets_for_concat)
        reversed_concat_string = temp_concat_string[::-1]

        final_concat_string = ""
        for i, char in enumerate(reversed_concat_string):
            if i % 2 == 0:
                final_concat_string += char.upper()
            else:
                final_concat_string += char.lower()

        user_id = "kashish_sharma08102003".lower()
        email = "kashish.sharma@example.com"
        roll_number = "2210991770"

        response_data = {
            "is_success": True,
            "user_id": user_id,
            "email": email,
            "roll_number": roll_number,
            "odd_numbers": odd_numbers,
            "even_numbers": even_numbers,
            "alphabets": alphabets,
            "special_characters": special_characters,
            "sum": str(numbers_sum),
            "concat_string": final_concat_string
        }

        return jsonify(response_data), 200

    except Exception as e:
        print(f"An error occurred: {e}")
        return jsonify({
            "is_success": False,
            "message": "An internal server error occurred."
        }), 500

if __name__ == '__main__':
    app.run(debug=True, port=5000)
