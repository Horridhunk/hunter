city = 'Nairobi Mombasa Kisumu Nakuru Eldoret Thika Nyeri Machakos Malindi Kitale Kakamega Kisii Garissa Wajir Mandera Nakuru Narok KerichoBungoma Busia Siaya Kisumu Homa Bay Migori Kisii Nyamira Nairobi Mombasa Kisumu  Nakuru Eldoret Thika Nyeri Machakos Malindi Kitale Kakamega Kisii Garissa Wajir Mandera Nakuru'
city_list = city.split(' ')
wing = ["A","B"]
start = "eBn"

for i in wing:
    for j in range(54):
        for k in city_list:
            h=(str(j)+i)
            password = start+h+"_"+k
        print(password)
        # print(city_list[j])
