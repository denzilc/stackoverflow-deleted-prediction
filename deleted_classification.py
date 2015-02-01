from sklearn import cross_validation
from sklearn.ensemble import AdaBoostClassifier
from sklearn.metrics import confusion_matrix
from sklearn.metrics import classification_report
from sklearn.metrics import f1_score
from sklearn.metrics import precision_recall_curve
from sklearn.metrics import auc
from sklearn.cross_validation import cross_val_score


import numpy as np


feature_names = ['age_of_account','prev_ques_pos','prev_ques_neg','prev_ques_zero',
                'prev_ans_pos','prev_ans_neg','prev_ans_zero','num_prev_ques','num_prev_ans','badge_score',
                'ques_by_aoc','ans_by_aoc','avg_ans_count','avg_view_count','avg_comment_count','avg_fav_score',
                'avg_ques_score','avg_acc_ans','num_url','tag_score','code_snippet_len','ppron','pronoun','space','relativ',
                'incl','cogmech','social','i','funct','conj','prep','num_body_chars','num_alpha_chars','num_upper_case_chars',
                'num_lower_case_chars','num_digit_chars','num_whitespace_chars','num_spl_chars','num_punct_marks',
                'num_body_words','num_short_words','num_uniq_words','avg_word_body_len','num_title_chars','num_title_words',
                'avg_title_word_len']



def clf_a():
  csv_deleted_fname = open('featset_deleted.csv', 'r')
  deleted_dataset = np.genfromtxt(csv_deleted_fname, skip_header=1, delimiter=",", usecols=(0,1,2,3,4,5,6,7,8,9,10,11,12,48))
  csv_deleted_fname.close()

  csv_featset_normal = open('featset_normal.csv', 'r')
  normal_dataset = np.genfromtxt(csv_featset_normal, skip_header=1, delimiter=",", usecols=(0,1,2,3,4,5,6,7,8,9,10,11,12,48))
  csv_featset_normal.close()

  print deleted_dataset.shape, normal_dataset.shape

  data_0 = normal_dataset[:, 1:]
  data_1 = deleted_dataset[:, 1:]

  # #np.random.shuffle(normal_dataset)
  # #np.random.shuffle(deleted_dataset)
  print data_0.shape, data_1.shape

  clf_dataset = np.vstack((data_0, data_1))
  X = clf_dataset[:, :-1]
  y = clf_dataset[:, -1]

  print X.shape, y.shape

  model = AdaBoostClassifier(n_estimators=300)
  accuracies = list()
  f1_scores = list()
  aucs = list()
      
  scoring_funcs = ['f1', 'accuracy', 'roc_auc']

  for scoring_func in scoring_funcs:
    print scoring_func,
    scores = cross_val_score(model, X, y, cv=10, scoring=scoring_func)
    print np.around(100*np.mean(scores), 2), np.around(100*np.var(scores), 2)



def clf_ab():

  csv_deleted_fname = open('featset_deleted.csv', 'r')
  deleted_dataset = np.genfromtxt(csv_deleted_fname, skip_header=1, delimiter=",", usecols=(0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,48))
  csv_deleted_fname.close()

  csv_featset_normal = open('featset_normal.csv', 'r')
  normal_dataset = np.genfromtxt(csv_featset_normal, skip_header=1, delimiter=",", usecols=(0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,48))
  csv_featset_normal.close()

  print deleted_dataset.shape, normal_dataset.shape

  data_0 = normal_dataset[:, 1:]
  data_1 = deleted_dataset[:, 1:]


  # #np.random.shuffle(normal_dataset)
  # #np.random.shuffle(deleted_dataset)
  print data_0.shape, data_1.shape

  clf_dataset = np.vstack((data_0, data_1))
  X = clf_dataset[:, :-1]
  y = clf_dataset[:, -1]

  print X.shape, y.shape

  model = AdaBoostClassifier(n_estimators=300)
  accuracies = list()
  f1_scores = list()
  aucs = list()
      
  scoring_funcs = ['f1', 'accuracy', 'roc_auc']

  for scoring_func in scoring_funcs:
    print scoring_func,
    scores = cross_val_score(model, X, y, cv=10, scoring=scoring_func)
    print np.around(100*np.mean(scores), 2), np.around(100*np.var(scores), 2)


def clf_abc():
  csv_deleted_fname = open('featset_deleted.csv', 'r')
  deleted_dataset = np.genfromtxt(csv_deleted_fname, skip_header=1, delimiter=",", usecols=(0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,48))
  csv_deleted_fname.close()

  csv_featset_normal = open('featset_normal.csv', 'r')
  normal_dataset = np.genfromtxt(csv_featset_normal, skip_header=1, delimiter=",", usecols=(0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,48))
  csv_featset_normal.close()

  print deleted_dataset.shape, normal_dataset.shape

  data_0 = normal_dataset[:, 1:]
  data_1 = deleted_dataset[:, 1:]


  # #np.random.shuffle(normal_dataset)
  # #np.random.shuffle(deleted_dataset)
  print data_0.shape, data_1.shape

  clf_dataset = np.vstack((data_0, data_1))
  X = clf_dataset[:, :-1]
  y = clf_dataset[:, -1]

  print X.shape, y.shape

  model = AdaBoostClassifier(n_estimators=300)
  accuracies = list()
  f1_scores = list()
  aucs = list()

  scoring_funcs = ['f1', 'accuracy', 'roc_auc']

  for scoring_func in scoring_funcs:
    print scoring_func,
    scores = cross_val_score(model, X, y, cv=10, scoring=scoring_func)
    print np.around(100*np.mean(scores), 2), np.around(100*np.var(scores), 2)



def clf_abcd():
  csv_deleted_fname = open('featset_deleted.csv', 'r')
  deleted_dataset = np.genfromtxt(csv_deleted_fname, skip_header=1, delimiter=",")
  csv_deleted_fname.close()

  csv_featset_normal = open('featset_normal.csv', 'r')
  normal_dataset = np.genfromtxt(csv_featset_normal, skip_header=1, delimiter=",")
  csv_featset_normal.close()

  print deleted_dataset.shape, normal_dataset.shape

  data_0 = normal_dataset[:, 1:]
  data_1 = deleted_dataset[:, 1:]


  # #np.random.shuffle(normal_dataset)
  # #np.random.shuffle(deleted_dataset)
  print data_0.shape, data_1.shape

  clf_dataset = np.vstack((data_0, data_1))
  X = clf_dataset[:, :-1]
  y = clf_dataset[:, -1]

  print X.shape, y.shape


  model = AdaBoostClassifier(n_estimators=300)
  accuracies = list()
  f1_scores = list()
  aucs = list()
      
  scoring_funcs = ['f1', 'accuracy', 'roc_auc']

  for scoring_func in scoring_funcs:
    print scoring_func,
    scores = cross_val_score(model, X, y, cv=10, scoring=scoring_func)
    print np.around(100*np.mean(scores), 2), np.around(100*np.var(scores), 2)


print '***** A ****'
clf_a()

print '***** A + B ****'
clf_ab()

print '***** A + B + C ****'
clf_abc()

print '***** A + B + C + D ****'
clf_abcd()


