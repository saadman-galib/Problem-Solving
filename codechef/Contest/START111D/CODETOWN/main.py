vowel_Array = ['A', 'E', 'I', 'O', 'U']

for _ in range(int(input())):
    s = input()
    can_reach = True

    check_vowels = [
    {
        "id": 1, 
        "got_it": False
    },
    {
        "id": 3,
        "got_it": False
    },
    {
        "id": 5,
        "got_it": False
    }]

    for i in range(len(s)):
        for check_vowel in check_vowels:
            if check_vowel["id"] == i and s[i] in vowel_Array:
                check_vowel["got_it"] = True
    
    for check_vowel in check_vowels:
        if(check_vowel["got_it"] == False):
            can_reach = False
                
    print("YES" if can_reach else "NO")

    vowel_Array = ['A', 'E', 'I', 'O', 'U']

# for _ in range(int(input())):
#     s = input()
#     can_reach = True

#     s_list = list(s)
#     s_list.reverse()
#     s_reversed = "".join(s_list)

#     for i in range(0, len(s), 2):
#         if s[i] in vowel_Array and s[i+1] not in vowel_Array:
#             can_reach = False
#             break

#     print("YES" if can_reach else "NO")