def climbingLeaderboard(ranked, player):
    ranked=list(set(ranked))
    ranked.sort(reverse=True)
    a=[]
    l = len(ranked)
    for s in player:
        while (l > 0) and (s >= ranked[l - 1]):
            l -= 1
        a.append(l + 1)
    return a

ranked=[295, 294 ,291, 287 ,287, 285 ,285 ,284 ,283, 279, 277, 274, 274 ,271, 270, 268 ,268 ,268 ,264, 260 ,259 ,258 ,257, 255 ,252 ,250 ,244 ,241, 240, 237, 236 ,236 ,231 ,227 ,227 ,227 ,226, 225, 224, 223 ,216 ,212 ,200 ,197 ,196 ,194, 193 ,189 ,188, 187 ,183, 182 ,178 ,177, 173 ,171 ,169 ,165, 143 ,140 ,137 ,135 ,133, 130, 130, 130, 128 ,127 ,122 ,120 ,116 ,114,113, 109 ,106 ,103,99 ,92, 85 ,81 ,69, 68 ,63 ,63 ,63 ,61, 57, 51, 47 ,46 ,38 ,30 ,28 ,25 ,22 ,15 ,14 ,12 ,6 ,4]
player=[5, 5, 6, 14, 19, 20, 23, 25 ,29, 29, 30 ,30 ,32, 37 ,38 ,38, 38 ,41 ,41, 44, 45, 45,47 ,59 ,59, 62, 63 ,65, 67, 69, 70 ,72, 72 ,76, 79 ,82 ,83 ,90 ,91 ,92, 93, 98, 98, 100 ,100, 102 ,103, 105, 106, 107 ,109 ,112, 115 ,118, 118, 121, 122, 122, 123 ,125, 125 ,125, 127, 128, 131, 131 ,133, 134, 139 ,140, 141, 143 ,144 ,144 ,144 ,144,147 ,150, 152, 155, 156, 160 ,164, 164, 165, 165, 166 ,168 ,169, 170, 171 ,172 ,173 ,174 ,174, 180, 184 ,187 ,187 ,188 ,194 ,197 ,197 ,197 ,198]
print("ok:",climbingLeaderboard(ranked,player))