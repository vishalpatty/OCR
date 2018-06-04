def LeNetbuild(width, height, depth, classes, weightsPath=None):
    # initialize the model
    model = Sequential()
        # first set of CONV => RELU => POOL
    model.add(Convolution2D(20, 3, 3, border_mode="same",
        input_shape=(height, width, depth)))
    model.add(Activation("relu"))
    model.add(MaxPooling2D(pool_size=(2, 2), strides=(2, 2)))
    model.add(Dropout(0.25))
        # second set of CONV => RELU => POOL
    model.add(Convolution2D(50, 5, 5, border_mode="same"))
    model.add(Activation("relu"))
    model.add(MaxPooling2D(pool_size=(2, 2), strides=(2, 2)))
    model.add(Dropout(0.3))
        # set of FC => RELU layers
    model.add(Flatten())
    model.add(Dense(500))
    model.add(Activation("relu"))
        # softmax classifier
    model.add(Dense(classes))
    model.add(Activation("softmax"))
    # if a weights path is supplied (inicating that the model was
    # pre-trained), then load the weights
    if weightsPath is not None:
        model.load_weights(weightsPath)

    # return the constructed network architecture
    return model
