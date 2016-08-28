adj = {}
def create_adj(self, pawn, adj):
    "creates an  adjacency list"
    
    _possible_move = []
    k = 0
    while k != self.getsize():
        _possible_move.append([i, (i[0], k)])
        _possible_move.append([i, (k, i[1])])
        k = k + 1

    for i in self.notpossible(_possible_move):
        if i in _possible_move:
            _possible_move.remove(i)
    # all possible moves
    
    dangerzone = []
    enemies = self.getenemies()

    for i in _possible_move:
        if (i[1][0], i[1][1] + 1) in enemies:
            dangerzone.append(i)
        elif (i[1][0], i[1][1] - 1) in enemies:
            dangerzone.append(i)
        elif (i[1][0] + 1, i[1][1]) in enemies:
            dangerzone.append(i)
        elif (i[1][0] - 1, i[1][1]) in enemies:
            dangerzone.append(i)
    # looks if pawn would get into DANGERZONE
            
    helplist = _possible_move[:]
    _possible_move = []

    for i in helplist:
        if i not in dangerzone:
            _possible_move.append(i)

              
    for i in _possible_move:
            if adj.get(i[0]):
                    adj[i[0]].add(i[1])
            else:
                adj[i[0]] = {i[1]}
    # writes the adj.list

    for i in _possible_move:
        if i not in adj:
            adj = create_adj(pawn, adj)
            
    return adj    
    
