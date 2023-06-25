import bardapi
def bard(input):
 token = 'XAjwAcmw3uAlxmdvTdT3HCPDSq8KyVuZD-jwGO6S15PAFKX3Dm7Ah9sC2g-6inJOLIYijQ.'
 try:
    response = bardapi.core.Bard(token).get_answer(input)
    return response
 except Exception as e:
    print("An error occurred:", str(e))

