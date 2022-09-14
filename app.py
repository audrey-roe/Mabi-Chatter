from django.shortcuts import render
from django.http import HttpResponse
from mabi_main import get_response






def index_get(request):
    if request.method == 'GET':

        return render (request,"base.html")

def predict(request):
    if request.method == 'POST':
        text = request.json("message")

        response = get_response(text)
        message = {"answer":response}
        return render(message)

if __name__ == "__main__":
    app.run(debug=True)
