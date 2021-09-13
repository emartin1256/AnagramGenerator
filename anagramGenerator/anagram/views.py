from django.shortcuts import render
from django.http import HttpResponseRedirect, HttpResponse
from .models import Anagram
import os.path
import sys
words = open(os.path.dirname(__file__) + "/words.txt").read()
dict = words.split("\n")
# Create your views here.
def main(request):
    return HttpResponse("Hello")

def myView(request):
    all_anagram_items = Anagram.objects.all()
    return render(request, 'anagram.html', {'all_items': all_anagram_items})

# def anagramer(input):
#     input = sorted(input)
#     anagrams = []
#     for i in dict:
#         if input == sorted(i):
#             anagrams.append(i)
#             return(i)

def findAnagram(request):
    # input = request
    # anagrams = []
    # # input.replace(" ", "")
    # input = sorted(input)
    # for i in dict:
    #     if input == sorted(i):
    #         anagrams.append(i)
    # for i in anagrams:
    input = request.POST['content']
    input = sorted(input)
    # anagrams = []
    Anagram.objects.all().delete()
    for i in dict:
        if input == sorted(i):
            # anagrams.append(i)
            new_item = Anagram(content = i)
            new_item.save()
    # new_item = Anagram(content = a.POST['content'])
    # new_item.save()
    print(i)

    return HttpResponseRedirect('/anagram/')
