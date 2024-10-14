from flask import request, jsonify
from workflow_manager.workflow_manager import execute_workflow

def news_controller():
    data = request.get_json()
    query = data.get('query')
    user_email = data.get('email')

    if not query:
        return jsonify({"error": "Query is required."}), 400

    try:
        result = execute_workflow(query, user_email)  # Capture the result or message
        return jsonify({"message": result}), 200  # Return success message
    except Exception as e:
        return jsonify({"error": str(e)}), 500
