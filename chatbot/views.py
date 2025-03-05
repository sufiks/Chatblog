from django.shortcuts import render
from openai import api_key
from .forms import MessageForm
from langchain.llms import OpenAI

llm = OpenAI(api_key='OpenAi_API_KEY')

def chatbot_view(request):
    response = ""
    if request.method == "POST":
        form = MessageForm(request.POST)
        if form.is_valid():
            user_message = form.cleaned_data['message']
            response = llm(user_message)
    else:
        form = MessageForm()

    return render(request, 'chatbot/chatbot.html',{'form': form, 'response': response})
