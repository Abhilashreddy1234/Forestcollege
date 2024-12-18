from django.shortcuts import render
# Render the chatbot HTML template

def vision(request):
    return render(request, 'vision.html')
def Governing_Board(request):
    return render(request,'Governing_Board.html')
def Dean(request):
    return render(request,'Dean.html')
def Joint_Director(request):
    return render(request,'Joint-Director.html')
def Deputy_Director(request):
    return render(request,'Deputy-Director.html')
def Organogram(request):
    return render(request,'Organogram.html')