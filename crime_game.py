print('''
GAME START
      
You're a detective investigating a crime. Two days ago a body of a woman was found in a creek. 
That's what you know:
- Her name was Laura Clook
- The woman was around 20 y/o
- She probably drowned
- She was in water for about 2-3 days
Every evidence is hard to get because of the water.
      
There are 3 suspects that you need to question:
1. Patric Stefano - her ex boyfriend, they had a problem before breaking up
2. Katherine Clook - her sister, that she visited some days before 
3. Alexy Krocs - her coworker, who had strange relationship with her
''')

suspects = [
    {
        "name": "Patric Stefano",
        "question": {
            1: "You had a close relationship with the victim, didn't you?",
            2: "When was the last time you talked to Laura?",
            3: "Did you have a fight with Laura before she disappeared?",
            4: "(Go back)"
        },
        "response": {
            1: "-- Sure I did, she was my girlfriend. We were dating for like a year and a half.",
            2: "-- A couple of days ago. She actually was leaving me for a few days before. It's her temper.",
            3: "-- Yes we did."
        },
        "added_question": {
            1: "What was the fight about?",
            2: "Did you threaten her or mention someone else during the argument?",
            3: "Do you know where Laura went after the fight?",
            4: "(Go back)"
        },
        "added_response": {
            1: "-- I wanted to start a family. She said she wasn't ready. I think she just doesn't appreciate me, thats all. She never thinks about my needs.",
            2: "-- I was mad so I told her I found someone who actually wanted a baby. That we were dating for 2 month and that girl is what I actually need.",
            3: "-- I don't know. Don't care either."
        },
        "is_questioned": False
    },

    {
        "name": "Katherine Clook",
        "question": {
            1: "What are your relationship with Laura?",
            2: "Are you her older or younger sister?",
            3: "When and where did you and Laura last see each other?",
            4: "(Go back)"
        },
        "response": {
            1: "-- We hadn't met since our childhood. We were separated when I was 13. We had a tough relationship before, but now we're doing better.",
            2: "-- I'm older. When we were children I used to be jealous of Laura, cause I wasn't as successful at school and in relationships as her. But it's good now.",
            3: "-- In a cafe 3 days ago, we met because she had a problem with her bf and wanted to talk to me."
        },
        "added_question": {
            1: "What did she say to you?",
            2: "Did something happen before she left?",
            3: "(Go back)"
        },
        "added_response": {
            1: "-- She said that her boyfriend was pushing her to start a family. Well, that was kinda abusing to me, so i told her that they should immediately break up. She responded that they alredy did, she looked like she was loosing herself.",
            2: "-- Yeah. Laura already made an order when she got a call from someone. She was talking for 2 mins and then told me she had to leave. I asked her who was that and where is she going. Laura only said that it's a guy she's dating now and left. I let her go. That's all I know."
        },
        "is_questioned": False
    },

    {
        "name": "Alexy Krocs",
        "question": {
            1: "What are your relationship with Laura?",
            2: "How long have you known Laura?",
            3: "When and where did you last see Laura?",
            4: "(Go back)"
        },
        "response": {
            1: "-- Well, it's complicated. We met a couple of times after worktime, but that's all.",
            2: "-- For 3 month. She's my work colleague, as you know.",
            3: "-- Umm, at the bar, few days ago. It was already late nigth, but I was so drunk I barely remember anything."
        },
        "added_question": {
            1: "What where you and Laura doing at the bar?",
            2: "Were you the last person to talk to Laura?",
            3: "Do you know anything about Laura's boyfriend?",
            4: "(Go back)"
        },
        "added_response": {
            1: "-- Well, I invited her there to chill. She was with me for a couple of hours, but then she left.",
            2: "-- Probably, yeah. I don't know where she went, but if something happened to her, this migth have been the strange guy that always sneaks around the bar. He has a long black beard and the same hair. I hope she's ok anyway.",
            3: "-- Almost nothing. Just heard that they've been having a hard time living together. So I just wanted to fix her mood."
        },
        "is_questioned": False
    },
]


detective_call = """
** You recieve a call from another detective **
-- Hey there. There are some new information about the victim.
   The medical examiner reported that she had several blunt force trauma wounds to her head. She also was choked.
   Near that creek we found an abandoned white pickup. It's slightly damaged, near it we found a burnt gun and peaces of rope.
   We sent those to examine, but results won't be here in the closest time.
   Do what you have to with that information.
You: Alexy Krocs told me about a strange guy near the bar he last saw Laura. He had long black beard and hair. Might wanna check him too.
-- Ok, let me check who it could be... Well, his name is Alejandro Nuñes and he's got some crime record on him. I'll send him to you.
** Hangs up **
"""

win = """
Alexy Krocs was accused of killing Laura. The other detectives questioned him more, so he told them the real story. It turns aout that after the bar, he and Laura drived back to her home. He asked her to go to his home, but Laura started screaming and grabbed his gun. So Alexy got mad and scared, fighted Laura and beated her with a gun. After that, they crashed, but Laura was still alive. So he grabbed a rope from the trunk and chocked her. He threw her body to the creak nearby, hoping she wouldn't be found.
During the trial he confessed to the crime. He was sentenced to life.

You were chilling at your home. This case was done, you were glad you could help Laura's family find out what happened to her. Your career is growing now, so you're waiting for the next case.
"""

lost_kath = """
Katherine Clook was accused of killing Laura. The other detectives questioned her more, but she kept defending herself. He was surprised that someone could have thought on her.
During the trial she didn't confess to the crime. They claimed she had her motive, because she was the one Patric was cheating Laura with. She cried, while she was being sentenced to life.

You were chilling at your home. This case wasn't done, so you were still worried. You felt bad for putting Laura's sister in prison. Now you're not sure about your decision. While you were thinking who could be the real killer, someone knocked on your door. You opened. You were shot right there, in the face...

What was that?
"""

lost_patric = """
Patric Stefano was accused of killing Laura. The other detectives questioned him more, but he kept defending himself.
During the trial he didn't confess to the crime. The evidence provided wasn't enough, so he was cleared of all charges and released.

You were chilling at your home. This case wasn't done, so you were still worried. While you were thinking who could be the real killer, someone knocked on your door. You opened. You were shot right there, in the face...

What was that?
"""

lost_alej = """
Alejandro Nuñes was accused of killing Laura. The other detectives questioned him more, but he kept defending himself. But as detectives kept pushing and threatening him, he agreed to confess the crime.
During the trial he confessed to the crime. It was quite obvious that he was the one who killed Laura, right?

You were chilling at your home. This case was done, but something in you was still shaking. While you were thinking if he was the real killer or not, someone knocked on your door. You opened. You were shot right there, in the face...

What was that?
"""

def reply(suspect, trigger_question = 3, back_option = 4, added_back_option = 4):

    while True:
        for key, value in suspect["question"].items(): # items for printing key and value
            print(f"{key}. {value}")
        
        try: # for errors with value types
            question = int(input("Choose a question (number): ")) # question choosed
            print("---------------------------------")
        except ValueError:
            print("Write a number.")
            continue

        if question == back_option:
            break
        elif question == trigger_question:
            print(suspect["response"][question])
            print("Hmm...")

            while True:
                
                for key, value in suspect["added_question"].items():
                    print(f"{key}. {value}") # prints questions

                try:
                    question2 = int(input("Choose a question (number): "))
                    print("---------------------------------")
                except ValueError:
                    print("Write a number.")
                    continue

                if question2 == added_back_option:
                    break
                elif question2 in suspect["added_response"]: # if second question is in array of responses
                    print(suspect["added_response"][question2])
                    suspect["is_questioned"] = True # suspect is questioned only when added responces were printed
                else:
                    print('Write a proper number.')
                
        elif question in suspect["response"]:
            print(suspect["response"][question])
        else:
            print('Write a proper number.')
            
            
def print_suspects():
    num = 1
    for i in range(len(suspects)):
        print(f"{num}. {suspects[i]["name"]}")
        num += 1


def print_end(sus):
    print(sus)
    print("THANKS FOR PLAYING")


detective_call_shown = False

while True:
    
    print_suspects()
    
    try:
        choice = int(input("Who do you want to question? (number): "))
        print("---------------------------------")
    except ValueError:
        print("Write a number.")
        continue

    if choice == 2:
        print(suspects[1]["name"])
        reply(suspects[1], added_back_option=3)
    elif 1 <= choice <= len(suspects): # if choosed suspect is a natural number and less than number of suspects
        print(suspects[choice-1]["name"])
        reply(suspects[choice-1])
    else:
        print('Write a proper number.')

    if all(s["is_questioned"] for s in suspects) and not detective_call_shown: # if everyone was chosen at least once and detective didn't call yet
        print(detective_call)
        suspects = [
        {
            "name": "Patric Stefano",
            "question": {
                1: "Did you hit Laura during an argument?",
                2: "Do you own a gun?",
                3: "Do you drive a car?",
                4: "(Go back)"
            },
            "response": {
                1: "-- No, I think she was actually the one that hit me. I told you, she's crazy.",
                2: "-- I don't, but my brother does. He keeps it at home and never carries it with him.",
                3: "-- Yeah, it was parked near my house when you came, so I bet you saw it."
            },
            "added_question": {
                1: "Was it damaged?",
                2: "What color is the car?",
                3: "What is the mark of the car?",
                4: "(Go back)"
            },
            "added_response": {
                1: "-- Yes, Laura crashed it one time, so it was damaged from the front.",
                2: "-- A white car, pretty common.",
                3: "-- BMW."
            },
            "is_questioned": False
        },

        {
            "name": "Katherine Clook",
            "question": {
                1: "Do you drive a car?",
                2: "Do you own a gun?",
                3: "Did you have relationship with Laura's boyfriend?",
                4: "(Go back)"
            },
            "response": {
                1: "-- No, but I used to. Abou 10 years ago, I had to sell it then.",
                2: "-- No, never did.",
                3: "-- Hm... Ok, i'm gonna be honest with you. We're chatting since i got back in this town. We're not a couple or anything, I couldn't do that to my sister."
            },
            "added_question": {
                1: "Have you met?",
                2: "Are you that woman who is a new Patric's love interest?",
                3: "(Go back)"
            },
            "added_response": {
                1: "-- ... No, never.",
                2: "-- What? No! I didn't even know about him cheating before Laura told me that herself."
            },
            "is_questioned": False
        },

        {
            "name": "Alexy Krocs",
            "question": {
                1: "Did Laura tell you anything before she left the bar?",
                2: "Do you own a gun?",
                3: "Do you drive a car?",
                4: "(Go back)"
            },
            "response": {
                1: "-- Errm... No, she didn't.",
                2: "-- Yeah, but I never used it. I keep it in my car.",
                3: "-- Emm, yeah."
            },
            "added_question": {
                1: "Was it damaged?",
                2: "What color is the car?",
                3: "What is the mark of the car?",
                4: "(Go back)"
            },
            "added_response": {
                1: "-- ... A bit, I drove into a tree recently. There was an animal on the road.",
                2: "-- White.",
                3: "-- Ford. My dad gived it to me for my birthday."
            },
            "is_questioned": False
        },
        {
            "name": "Alejandro Nuñes",
            "question": {
                1: "How namy times were you arrested?", 
                2: "Someone said you harass women near the bar. True?",
                3: "Were you near the bar the night Laura disappeared?",
                4: "(Go back)"
            },
            "response": {
                1: "-- I don't count. I think around 5-6 times.",
                2: "-- No, never. I'm always arrested for drinking and drug dealing. You know, I don't even deal drugs, you cops are happy to jail guys that just knows how to relax.",
                3: "-- Who's that girl? I was at the bar then, but I can't tell you more."
            },
            "added_question": {
                1: "Did you see Laura before?",
                2: "Do you own a gun?",
                3: "Do you drive a car?",
                4: "(Go back)"
            },
            "added_response": {
                1: "-- I don't get who are you talking about.",
                2: "-- No, never did.",
                3: "-- No, I go on foot usually."
            },
            "is_questioned": False
        }
        ]
        # everyone is set again to not questioned, so the next if will be executed, when everyone is questioned again
        detective_call_shown = True

    elif all(s["is_questioned"] for s in suspects):
        print("It's time to accuse the criminal.")
        print_suspects()

        try:
            criminal = int(input("The one who killed Laura is... "))
            print("---------------------------------")
        except ValueError:
            print("Write a number.")
            continue

        if criminal == 3:
            print_end(win)
            break
        elif criminal == 1:
            print_end(lost_patric)
            break
        elif criminal == 2:
            print_end(lost_kath)
            break
        elif criminal == 4:
            print_end(lost_alej)
            break
        else:
            print("Write a proper number")