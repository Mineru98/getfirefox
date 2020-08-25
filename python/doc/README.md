# TensorFlow 2.3.0 API

## tf
### tf.print

Tensor의 결과 값을 tf class를 출력하는게 아닌 Tensor가 가지고 있는 value를 출력하는 메소드

```python
>>> import tensorflow as tf
>>> input_const = tf.constant(1.5)
>>>print(input_const)
tf.Tensor(1.5, shape=(), dtype=float32)
```

```python
>>> import tensorflow as tf
>>>input_const = tf.constant(1.)
>>>tf.print(input_const)
1.5
```

### tf.range

for문 같은 작동을 한다.
- 첫번째 인자(start)는 초기값
- 두번째 인자(limit)는 임계값
- 세번째 인자(delta)는 증감값
- 네번째 인자(dtype)는 자료구조
- 다섯번째 인자(name)는 변수 이름
```python
>>> start = 3
>>> limit = 18
>>> delta = 3
>>> tf.range(start, limit, delta)
tf.Tensor([ 3  6  9 12 15], shape=(5,), dtype=int32)
```

### tf.rank

Tensor의 shape의 깊이 값

### tf.where

tf.where(조건 텐서, 참일 경우의 출력 텐서,거짓일 경우의 출력 텐서)

## tf.math
### tf.math.equal(=tf.equal)

```python
>>> a = tf.constant([1,2])
>>> b = tf.constant([1,3])
>>> result = tf.equal(a, b)
>>> tf.print(result)
[True, False]
```

### tf.math.not_equal(=tf.not_equal)

```python
>>> a = tf.constant([1,2])
>>> b = tf.constant([1,3])
>>> result = tf.not_equal(a, b)
>>> tf.print(result)
[False, True]
```

### tf.math.less(=tf.less)
### tf.math.less_equal(=tf.less_equal)
