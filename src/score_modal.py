def kNN():
    knn = KNeighborsClassifier(n_neighbors=3)
    scores = cross_val_score(model, X, y, cv=10, scoring='accuracy')
    print(scores)

    print(scores.mean())
    scores.std()
    # choose k between 1 to 31
    k_range = range(1, 31)
    k_scores = []
    # use iteration to caclulator different k in models, then return the average accuracy based on the cross validation
    for k in k_range:
        knn = KNeighborsClassifier(n_neighbors=k)
        scores = cross_val_score(knn, X, y, cv=5, scoring='accuracy')
        k_scores.append(scores.mean()
                        
    knn.fit(X_train, y_train)
    y_pred = knn.predict(X_test)
    print('K-Nearset Neighbour Classifier - Accuracy: ', metrics.accuracy_score(y_test, y_pred) * 100)