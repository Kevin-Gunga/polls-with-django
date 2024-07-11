from django.shortcuts import render
from django.http import HttpResponse
from .models import Choice, Question
from django.utils.datastructures import MultiValueDictKeyError

def index(request):
    if request.method == 'POST':
        try:
            question = request.POST['question_text']
            publication = request.POST['pub_date']
            choice = request.POST['choice_text']
            votes = request.POST['votes']

            new_question = Question(question_text=question, pub_date=publication)
            new_question.save()

            new_choice = Choice(choice_text=choice, votes=votes, question=new_question)
            new_choice.save()
            
            return HttpResponse("Question and choice saved successfully.")
        
        except MultiValueDictKeyError as e:
            return HttpResponse(f"Missing field: {str(e)}")
    
    return render(request, 'polls/index.html', {})
