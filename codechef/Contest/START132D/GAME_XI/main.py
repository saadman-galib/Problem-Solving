t = int(input())

for _ in range(t):
    n, m = map(int, input().split())
    n_array = list(map(int, input().split()))
    m_array = list(map(int, input().split()))

    n_array.sort(reverse=True)
    m_array.sort(reverse=True)

    new_team = 0
    team_member_count = 0


    if(n < 4 or m < 4):
        print(-1)
    elif((n + m) < 11):
        print(-1)
    else:
        for i in range(4):
            new_team += n_array[0]
            
            n_array.pop(0)
            team_member_count += 1
            new_team += m_array[0]
           
            m_array.pop(0)
            team_member_count += 1

        while(team_member_count < 11):
            if len(n_array) != 0 and len(m_array) != 0:
                if(n_array[0] > m_array[0]):
                    new_team += n_array[0]
                    team_member_count += 1
                    n_array.pop(0)
                else:
                    new_team += m_array[0]
                    team_member_count += 1
                    m_array.pop(0)

            elif len(n_array) == 0 and len(m_array) != 0:
                new_team += m_array[0]
                m_array.pop(0)
                team_member_count += 1
            elif len(n_array) != 0 and len(m_array) == 0:
                new_team += n_array[0]
                n_array.pop(0)
                team_member_count += 1
            else:
                break               

        print(new_team)
            