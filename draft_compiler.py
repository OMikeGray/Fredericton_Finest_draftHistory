import csv

draft_history = []
header = ['Year', 'Round', 'Pick', 'Player', 'Position', 'Team', 'Owner']
draft_history.append(header)
years = [2021,2020,2019,2018,2017,2016,2015,2014,2013,2012]
adv = { 'Arizona Cardinals':'ARZ',
        'Atlanta Falcons':'ATL',
        'Baltimore Ravens':'BLT',
        'Buffalo Bills':'BUF',
        'Carolina Panthers':'CAR',
        'Chicago Bears':'CHI',
        'Cincinnati Bengals':'CIN',
        'Cleveland Browns':'CLV',
        'Dallas Cowboys':'DAL',
        'Denver Broncos':'DEN',
        'Detroit Lions':'DET',
        'Green Bay Packers':'GB',
        'Houston Texans':'HST',
        'Indianapolis Colts':'IND',
        'Jacksonville Jaguars':'JAX',
        'Kansas City Chiefs':'KC',
        'Las Vegas Raiders':'LV',
        'Los Angeles Chargers':'LAC',
        'Los Angeles Rams':'LAR',
        'Miami Dolphins':'MIA',
        'Minnesota Vikings':'MIN',
        'New England Patriots':'NE',
        'New Orleans Saints':'NO',
        'New York Giants':'NYG',
        'New York Jets':'NYJ',
        'Philadelphia Eagles':'PHI',
        'Pittsburgh Steelers':'PIT',
        'San Francisco 49ers':'SF',
        'Seattle Seahawks':'SEA',
        'Tampa Bay Buccaneers':'TB',
        'Tennessee Titans':'TEN',
        'Washington Football Team':'WAS'
    }

## Draft Compiler
for year in years:
    print(year)
    with open(str(year)+'_draft.txt','r') as file:
        reader = list(csv.reader(file))
        i = 0
        for row in reader:
            if i == 0:
                pick = row[0]
                pick = pick.replace('.','')
                i = i + 1
            elif i == 1:
                player = row[0]
                i = i + 1
            elif i == 2:
                p_t = row[0].split('TO',-1)[0]
                try:
                    pos = p_t.split(' - ',-1)[0]
                    team = p_t.split(' - ',-1)[1]
                except:
                    pos = p_t
                    try:
                        team = adv[player]
                    except:
                        team = ''
                i = i + 1
            elif i == 3:
                i = i + 1
            elif i == 4:
                owner = row[0]
                line = [year, '', pick, player, pos, team, owner]
                draft_history.append(line)
                i = 0

with open('draft_history.csv', 'w', newline='') as csvfile:
    writer = csv.writer(csvfile)
    for row in draft_history:
        writer.writerow(row)

