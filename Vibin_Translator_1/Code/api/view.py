from flask import request, Blueprint, jsonify
from translate import Translator

users = Blueprint("api", __name__, url_prefix="/user")


@users.route("/translate", methods=["POST"])
def translate():
    try:
        # Get Tamil text from the JSON body
        data = request.get_json()
        tamil_text = data.get("TamilText")

        # Check if TamilText was provided
        if not tamil_text:
            return jsonify({
                "Tamil Text": "",
                "English Text": "No Tamil text provided"
            }), 400

        # Translate the Tamil text to English
        translator = Translator(from_lang="ta", to_lang="en")
        english_translation = translator.translate(tamil_text)
        print(english_translation)
        # Return the translation as JSON response
        return jsonify({
            "Tamil Text": tamil_text,
            "English Text": english_translation
        }), 200
    except Exception as e:
        return jsonify({
            "Tamil Text": tamil_text if 'tamil_text' in locals() else "",
            "English Text": "Error in translation"
        }), 400
