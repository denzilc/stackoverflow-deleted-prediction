**Stack Overflow Deleted Question Prediction**

Classification code for the paper **Chaff from the wheat: characterization and modeling of deleted questions on stack overflow** published at *WWW '14 Proceedings of the 23rd international conference on World wide web*. 

Dataset - https://archive.org/details/stackoverflow_2013_05_deleted_posts_stackoverflow

**Sample Output**

```
***** A ****
(235048, 14) (235048, 14)
(235048, 13) (235048, 13)
(470096, 12) (470096,)
f1 58.23 0.12
accuracy 57.19 0.04
roc_auc 59.6 0.09
***** A + B ****
(235048, 20) (235048, 20)
(235048, 19) (235048, 19)
(470096, 18) (470096,)
f1 61.5 0.05
accuracy 59.78 0.11
roc_auc 63.7 0.23
***** A + B + C ****
(235048, 31) (235048, 31)
(235048, 30) (235048, 30)
(470096, 29) (470096,)
f1 64.9 0.09
accuracy 64.65 0.02
roc_auc 70.91 0.03
***** A + B + C + D ****
(235048, 49) (235048, 49)
(235048, 48) (235048, 48)
(470096, 47) (470096,)
f1 65.62 0.12
accuracy 65.33 0.02
```

**Bibtex**
```
@inproceedings{Correa:2014:CWC:2566486.2568036,
 author = {Correa, Denzil and Sureka, Ashish},
 title = {Chaff from the Wheat: Characterization and Modeling of Deleted Questions on Stack Overflow},
 booktitle = {Proceedings of the 23rd International Conference on World Wide Web},
 series = {WWW '14},
 year = {2014},
 isbn = {978-1-4503-2744-2},
 location = {Seoul, Korea},
 pages = {631--642},
 numpages = {12},
 url = {http://doi.acm.org/10.1145/2566486.2568036},
 doi = {10.1145/2566486.2568036},
 acmid = {2568036},
 publisher = {ACM},
 address = {New York, NY, USA},
 keywords = {question quality, question-answering, stack overflow},
} 
```
