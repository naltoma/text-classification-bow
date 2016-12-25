import dataset
import Stemmer
import numpy as np
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.feature_extraction.text import TfidfTransformer

# ready dataset
lawdata, target, target_names = dataset.load(config_file="config.json")
stemmed_data = Stemmer.mecab_stemmer(lawdata)
print('\n### stemmed_data')
print(stemmed_data)

# make bag-of-words
count = CountVectorizer()
bag = count.fit_transform(stemmed_data)
#print(count.vocabulary_)
print('\n### feature_names')
print(count.get_feature_names())
print('\n### bag')
print(bag.toarray())

# tune the bag with TF-IDF
tfidf = TfidfTransformer(use_idf=True, norm='l2', smooth_idf=True)
np.set_printoptions(precision=2)
data = tfidf.fit_transform(count.fit_transform(stemmed_data)).toarray()
#print(tfidf.fit_transform(count.fit_transform(stemmed_data)).toarray())
print('\n### vectors with TF-IDF')
print(data)

### machine learning
# dataset
X_train = data[:] # using all data
y_train = target[:]
X_test = data[:] # using all data = close test
y_test = target[:]

# model + grid search
from sklearn.grid_search import GridSearchCV
from sklearn.pipeline import Pipeline
from sklearn.linear_model import LogisticRegression

pipline = Pipeline([('clf', LogisticRegression(random_state=0))])
param_grid = {'clf__penalty': ['l1', 'l2'],
               'clf__C': [1.0, 10.0, 100.0]}

grid_search = GridSearchCV(pipline, param_grid, n_jobs=-1, cv=2, verbose=1)
grid_search.fit(X_train, y_train)

print("\n### best parameter")
best_parameters = grid_search.best_estimator_.get_params()
for param_name in sorted(best_parameters.keys()):
    print("\t%s: %r" % (param_name, best_parameters[param_name]))

print("\n### best score")
print("CV Accuracy: %.3f" % grid_search.best_score_)

print("\n### test by best estimator")
model = grid_search.best_estimator_
results = model.score(X_test, y_test)
print("Test Accuracy: ", results)
