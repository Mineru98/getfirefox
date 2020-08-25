# Step 1

## 기본 용어
### 플로우(Flow)
Flow란 Graph이다.
즉 모든 계산을 쉽게 하기 위해서 각각의 연산을 잘게 쪼개고 이것을 Graph로 연결 한 것이다.
미분 Chain Rule 같은것을 생각해보면 왜 연산이 간단해 지는지 알 수 있다.

### Graph, Node, Edge
선언부와 실행부가 다르다

TensorFlow코드 상에서 a=1을 선언해도 추후에 이것이 반영되는 것이지 지금 당장 변수 a가 1로 assgin된것은 아니다.
이러한 부분이 기본적인 python 프로그래밍과는 다른점이다. 
이러한 동작 매커니즘을 생각해보면 결국 앞으로 어떻게 동작 할 것이다라는 계획을 Graph로 표현한것이 TensorFlow가 되는 것이다.

- Operation: 동작을 정의한 것
- Node: Operation 정의를 포함한 것
- Edge: Node와 Node를 연결한 것

### 오퍼레이션(Operation)
그래프 상의 노드는 오퍼레이션(줄임말 op)으로 불립니다. 오퍼레이션은 하나 이상의 텐서를 받을 수 있습니다. 오퍼레이션은 계산을 수행하고, 결과를 하나 이상의 텐서로 반환할 수 있습니다.

### 텐서(Tensor)
내부적으로 모든 데이터는 텐서를 통해 표현됩니다.
텐서는 일종의 다차원 배열(Array)인데, 그래프 내의 오퍼레이션 간에는 텐서만이 전달됩니다.

### 세션(Session)
그래프를 실행하기 위해서는 세션 객체가 필요합니다.(TensorFlow 1.x 기준)
세션은 오퍼레이션의 실행 환경을 캡슐화한 것입니다.

### 변수(Variables)
변수는 그래프의 실행시, 패러미터를 저장하고 갱신하는데 사용됩니다.
메모리 상에서 텐서를 저장하는 버퍼 역할을 합니다.

## 개념
오퍼레이션은 Graph로 이뤄진다.

Graph는 Session Context에 들어가서 처리 된다.

Data는 Tensor로 표현된다.

상태 정보는 Variables로 관리 된다.

## 자료 출처
[참고 자료1](https://gist.github.com/haje01/202ac276bace4b25dd3f)
[참고 자료2](https://goodtogreate.tistory.com/entry/TensorFlow-기본-개념-2)
[참고 자료3](https://goodtogreate.tistory.com/entry/TensorFlow-기본-개념?category=620143)