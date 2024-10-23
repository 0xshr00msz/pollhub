from django.shortcuts import render

from .forms import QuestionForm
from .models import Question

# Create your views here.
def index(request):
    if request.method == "POST":
        form = AnswerForm(request.POST)
        if form.is_valid():
            answer = form.cleaned_data['answer']  # Get the selected answer
            # You can save this answer if needed, or just redirect
            Question.objects.create(answer=answer)
            return redirect('success')  # Redirect to success page after submission
    else:
        form = AnswerForm()

    return render(request, 'ask/index.html', {'form': form})

def success(request):
    return render(request, 'ask/success.html')