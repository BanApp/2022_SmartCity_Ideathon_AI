import random

car = int(random.random() * 100) #사물인식에 감지된 차량의 대수(랜덤)
people = int(random.random() * 100) #사물인식에 감지된 보행자의 수(랜덤)

print("====<차량과 보행자의 수>====")
print("대기중인 차량의 대수: ",car)
print("대기중인 보행자의 수: ",people)

time_set = random.randrange(0,24) #랜덤으로 시간 설정

car_weight = 0.5 #차량 가중치 기본값
people_weight = 0.5 #보행자 가중치 기본값

if (time_set >= 8 and time_set <= 9) or (time_set >= 17 and time_set <= 18): #출근시간 & 퇴근시간
    car_weight += 0.15 #차량 가중치 증가
    people_weight -= 0.15 #보행자 가중치 감소

elif (time_set >= 12 and time_set <= 13): #점심시간(보행자 통행량 많음)
    car_weight -= 0.15 #차량 가중치 감소
    people_weight += 0.15 #보행자 가중치 증가

car_value = car*car_weight #차량 수 * 차량 가중치 = 차량 최종 가중치
people_value = people*people_weight #보행자 수 * 보행자 가중치 = 보행자 최종 가중치

print()
print("========<가중치>========")
print("현재 시각:",time_set)
print("실시간 차량의 가중치: ",car_value)
print("실시간 보행자의 가중치: ",people_value)
print()

accident = random.randrange(0,20)

#####각각 1/10 확률로 무단횡단과 정지선 침범 발생#####
if accident == 0 or accident == 12:
    print("=========<경고음>=========")
    print("무단횡단자가 있습니다. 조심하세요!")
    print()

elif accident == 4 or accident == 19:
    print("=======<경고음>=======")
    print("차량이 정지선을 넘었습니다. 조심하세요!")
    print()
#############################################

print("=========<신호등>=========")
if car_value > people_value: #차량용 신호등의 가중치가 보행자의 가중치보다 큼
    print("차량용 신호등에 초록불이 켜집니다.")
else: #보행자 신호등의 가중치가 차량용 신호등의 가중치보다 큼
    print("보행자용 신호등에 초록불이 켜집니다.")
