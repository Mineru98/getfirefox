import tensorflow as tf

# 1x2 행렬을 생성하는 상수 연산을 만듭니다.
# 연산은 기본 그래프에 노드로 추가됩니다.
# 생성자가 반환 한 값은 상수 작업의 출력을 나타냅니다.
matrix1 = tf.constant([
  [3., 3.]
])

# 2x1 행렬을 생성하는 또 다른 상수를 만듭니다.
matrix2 = tf.constant([
  [2.],
  [2.]
])

# 'matrix1'및 'matrix2'를 입력으로 사용하는 Matmul 연산을 만듭니다.
# abs() 반환 된 값 'product'는 행렬 곱셈의 결과를 나타냅니다.
product = tf.matmul(matrix1, matrix2)

"""
# TensorFlow 1.x 에서는 정의부와 실행부가 따로 나뉘어 실행 되었지만
# 2.x 부터는 정의부만 존재하고 실행부는 프로그래머가 작성하지 않는 메커니즘으로 변경 되었다고 한다.

기본 그래프를 시작합니다.
sess = tf.Session()

matmul op를 실행하기 위해 우리는 세션 'run ()'메서드를 호출하고
matmul op의 출력을 나타내는 'product'를 전달합니다.
이것은 우리가 matmul op의 출력을 얻기를 원한다는 것을 호출에 나타냅니다.

따라서 'run (product)'호출은 그래프에서 두 개의 상수와 matmul이라는 세 개의 연산을 실행하게합니다.

연산의 출력은 '결과'에 numpy 'ndarray'객체로 반환됩니다.
result = sess.run(product)
print(result)

#완료되면 세션을 닫습니다
sess.close()
"""

print(product)

