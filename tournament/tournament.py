def generate_table(tournament_results):
    if tournament_results == '':
        return {}
    parsed = []
    teams_played = set()
    table = dict()

    #parse results and add to teams played
    for raw_result in tournament_results.split('\n'):
        parsed.append(raw_result.split(';'))
        teams_played.update(parsed[-1][0:2])

    #initialize table
    for team in teams_played:
        table[team] = {'MP': 0, 'W': 0, 'D':0, 'L':0, 'P':0}

    #indicate wins, losses, draws in table
    for team1,team2,result in parsed:
        if result == 'win':
            table[team1]['W'] += 1
            table[team2]['L'] += 1
        elif result == 'loss':
            table[team2]['W'] += 1
            table[team1]['L'] += 1
        else: #result == 'draw':
            table[team2]['D'] += 1
            table[team1]['D'] += 1

    #finalize table, add games played and points
    for team, entry in table.items():
        table[team]['MP']  = entry['W'] + entry['D'] + entry['L']
        table[team]['P'] = entry['W'] * 3  +  entry['D']

    return table


def stringify(table):
    disp_str = 'Team                           | MP |  W |  D |  L |  P';
    for team,entry in table:
        disp_str += "\n{name:31}|  {MP} |  {W} |  {D} |  {L} |  {P}".format(
            name = team,
            MP = entry['MP'],
            W = entry['W'],
            D = entry['D'],
            L = entry['L'],
            P = entry['P'],
        )
    return disp_str


def tally(tournament_results):
    table = generate_table(tournament_results)
    #sort alphabetically then sort by points
    sorted_table_by_name = sorted(table.items(), key = lambda kv: kv[0])
    sorted_table_by_points = sorted(sorted_table_by_name, key = lambda tup: tup[1]['P'], reverse = True)
    return stringify(sorted_table_by_points)

if __name__ == '__main__':
    disp_str = tally(result)
    print(disp_str)



#end
