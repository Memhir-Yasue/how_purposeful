from textblob import TextBlob
from flask import Flask, request, render_template, session
import nltk
# nltk.download()


def input(text):
	occurance = 0
	# text = " Hi. Python is not a good langauge why. Why  "
	blob = TextBlob(text)
	words = blob.words
	print(blob.words)
	occurance = words.count('why')
	print("The word occures",occurance,"times")
	return occurance
# input()