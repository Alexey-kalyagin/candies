
import random 


candies = int(input("Введите количество конфет, сладкоежки: " ))
candiesPl1 = 0
bot = 0
count = random.randint(1,6)
print(f"Пока в карзине {candies} конфет") 
print()
print(f"На костях выполо {count}")
print()

if candies>0:
    while True:
        if count %2 == 0:
            print("Ходит Player1") 
            print()
            player = int(input("Сколько хочешь взять конфет? - " )) 
            print()
            if player<=20:
                candiesPl1 += player
                candies -= player
                count+=1
                if candies<=0:
                       
                    if count%2!=0:
                        print ("Player1 win")
                        break
                    else:
                        print ("Bot win")
                        break
            else:
                print("Слишком много конфет, жадина)")
            
        else:
            print("Ходит Bot") 
            print()
            player = int(random.randint(1,20)) 
            print (f"Bot взял - {player} конфет")
            print()
            bot += player
            candies -= player
            count+=1
            if candies<=0:
                if count%2!=0:
                    print ("Player1 win")
                    break
                else:
                    print ("Bot win")
                    break
                       
        print(f"Конфеты первого игрока {candiesPl1}")
        print(f"Конфеты Bot {bot}")
        print(f"Остаток конфет {candies}")
        print()