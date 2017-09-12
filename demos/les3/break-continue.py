# break and continue statements
# Demo purposes, may noit be well formatted for display reasons
#
# Robert Schrijvers



results = [('Feyenoord',4 ,4,0,0,12,3),\
('Vitesse',4 ,3,0,1,11,4),\
('Ajax',4 ,3,0,1,9,3),\
('FC Utrecht',4 ,3,0,1,8,2),\
('PSV',4 ,3,0,1,9,5),\
('AZ',4 ,3,0,1,8,5),\
('SC Heerenveen',4 ,2,2,0,8,5),\
('VVV-Venlo',4 ,2,1,1,6,4),\
('PEC Zwolle',4 ,2,1,1,7,6),\
('FC Groningen',4 ,1,2,1,7,8),\
('Heracles Almelo',4 ,1,2,1,7,8),\
('Sparta',4 ,1,2,1,4,6),\
('Excelsior',4 ,1,1,2,4,7),\
('ADO Den Haag',4 ,1,0,3,3,8),\
('NAC Breda',4 ,0,1,3,5,12),\
('FC Twente',4 ,0,0,4,2,7),\
('Roda JC',4 ,0,0,4,3,11),\
('Willem II',4 ,0,0,4,2,11)]



print('\n --- Break at 2 matches drawn ----')
for team in results:
    if team[3] == 2 :
        print('{0:20} 2 maal gelijk'.format(team[0]))
        break
    print('{0:20} {1:^10} {2:^10} {3:^10} {4:^10} {5:^10} {6:^10} '.format(team[0],team[1],team[2],team[3],team[4],team[5],team[6]))





print('\n --- Continue at 2 matches drawn ----')
for team in results:
    if team[3] == 2 :
        print('{0:20} 2 maal gelijk'.format(team[0]))
        continue
    print('{0:20} {1:^10} {2:^10} {3:^10} {4:^10} {5:^10} {6:^10} '.format(team[0],team[1],team[2],team[3],team[4],team[5],team[6]))





print('\n --- Show only teams without letter r in name ----')
for team in results:
    if 'r' in team[0]:
        continue
    print('{0:20} {1:^10} {2:^10} {3:^10} {4:^10} {5:^10} {6:^10} '.format(team[0],team[1],team[2],team[3],team[4],team[5],team[6]))



