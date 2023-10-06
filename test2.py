pingpong_list = ["나영", "예진", "원빈", "현빈"]

results = []

def create_contents_of_mail(name):
    a = "2023-10-06"
    b = "10:30 AM"
    c = "트레이닝 복"

    mail = f"한국교통대학교 천하제일 탁구대회, {name} 탁구 대회에 참여해주셔서 감사합니다.\n"
    mail += f"행사 일시: {a}, 시간: {b}, 복장: {c}\n"
    mail += f"행사 당일에 뵙겠습니다. {name}님 감사합니다."

    return mail

for participant in pingpong_list:
    mail = create_contents_of_mail(participant)
    results.append(mail)

for result in results:
    print(result)
