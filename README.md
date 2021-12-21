# Final Project

​	numpy의 기능을 이용하여 출산율과 다른 사회적 수치 간 연관성을 분석해보았습니다.



## Contents

* [설명](#1)
* [분석 결과](#2)
* [참조](#3)
* [라이선스](#4)



### 설명 <a name="1"></a>

​	한국의 출산율에 대해서 분석하기 위해 통계청에서 조사한 데이터를 사용하였습니다.
​	사용한 자료들은 다음과 같습니다.

​	* [시군구/합계출산율, 모의 연령별 출산율](https://kosis.kr/statHtml/statHtml.do?orgId=101&tblId=DT_1B81A17&conn_path=I2)

​	* [아파트 매매 실거래가격지수 시군구 분기별](https://kosis.kr/statHtml/statHtml.do?orgId=408&tblId=DT_KAB_11672_S5)

​	* [시군구/인구동태건수 및 동태율(출생,사망,혼인,이혼)](https://kosis.kr/statHtml/statHtml.do?orgId=101&tblId=DT_1B8000I&conn_path=I2)

​	상관 관계 분석은 출산율과 아파트 가격 지수, 출산율과 이혼율의 두 가지 경우를 진행하였습니다.
​	또한 2020년까지의 연도별 출산율에 대해 Curve Fitting을 이용하여 2035년까지의 출산율을 예측해보고자 하였습니다.



### 분석 결과 <a name="2"></a>

![Figure_1](https://user-images.githubusercontent.com/70771742/146911624-1a9b5ef9-28be-49b3-8611-32d190aee5bf.png)
​	2009년부터 2020년까지의 지역별 출산율과 아파트 가격 지수의 상관 관계는 -0.693으로 계산되며 두 수치는 유의미한 negetive 관계를 가지고 있음을 알 수 있었습니다.

![Figure_2](https://user-images.githubusercontent.com/70771742/146911618-0c479859-6cc7-47a8-a334-e2a40ee39496.png)
​	2000년부터 2020년까지의 지역별 출산율과 이혼율의 상관 관계는 0.172로 계산되며 두 수치 간 유의미한 관계를 발견할 수 없었습니다.

![Figure_3](https://user-images.githubusercontent.com/70771742/146911622-9b87bee6-4172-448a-b405-a19a34cb8d2f.png)
​	2000년부터 2020년까지의 전국 출산율에 대해 Curve Fitting을 이용하여 2035년까지의 출산율 동향을 예측해보고자 하였습니다. 출산율이 계속하여 감소하는 경우 0 미만의 값을 방지하기 위해 0으로 수렴할 수 있도록 다항함수를 지수함수와 함께 사용하였습니다. 또한 음수의 출산율을 방지하기 위해 RMS를 사용하여서 2&#42;exp와 3&#42;exp를 설계하였습니다.



### 참조 <a name="3"></a>

​	지수함수를 이용한 curve fitting의 경우 다음의 내용을 참조하였습니다.

​	[How to do exponential and logarithmic curve fitting in Python](https://www.kite.com/python/answers/how-to-do-exponential-and-logarithmic-curve-fitting-in-python)



### 라이선스 <a name="4"></a>

​	[MIT License](http://opensource.org/licenses/MIT)
