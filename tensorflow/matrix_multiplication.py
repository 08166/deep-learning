import tensorflow as tf

# TensorFlow : 텐서 (Tensor), 그래프(Graph), 세션(Session)등의 기본 개념을 이해해야 한다.
# 텐서(Tensor) : 다차원 배열 (Numpy의 ndarray와 유사)
# 그래프(Graph) : 데이터 흐름을 나타내는 객체 (연산과 데이터를 노드와 엣지로 표현)
# 세션(Session) : 그래프를 실행하는 환경 (실행을 위한 메서드를 제공)
# 텐서플로우 2.0 버전부터는 즉시 실행(eager execution)이 기본으로 활성화 되어 있어서 세션을 사용하지 않아도 된다.
# 즉시 실행(eager execution) : 그래프를 생성하지 않고 연산을 즉시 실행하는 명령형 프로그래밍 환경

print (tf.__version__) # 버전 확인
print (tf.reduce_sum(tf.random.normal([1000, 1000]))) # 랜덤 텐서 생성 및 합계 계산

# 예제 : 간단한 텐서 연산 예제를 구하기 ( 행렬 곱셈 )
# 결과를 Jupyter Notebook으로 작성 후 해당 파일을 basic_conepts/ 로 저장한다.
# 파일 내용 : 행렬 곱셈 연산 예제
# 행렬 곱셈 연산 예제
a = tf.constant([[1, 2], [3, 4]])
b = tf.constant([[5, 6], [7, 8]])
c = tf.matmul(a, b)
print(c) # 행렬 곱셈 결과 출력

