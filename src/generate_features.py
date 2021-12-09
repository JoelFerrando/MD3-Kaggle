def generate_features(df):
    pix = []

    for i in range(784):
        pix.append('pixel'+str(i))

    features = pix

    X = df.loc[:, features].values
    y = df.loc[:,'class'].values

    return X, y