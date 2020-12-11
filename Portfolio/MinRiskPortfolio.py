import numpy as np
import pickle
import matplotlib.pyplot as plt
import tensorflow as tf

with open("Covariance.pickle", "rb") as handle:
    raw = pickle.load(handle)
    cov = raw["covariance"]

writer = tf.summary.create_file_writer("/tmp/mylogs")
def Get_Min_Risk(Cov):
    N = Cov.shape[0]
    X = tf.Variable(shape=[N, 1], trainable=True, initial_value=np.zeros([N, 1]), dtype=tf.float32)
    for step in range(10000):
        with tf.GradientTape() as tape:
            W = tf.sigmoid(X)
            W = W / tf.reduce_sum(W)
            opt = tf.keras.optimizers.Adam(learning_rate=1)
            loss = tf.multiply(tf.matmul(W, tf.transpose(W)), Cov)
            loss = tf.reduce_sum(loss * loss)
            gradients = tape.gradient(loss, X)
            opt.apply_gradients([(gradients, X)])
            print(loss, X)
            with writer.as_default():
                tf.summary.scalar("loss", loss, step=step)
                writer.flush()
    return W, loss

Weight, Risk = Get_Min_Risk(tf.constant(cov, dtype=tf.float32))
Portfolio = [(Weight[i][0].numpy().tolist(), raw["manifest"][i]) for i in range(cov.shape[0])]
print(Portfolio)
print(Risk)

with open("MinRiskPortfolio.pickle", "wb") as handle: 
    pickle.dump((Risk, Portfolio), handle)
