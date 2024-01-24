


x = 1

phone_keywords =["Apple","apple", "Iphone", "iPhone","iphone", "Samsung","samsung","Oneplus", "oneplus","OnePlus","pixel","Pixel","Google","google","camera","Camera"]

########################################################################
# We used the split function to split a sentence into a list  
# We found out about it from this website <  https://pythonbasics.org/split/  >

def extract_brand(sentence):
    List = sentence.split() 
    for brand in List:
        if brand in phone_keywords:
            return brand
    return None

# We used the split function to split a sentence into a list  
# We found out about it from this website <  https://pythonbasics.org/split/  >
########################################################################




########################################################################
# We used “Regular Expression Operation” from python library
# It is used to extract an integer from a sentence 
# Here is the link to the python library    <  https://docs.python.org/3/library/re.html  >


import re
def if_brand_samsung(line):
    number = re.search(r'\d+',line)
    price = int(number.group())
# We used “Regular Expression Operation” from python library
# It is used to extract an integer from a sentence 
# Here is the link to the python library    <  https://docs.python.org/3/library/re.html  >
########################################################################



    if price >= 1200 and price < 1700:
        print("Bot :Damn!! You have lot of money to spend on a smartphone. For this much money I would prefer you to take a look into the latest samsung S23 ultra, as this have lots of latest features, best camera in the market and a really good software experience with guaranteed 4 years of software updates.")
    elif price >=800 and price <=1199:
        print("Bot :Thats a really good price range to buy a samsung phones. I would recommend you to look at the latest Samsung Galaxy S23 and S23+. Both phones have almost the exact same specs in paper, however, the differnce is in the size. If you like smaller form factor go for S23 as this phone have a compact build. If you are guy who have bigger hand you might want to buy S23+ because it is much bigger version of S23. But keep in mind that smaller form factor will reduce the battery capacity (no one likes their phone to die in the middle of a game XD).")
    elif price >=300 and price <=799:
        print("Bot :hmmm...let me think. Oh! the Samsung Galaxy A series might be a good option for you. But if you don't mind using a used or reffurbished phones, you might get some good deals for the last year S series phones in this price range.")
    elif price>1700:
        print("Bot :Dude thats a lot of money. You dont need that much to buy the latest samsung flagship which is the samsung S23 ultra.")
    elif price<=299 and price >=0:
        print("Bot :Yo!! you are broke. Get a job, make some money and buy a good phone")



########################################################################
# We used “Regular Expression Operation” from python library
# It is used to extract an integer from a sentence 
# Here is the link to the python library    <  https://docs.python.org/3/library/re.html  >


def if_brand_apple(line):
    number = re.search(r'\d+',line)
    price = int(number.group())

# We used “Regular Expression Operation” from python library
# It is used to extract an integer from a sentence 
# Here is the link to the python library    <  https://docs.python.org/3/library/re.html  >
########################################################################


    if price < 449 and price >=0:
        print("Bot : Yo!! Are you broke??.There is no iphone that is cheaper than £449. You might want to save up some money to buy a good iphone...")
    elif price >= 449 and price <=600:
        print("Bot :I don't think its a good idea to buy an iphone at this price range...There is only the iphone SE series available at this price category, which is not an ideal phone for you if you use it most of the day because of its very low battery life. If you are ok with using refurbished iphones, try to get refurbished iphone 13 under £600, which is a great deal...")
    elif price >600 and price <794:
        print("Bot :For this price range I would personally recommend buying iphone 13. Although it is last years phone it is more than enough for every person.")
    elif price >=794 and price <1039:
        print("Bot :You have two options at this price range, one is iphone 14 and other one is iphone 14 plus. Both are similar in terms of specifications, the only difference is in the size and battery capacity. If you want a bigger phone go for iphone 14 plus, otherwise go for iphone 14...")
    elif price >=1039 and price <=2000:
        print("Bot :Bot :Oh! that's great. You can check the Apples latest iphone 14 pro or 14 pro max, both phones have everything the same except the pro max version is bigger and it has much better battery life. You can choose according to you usage.")
    elif price >2000:
        print("Bot :Dude! Thats a lot of money. You dont need that much to buy a great phone. You can get the latest iphones for less than £1700. Give some money to charity :)")






########################################################################
# We used “Regular Expression Operation” from python library
# It is used to extract an integer from a sentence 
# Here is the link to the python library    <  https://docs.python.org/3/library/re.html  >

        
def if_brand_oneplus(line):
    number = re.search(r'\d+',line)
    price = int(number.group())


# We used “Regular Expression Operation” from python library
# It is used to extract an integer from a sentence 
# Here is the link to the python library    <  https://docs.python.org/3/library/re.html  >
########################################################################


    if price >=0 and price <= 149:
        print("Bot : Hmm.... Looks like somebody is broke. First you need to get a job to make some money, then you will be able to buy your dream phone... XD")
    elif price >149 and price <= 249:
        print ("Bot : At this price range, it is not a good option to buy a oneplus phone. But you can find some good deals on used or refurbished oneplus devices.")
    elif price >249 and price <= 369:
        print("Bot : For this price range you can buy the OnePlus Nord 2T. It is a decent option for this price.")
    elif price >369 and price <= 700:
        print ("Bot : I would recommend you to buy the OnePlus 10R or 10 pro. Which is still a solid option for this range.")
    elif price >700 and price <= 800:
        print("Bot : Great! You can buy the latest flagship from OnePlus which is the OnePlus 11. It has all the greatest and latest features for a modern smart phone.")
    elif price > 800:
        print("Bot : Hmm.... To be fair, thats a lot of money for a OnePlus phone. You can check the latest flagship which is the OnePlus 11")
    else:
        print("Bot : Sorry... I did not understand what you said. Please be more specific about your price range next time... :)")





########################################################################
# We used “Regular Expression Operation” from python library
# It is used to extract an integer from a sentence 
# Here is the link to the python library    <  https://docs.python.org/3/library/re.html  >


        
        
def if_brand_pixel(line):
    number = re.search(r'\d+',line)
    price = int(number.group())


# We used “Regular Expression Operation” from python library
# It is used to extract an integer from a sentence 
# Here is the link to the python library    <  https://docs.python.org/3/library/re.html  >
########################################################################


    if price >=0 and price <= 300:
        print("Bot : Hmm.... Looks like you are broke. The cheapest pixel phone which is the pixel 6a starts from £300. Get a job and make some money, then you will be able to buy your dream phone... XD")
    elif price >300 and price <= 450:
        print ("Bot : At this price you can buy the pixel 6a. It is a great device if you like still photos. Don't expect any high end performance tho...")
    elif price >450 and price <= 650:
        print("Bot : For this price range you can buy the latest pixel 7. It is a really good option for you if your main focus is photograpy.")
    elif price >650 and price <= 900:
        print ("Bot : Oh wow! You can check out the google's latest pixel 7 pro. It is the flagship phone from google, which take breathtaking photos you should try it...")
    elif price >900:
        print("Bot : Actually, you don't need so much money to buy the latest flagship from Pixel which is the Pixel 7 pro.It is the flagship phone from google, which take breathtaking photos.... You should check that out...")
    else:
        print("Bot : Sorry... I did not understand what you said. Please be more specific about your price range next time... :)")






def give_feedback():
    phone_feedback = input("Bot :Did you find your phone from my recommendations? (yes/no)\nUser: ")
    if phone_feedback == "yes":
        print("Bot :Yayy, finally you got your dream phone! Cheers!!")
    elif phone_feedback == "no":
        print("Bot :Oh, my bad. Better luck next time :( I hope you will get a much better phone soon.")
    else:
        print("Bot :Sorry, I didn't understand your response. Please enter 'yes' or 'no'.\nUser: ")
        return

    if phone_feedback == "yes" or phone_feedback == "no":
        services_feedback = input("Bot :Did you like our services? (yes/no)\nUser: ")
        if services_feedback == "yes":
            improvement_feedback = input("Bot :That's great to hear! How can I improve my services?\nUser: ")
            return "Bot :Thank you for your feedback, I would love to meet you next time see you soon Bye.\n\n"
        elif services_feedback == "no":
            improvement_feedback = input("Bot :I'm so sorry to hear that. How can I improve my services?\nUser: ")
            return "Bot :Thank you for your feedback, I'll not disappoint you next time.\n\n"
        else:
            return "Bot :Sorry, I didn't understand your response. Please enter 'yes' or 'no' for whether you liked our services.\n\n"






spec_cam = ["camera","Camera"]  
brandList1 = ["Samsung","samsung"]
brandList2 = ["Apple","apple","iphone","Iphone","iPhone"]
brandList3 = ["Oneplus","oneplus","OnePlus"]
brandList4 = ["pixel","Pixel","Google","google"]
print("Bot : Hi there... I'm your personal chatbot to recommend phones according to your price preferrence. I can recommend phones from different brands like Apple, Samsung, OnePlus and Pixel. Feel free to give your feedback and tell me how can I improve my service... :)")
while x == 1:
    result = extract_brand(input("Bot : How can I help you?\nUser: "))
    
    if result in brandList1:
        print("Bot : Oh! You like",result,"! That's great... I have few",result,"phones that might be good for you")
        if result in brandList1:
            if_brand_samsung(input("Bot : Tell me about your price range\nUser: "))
            
    elif result in brandList2:
        print("Bot : Oh! You like",result,"! That's great... I have few",result,"phones that might be good for you")
        if result in brandList2:
            if_brand_apple(input("Bot : Tell me about your price range\n" "User: "))
            
    elif result in brandList3:
        print("Bot : Oh! You like",result,"! That's great... I have few",result,"phones that might be good for you")
        if result in brandList3:
            if_brand_oneplus(input("Bot : Tell me about your price range\n" "User: "))
            
    elif result in brandList4:
        print("Bot : Oh! You like",result,"! That's great... I have few",result,"phones that might be good for you")
        if result in brandList4:
            if_brand_pixel(input("Bot : Tell me about your price range\n" "User: "))
        
        
    elif result in spec_cam:
        print("Bot : Oh! You have many options availabe according to your preferrence. If you like apple devices go for the latest Iphone 14 series. When it comes to android, if you have a higher budget, you can look for the latest Samsung Galaxy S23 series. If your budget is low, you can check out the pixel phones... :)")
    else:
        print("Sorry, I only know about Samsung and Apple phones :(\n")


    print(give_feedback())




