import spacy
import en_core_web_sm
import json
from spacy import displacy
import os

nlp = spacy.load('en')
ner_dict = dict()
doc = nlp(u'The F.B.I. had been under immense political pressure by Mr. Trump to dismiss Mr. Strzok, who was removed last summer from the staff of the special counsel, Robert S. Mueller III. The president has repeatedly denounced Mr. Strzok in posts on Twitter, and on Monday expressed satisfaction that he had been sacked.')
for X in doc.sents:
  for X1 in X.ents:
    if(X1.label_ == 'NORP'):
      ner_dict.update({X1.text:'Nationalaties or religious or political groups'})
    elif(X1.label_ == 'GPE'):
      ner_dict.update({X1.text:'Countries,Cities, States'})
    else:
      ner_dict.update({X1.text:X1.label_})
print(ner_dict)
displacy.render(doc, style='ent', jupyter=True)

jason = json.dumps(ner_dict)
print(jason)

ner_dict1 = dict()
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
  s = unicode(str1,errors='ignore')
  doc1 = nlp(s)
  for X in doc1.sents:
    for X1 in X.ents:
      if(X1.label_ == 'NORP'):
        ner_list1.append(X1.text)
        ner_list2.append('Nationalaties or religious or political groups')
      elif(X1.label_ == 'GPE'):
        ner_list1.append(X1.text)
        ner_list2.append('Countries,Cities, States')
      else:
        ner_list1.append(X1.text)
        ner_list2.append(X1.label_)
  ner_dict1.update({"annotation":{"data_filename": os.path.basename(file.name), "data_type": "text","data_annotation":{"text_ner_classification":{"ner_word":ner_list1,"ner_label":ner_list2}}}})
  for i in range(1,100):
    if(os.path.exists("{}{}{}".format(s2,i,s1))):
      pass
    else:  
      json.dump(ner_dict1 , open("{}{}{}".format(s2,i,s1),"w"))
      break
  print("File created is: "+"{}{}{}".format(s2,i,s1))d
except:
  print("File does not exist")
  