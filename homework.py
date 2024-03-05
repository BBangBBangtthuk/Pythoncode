# 1번 평균 점수 구하기
# a = 80
# b = 75
# c = 55
# average = (a+b+c)/3
# print(average)

# 2번 : 홀수, 짝수 판별하기
# a = 13
# a % 2 == 0
# print (a)

# 3번 주민등록번호 나누기 
# pin = "881120-1068234"
# yyyymmdd = pin[0:6]
# num =pin[7:]
# print(yyyymmdd)
# print(num)

# 4번 주민등록번호 인덱싱
# pin = "881120-1068234"
# print(pin[7:9])

# 5번 문자열 바꾸기
# a = "a:b:c:d"
# b = a.replace(":","#")
# print(b)

# 6번 리스트 역순 정리하기
# a = [1,3,5,4,2]
# a.sort()
# a.reverse()
# print(a)

# 7번 리스트를 문자열로 만들기
# a = ['Life', 'is', 'too', 'short']
# result = " " .join(a)
# print(result)

# 8번 튜플 더하기 
# a = (1,2,3)
# a = a + (4,)
# print (a)

# 9번 딕셔너리의 키
# a = dict()
# a['name'] = 'python' 
# a[('a',)] = 'python'
# a[[1]]  = 'python' # list 는 변하는 값이다.
# a[250] = 'python'
# print (a[250])

# 10번 딕셔너리 값 추출하기
# a = {'A' : 90, 'B':80, 'C':70}
# result = a.pop('B')
# print(a)
# print(result)

# 11번 리스트에서 중복 제거하기
# a = [1,1,1,2,2,3,3,3,4,4,5]
# aSet = set(a)
# b = list(aSet)
# print(b)

# 12번 파이썬 변수
# a = b = [1,2,3]
# a[1] = 4
# print (b)

#########################################################################################################################################################################


# 되새김 문제  149p
# 1. 조건문의 참과 거짓

# a = "Life is too short, you need python"

# if "wife" in a:
#     print ("wife")
# elif "python" in a and "you" not in a:
#     print ("python")
# elif "shirt" not in a:
#     print ("shirt")
# elif "need" in a:
#     print ("need")
# else:
#     print("none")

# # 2. 3의 배수의 합 구하기 
# result = 0
# i = 1
# while i <= 1000:
#     if i %3 == 0:
#         result +=i
#     i +=1

# print(result)

# 3. 별 표시하기
# i = 0
# while True:
#     i +=1
#     if i > 5  :break
#     print('*'*i)

# 4. 1부터 100까지 출력하기
# for i in range(1,101):
#     print (i)


# 5. 평균 점수 구하기
# A = [70,60,55,75,95,90,80,80,85,100]
# total = 0
# for score in A:
#     total += score
# average = (total)/len(A)
# print(average)

# 6. 리스트 컴프리헨션 사용하기
# numbers = [1,2,3,4,5]
# result = []
# for n in numbers:
#     if n%2 == 1:
#         result.append(n*2)
        
# numbers = [1,2,3,4,5]
# result = [num*2 for num in numbers if num%2==1]
# print (result)

# 되새김 문제 185쪽
# def is_odd(number):
#     if number%2 ==1:
#         return True
#     else:
#         return False

# print(is_odd(3))
# print(is_odd(2))

# # 2번 모든 입력의 평균값 구하기
# def avg_numbers(*args):
#     result = 0
#     for i in args:
#         result += i
#     return result / len(args)
# print(avg_numbers(1,2))
# print(avg_numbers(1,2,3,4,5))

# # 3. 프로그램 오류 수정하기
# input1 = input("첫 번째 숫자를 입력하시오:")
# input2 = input("두 번째 숫자를 입력하시오:")

# total =int(input1) + int(input2)
# print("두 수의 합은 %s입니다" % total)

# 4. 출력결과가 다른 하나는?
# print("you" "need" "python")
# print("you" + "need" + "python")
# print("you", "need", "python") # , 는 띄어쓰기다.
# print("".join(["you","need","python"]))

# f1 = open("test.txt", 'w')
# f1.write("Life is too short")
# f1.close()

# f2 = open("test.txt", 'r')
# print(f2.read())
# f2.close()

# 6번 사용자 입력 저장하기
# user_input = input("저장할 내용을 입력하세요")
# f = open('test.txt', 'a')
# f.write(user_input)
# f.write("\n")
# f.close()

# 7번 : 파일의 문자열 바꾸기
# f = open('test.txt','r')
# body = f.read()
# f.close()

# body = body.replace("java", "python")
# f = open('test.txt', 'w')
# f.write(body)
# f.close()

# import sys

# numbers = sys.argv[1:]
# result = 0

# for number in numbers:
#     result += int(number)
    
# print(result)

    