import tensorflow as tf
import os
# TensorFlow 오류 로그 off
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '2'

input_const = tf.constant(1.5)

input_var = tf.Variable(2.0)
input_var.assign_add(1)

output = input_const * input_var

# tf.print(output)

a, b = tf.constant([[1], [2], [3]]), tf.constant([[1, 2, 3, 4]])

"""
데이터 형태
a = [
  [1]
  [2]
  [3]
]

b = [
  [1 2 3 4]
]
"""

tf.print(a)
tf.print(b)

cond = tf.less(a, b)
x = tf.multiply(a, a)
y = tf.multiply(b, -1)

tf.print(cond)
tf.print(x)
tf.print(y)
tf.print(tf.where(cond, x, y))

"""
tf.less(a, b) = [
  [-1  1  1 1]
  [-1 -1  1 1]
  [-1 -1 -1 1]
]

tf.multiply(b, -1) = [
 [1 2 3 4]
 [1 2 3 4]
 [1 2 3 4]
]

tf.multiply(a, a) = [
 [1 1 1 1]
 [2 2 2 2]
 [3 3 3 3]
]
"""

"""

"""













