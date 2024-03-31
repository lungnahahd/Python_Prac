# Python_Prac
Python을 활용한 알고리즘 학습
-------------------------
## 코딩 문제를 푸는 큰 줄기!
### 1. 제일 먼저 문제를 확실하게 이해하기
### 2. 몇 가지 예를 적용해보고 제대로 이해하고 있는지 확인하기
### 3. 적절한 알고리즘을 적용하고 그 알고리즘이 예제에 잘 들어 맞는지 확인해보기
### 4. 특별 케이스(경계 값...)도 빼먹지 말고 생각하기
### 5. 문제를 풀다가 막히면 또 다른 예시들을 적용해보면서 풀이법을 떠올리기
### cf) 성능에 대한 판단을 빅 오 분석법을 적용해서 수시로 판단해주기
![코테 오류 확인 절차](https://user-images.githubusercontent.com/67555400/152671247-7244ed46-e86e-489c-8e05-2647e4c82d6e.PNG)
----------------------
## 시간 복잡도
### 참고로!! 파이썬은 1초에 대략 2000만 건의 연산을 수행할 수 있다고 생각하고 항상 문제에 접근하기!! 
### for문 1억번에 1초가 걸린다고 판단하기 (10^8)
#### N<=20 이면 왠만하면 모든 경우에서 통과
#### N=100 이면 4중 for문까지 가능
#### N=500 이면 3중 for문까지 가능
#### N=1000 이면 O(N^2), O(N^2logN) 가능
#### N=10만 이면, O(N), O(NlogN), O(logN), O(1) 가능
  * 위의 시간 복잡도를 코드 구현 전에 항상 떠올리고, 시간 복잡도가 넘치면 다른 효율적인 코드를 생각해서 구현하기!!
------------------
## 공간 복잡도
### int 기준
<img width="318" alt="스크린샷 2024-02-04 오후 11 16 46" src="https://github.com/lungnahahd/Python_Prac/assets/67555400/1a103f64-fed6-459f-80a1-a315f853afb4">

-----------------------------
## 오류 판단하기
### 코드 작성시 원하는 출력이 나오지 않는다면, 아래의 방법들로 판단해보기
#### 1. 디버깅
  * ide를 사용해서 편리하게 조사식을 이용해서 특정 위치까지의 변수 값이나 함수 과정들을 살펴보는 것이 가능
#### 2. print()
  * ide를 이용하지 못하는 경우 주로 사용, 보다 편리하고 직관적으로 값을 확인할 수는 있으나, 코드 자체가 복잡한 경우 사용이 어렵다는 단점이 존재
#### 3. asset 조건, "조건을 만족하지 않는 경우 출력"
  * 해당 위치에서 특정 변수 값등에 대한 확신을 얻고 싶은 경우 사용 가능
  * 조건을 만족하지 않는 경우 해당 위치에서 멈추고 출력을 보여줌

--------------
![코드트리](https://user-images.githubusercontent.com/67555400/156593719-6dcb23b1-0bb4-413f-a23a-34c4884ded06.PNG)
