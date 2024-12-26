from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/payment_status', methods=['POST'])
def payment_status():
    # Получаем данные из запроса
    data = request.json

    # Проверяем наличие обязательных полей
    required_fields = ["uuid", "order_id", "amount", "payment_amount", "payment_status"]
    if not all(field in data for field in required_fields):
        return jsonify({"error": "Missing required fields"}), 400

    # Извлекаем статус и другие данные
    uuid_value = data.get("uuid")
    order_id = data.get("order_id")
    amount = data.get("amount")
    payment_amount = data.get("payment_amount")
    payment_status = data.get("payment_status")

    # Логируем полученные данные для отладки
    print(f"Received payment status: {payment_status} for order {order_id} (UUID: {uuid_value})")

    # Обрабатываем статус платежа
    if payment_status == "paid":
        # Здесь ты можешь обновить статус заказа в базе данных или выполнить другие действия
        return jsonify({
            "status": "success",
            "message": "Payment received.",
            "details": data,
        }), 200

    elif payment_status == "pending":
        return jsonify({
            "status": "pending",
            "message": "Payment is still pending.",
            "details": data,
        }), 200

    elif payment_status == "failed":
        return jsonify({
            "status": "failure",
            "message": "Payment failed.",
            "details": data,
        }), 200

    else:
        return jsonify({
            "status": "unknown",
            "message": f"Unhandled payment status: {payment_status}",
            "details": data,
        }), 200



if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080, debug=True)
