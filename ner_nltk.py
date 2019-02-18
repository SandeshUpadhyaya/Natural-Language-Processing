import nltk
from nltk.tokenize import word_tokenize
from nltk.tag import pos_tag
import re
import json
import os

import nltk
nltk.download('punkt')
nltk.download('averaged_perceptron_tagger')
nltk.download('maxent_ne_chunker')
nltk.download('words')

doc = 'The F.B.I. had been under immense political pressure by Mr. Trump to dismiss Mr. Strzok, who was removed last summer from the staff of the special counsel, Robert S. Mueller III. The president has repeatedly denounced Mr. Strzok in posts on Twitter, and on Monday expressed satisfaction that he had been sacked.'

ne_tree = nltk.ne_chunk(pos_tag(word_tokenize(doc)))
print(ne_tree)

named_entities = dict()
ner_list1 = []
ner_list2 = []
str1 = " "
str2 = raw_input("Enter a filename: ")
s2 = 'out'
s1 = '.json'
try:
  file = open(str2,'r')
  for line in file:
    str1 += line
  ne_tree1 = nltk.ne_chunk(pos_tag(word_tokenize(str1)))
  for line in ne_tree1:
    if(hasattr(line,'label')):
      entity_name = ' '.join(c[0] for c in line.leaves()) 
      entity_type = line.label() 
      ner_list1.append(entity_name)
      ner_list2.append(entity_type)
  named_entities.update({"annotation":{"data_filename": os.path.basename(file.name), "data_type": "text","data_annotation":{"text_ner_classification":{"ner_word":ner_list1,"ner_label":ner_list2}}}})
  for i in range(1,100):
    if(os.path.exists("{}{}{}".format(s2,i,s1))):
      pass
    else:  
      json.dump(named_entities , open("{}{}{}".format(s2,i,s1),"w"))
      break
  print("File created is: "+"{}{}{}".format(s2,i,s1))
except:
  print("File does not exist")