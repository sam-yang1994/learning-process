def starcenter(edges=list):

    if edges[0][0] ==edges[1][0] or edges[0][0] ==edges[1][1]:
        return edges[0][0]
    else:
        return edges[0][1]
