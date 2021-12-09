def train_model():
    pix = []

    for i in range(784):
        pix.append('pixel' + str(i))

    features = pix

    X = df.loc[:, features].values
    y = df.loc[:, 'class'].values

    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.30, random_state=100)
    y_train = y_train.ravel()
    y_test = y_test.ravel()
