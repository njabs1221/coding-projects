def average(numbers):
    r=sum(numbers)/len(numbers)
    return r
    

names=[]
shoot_list=[]
pass_list=[]
pace_list=[]
dribble_list=[]
defend_list=[]
physical_list=[]
players = []  

num_of_players=int(input("Number of players:",))
while len(names)<num_of_players:
    name=input("Name:",)
    f=int(input("Finishing:",))
    sp=int(input("Shot Power:",))
    ls=int(input("Long Shots:",))
    v=int(input("Volleys:",))
    pl=int(input("Penalties:",))
    pos=int(input("Positioning:",))
    shoot_att=[f,ls,sp,v,pl,pos]
    
    shooting=average(shoot_att)
    shoot_list.append(shooting)
    names.append(name)
    
    player = {'name': name, 'shooting': shooting}
    
    continuity=input("Continue to passing? YES OR NO:",)
    cont_pass=continuity.lower()
    if cont_pass=="no":
        players.append(player)
        print("\n---Leaderboard Shooting attribute---")
        for p in players:
            print(f"{p['name']}: Shooting={p['shooting']}")
        

    elif cont_pass=="yes":
        
        v=int(input("Vision:",))
        lp=int(input("Long passing:",))
        sp=int(input("Short passing:",))
        c=int(input("Crossing:",))
        cur=int(input("Curve:",))
        fk=int(input("FK accuracy:",))
        pass_att=[v,lp,sp,c,cur,fk]
        
        passing=average(pass_att)
        pass_list.append(passing)
        
        player['passing'] = passing
        
        continuity_pace=input("Continue to pace? YES OR NO:",)
        cont_pace=continuity_pace.lower()
        if cont_pace=="no":
            players.append(player)
            print("\n---Leaderboard Shooting and Passing attributes---")
            for p in players:
                print(f"{p['name']}: Shooting={p['shooting']} Passing={p.get('passing', 'N/A')}")

        elif cont_pace=="yes":
            
            ac=int(input("Acceleration:",))
            ss=int(input("Sprint speed:",))
            pace_att=[ac,ss]
            
            pacing=average(pace_att)
            pace_list.append(pacing)
            
            player['pacing'] = pacing
            
            continuity_dribble=input("Continue to dribbling? YES OR NO:",)
            cont_dribble=continuity_dribble.lower()
            if cont_dribble=='no':
                players.append(player)
                print("\n---Leaderboard Shooting, Passing and Pace attributes---")
                for p in players:
                    print(f"{p['name']}: Shooting={p['shooting']} Passing={p.get('passing', 'N/A')} Pace={p.get('pacing', 'N/A')}")
            
            elif cont_dribble=='yes':
                
                ag=int(input("Agility:",))
                bal=int(input("Balance:",))
                rea=int(input("Reactions:",))
                bacon=int(input("Ball control:",))
                dri=int(input("Dribbling:",))
                comp=int(input("Composure:",))
                dribble_att=[ag,bal,rea,bacon,dri,comp]
                
                dribbling=average(dribble_att)
                dribble_list.append(dribbling)
                player['dribbling'] = dribbling
                
                continuity_defend=input("Continue to defending? YES OR NO:",)
                cont_defend=continuity_defend.lower()
                if cont_defend=="no":
                    players.append(player)
                    print("\n---Leaderboard Shooting, Passing Pace and Dribbling attributes---")
                    for p in players:
                        print(f"{p['name']}: Shooting={p['shooting']} Passing={p.get('passing', 'N/A')} Pace={p.get('pacing', 'N/A')} Dribbling={p.get('dribbling', 'N/A')}")
                
                elif cont_defend=="yes":
                    
                    cep=int(input("Interceptions:",))
                    defaware=int(input("Def awareness:",))
                    he=int(input("Heading accuracy:",))
                    stackle=int(input("Stand tackle:",))
                    slickle=int(input("Slide tackle:",))
                    defend_att=[cep,defaware,he,stackle,slickle]
                    
                    defending=average(defend_att)
                    defend_list.append(defending)       
                    player['defending'] = defending
                    
                    continuity_physical=input("Continue to physical? YES OR NO:",)
                    cont_physical=continuity_physical.lower()
                    if cont_physical=="no":
                        players.append(player)
                        print("\n---Leaderboard Shooting Passing Pace Dribbling and Defending attributes---")
                        for p in players:
                            print(f"{p['name']}: Shooting={p['shooting']} Passing={p.get('passing', 'N/A')} Pace={p.get('pacing', 'N/A')} Dribbling={p.get('dribbling', 'N/A')} Defending={p.get('defending', 'N/A')}")

                    elif cont_physical=="yes":
                        
                        jump=int(input("Jumping:",))
                        stam=int(input("Stamina:",))
                        stre=int(input("Strength:",))
                        agg=int(input("Aggression:",))
                        physical_att=[jump,stam,stre,agg]

                        physical=average(physical_att)
                        physical_list.append(physical)
                        player['physical'] = physical
                        overall_att=average(numbers=[shooting,passing,pacing,dribbling,defending,physical])
                        player['overall'] = overall_att
                        players.append(player)
                        
                        
                        if len(shoot_list)==num_of_players:
                            print("\n---Leaderboard Shooting Passing Pace Dribbling Defending and Physical attributes---")
                            for p in players:
                                print(f"{p['name']}: Shooting={p['shooting']} Passing={p.get('passing', 'N/A')} Pace={p.get('pacing', 'N/A')} Dribbling={p.get('dribbling', 'N/A')} Defending={p.get('defending', 'N/A')} Physical={p.get('physical', 'N/A')}")
                                
