from rest_framework.test import APIRequestFactory

tester = APIRequestFactory()

def create_request_test():
    request = tester.post('/debit/', {
        "requester": "http://127.0.0.1:8000/users/2/",
        "value": 240,
        "target": "http://127.0.0.1:8000/partners/1/",
        "status": "Analyzing",
        "is_enable": True
    })


def actualize_request_test():
    request = tester.put('/debit/2/', {
        "requester": "http://127.0.0.1:8000/users/2/",
        "value": 123,
        "target": "http://127.0.0.1:8000/partners/1/",
        "status": "Rejected",
        "is_enable": true
    })