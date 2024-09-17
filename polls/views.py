from django.shortcuts import render
from django.http import HttpResponse
from .models import Question, Choice, Blog
from django.shortcuts import redirect,get_object_or_404

# Create your views here.

def index(request):
    blog = Blog.objects.all()
    data = {
        'blogs': blog
    }
    return render(request, "index.html", data)


def rooms(request):
    questions = Question.objects.all()
    current_question_index = request.session.get('current_question_index', 0)
    total_questions = questions.count()
    
    if current_question_index < total_questions:
        current_question = questions[current_question_index]
    else:
        current_question = None  # Handle the case when all questions are done
    
    data = {
        'question': current_question,
        'choices': current_question.choice_set.all() if current_question else [],
        'current_question_index': current_question_index + 1,  # Display 1-based index
        'total_questions': total_questions,
    }
    
    return render(request, "rooms.html", data)

def submit_answer(request):
    if request.method == 'POST':
        current_question_index = request.session.get('current_question_index', 0)
        total_questions = Question.objects.count()
        
        # Retrieve the selected choice from the POST data
        selected_choice_id = request.POST.get('choice')
        if selected_choice_id:
            selected_choice = get_object_or_404(Choice, pk=selected_choice_id)
            selected_choice.votes += 1
            selected_choice.save()
        
        # Update the current question index
        if current_question_index < total_questions - 1:
            request.session['current_question_index'] = current_question_index + 1
        else:
            request.session['current_question_index'] = total_questions  # Set to total_questions to indicate completion
        
        return redirect('rooms')
    
def restart_poll(request):
    request.session['current_question_index'] = 0
    return redirect('rooms')


    
def blogs(request):
    
    blogs = Blog.objects.all()
    data = {
        'blogs': blogs
    }
    
    
    return render(request, "blogs.html" , data)

def blog_detail(request, id):
    blog = get_object_or_404(Blog, pk=id)
    related_blogs = Blog.objects.exclude(pk=id)

    
    data = {
        'blog': blog,
        'related_blogs': related_blogs
    }
    
    return render(request, "blog_detail.html", data)