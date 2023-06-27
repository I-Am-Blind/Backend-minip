import bardapi

def bard(input):
 token = 'XQitoCQDhixAQDJR3Rbm0kpVu5XGEvOjXBE0LoY4i77br6lbJ8ogGvZSiQCWxgy7xMGuug.'
 try:
    response = bardapi.core.Bard(token).get_answer(input)
    return response
 except Exception as e:
    print("An error occurred:", str(e))

