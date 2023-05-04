questions = [
["1:The International Literacy Day is observed on","Sep 8","Nov 28","May 2","Sep 22",1],
["2:The language of Lakshadweep a Union Territory of India is","Tamil","Hindi","Malyalam","Telugu",3],
["3:Bahubali festival is related to","Islam","Hinduism","Buddism","Jainism",4],
["4:September 27 is celebrated every year as","Teachers' Day","National Integration Day","World Tourism Day","International Literacy Day",3],
["5:Who is the author of the epic 'Meghdoot","Vishakadatta","Valmiki","Banabhatta","Kalidas",4],
["6:Pongal is a popular festival of which state","Karnataka","Kerala","Tamil Nadu","Andhra Pradesh",3],
["7:The first month of the Indian national calendar","Magha","Chaitra","Ashadha","Vaishakha",2],
["8:Which of the following is not a dance from Kerala?","Karnataka","Kerala","Tamil Nadu","Andhra Pradesh",3],
["9:Which of the following was the first Indian state to issue photo identity cards to its voters?","Tamil Nadu","Rajasthan","West Bengal","Haryana",4],
["10:What is the largest object in our solar system?","Titan","Jupiter","Sun","Alpha Centauri",2],
["11:Which of these are names of national parks located in Madhya Pradesh?","Krishna and Kanhaiya","Krishna and Kanhaiya","Ghanshyam and Murari","Girdhar and Gopal",2],
["12:Who wrote the introduction to the English translation of Rabindranath Tagore’s Gitanjali?","P.B. Shelley"," Alfred Tennyson","W.B. Yeats","T.S. Elliot",3],
["13:Who is the only MP in the current Lok Sabha who is also an Olympic medalist?","Abhinav Bindra","Rajyavardan Singh Rathore","Karnam Maleshwari"," Gagan Narang",2],
["14:Which newspaper once kept its editorial cloumn blank as a mark of protest against the emergency of 1975?"," Hindustan Times","The Hindu"," The Indian Express","The Times of India",3],
["15:How many religions are there in India?","6","7","8","4",1],
["16:Which is known as direct tax….."," Custom tax","Income tax","Property tax"," Excise tax",2],
["17:A coin of what value is called as “Athhanni”?","1 Rupee","25 Paise","50 Paise","2 Rupees",3],
["18:Who was the first person to be awarded the Bharat Ratna posthumously?","Rajiv Gandhi","Vinoba Bhave","Lal Bahadur Shastri"," Indira gandhi",3]
]
levels = [1000, 2000, 3000, 5000, 10000, 20000, 40000, 80000, 160000, 320000, 640000, 1250000, 2500000, 5000000, 10000000, 30000000, 50000000, 70000000]
money = 0
for i in range(0,len(questions)):
    question = questions[i]
    print(f"\nQuestion For Rs. {levels[i]}")
    print(f"{question[0]}")
    print(f"a. {question[1]}          b.{question[2]}")
    print(f"c. {question[3]}          d.{question[4]}")
    reply = int(input("Enter your answer (1-4) or 0 to quit:\n"))
    if(reply == 0):
        money = levels[i-1]
        break
    if(reply == question[-1]):
        print(f"Correct answer , You have won Rs.{levels[i]}")
        if(i == 4):
            money = 10000
        if(i == 9):
            money = 320000
        if(i == 14):
            money = 10000000
        if(i == 16):
            money = 70000000
    else:
        print("Wrong answer ! You out of this game.")
        break
    print(f"Your take home money is Rs.{money}")
