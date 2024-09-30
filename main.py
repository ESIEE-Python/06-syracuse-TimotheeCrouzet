# imports
from plotly.graph_objects import Scatter, Figure

### NE PAS MODIFIER ###
def syr_plot(lsyr):
    title = "Syracuse" + " (n = " + str(lsyr[0]) + " )"
    fig = Figure({  'layout':   { 'title': {'text': title},
                                'xaxis': {'title': {'text':"x"}},
                                'yaxis': {'title': {'text':"y"}},
                                }
                }
    )

    x = [ i for i in range(len(lsyr)) ]
    t = Scatter(x=x, y=lsyr, mode="lines+markers", marker_color = "blue")
    fig.add_trace(t)
    fig.show()
    # fig.write_html('fig.html', include_plotlyjs='cdn')
    return None



def syracuse_l(n):
    """retourne la suite de Syracuse de source n

    Args:
        n (int): la source de la suite

    Returns:
        list: la suite de Syracuse de source n
    """
    L = [n]  # Commence par n
    while n != 1:  # Continue jusqu'à ce que n atteigne 1
        if n % 2 == 0:  # n est pair
            n = n // 2
        else:  # n est impair
            n = 3 * n + 1
        L.append(n)  # Ajouter la nouvelle valeur à la liste
    return L
                 

def temps_de_vol(L):
    """Retourne le temps de vol d'une suite de Syracuse

    Args:
        l (list): la suite de Syracuse

    Returns:
        int: le temps de vol
    """
    if not L:  # Vérifie si la liste est vide
        return 0
    i = 0
    while L[i] != 1 and i < len(L):
        i += 1
    return i+1
            


def temps_de_vol_en_altitude(L):
    """Retourne le temps de vol en altitude d'une suite de Syracuse

    Args:
        l (list): la suite de Syracuse

    Returns:
        int: le temps de vol en altitude
    """
    if not L:  # Vérifie si la liste est vide
        return 0
    i = 0
    while  i < len(L)-1 and L[i+1] > L[0]:
        i += 1
    return i



def altitude_maximale(L):
    """retourne l'altitude maximale d'une suite de Syracuse

    Args:
        l (list): la suite de Syracuse

    Returns:
        int: l'altitude maximale
    """
    if not L:  # Vérifie si la liste est vide
        return None
    return max(L)

print(syracuse_l(6))
print(altitude_maximale(syracuse_l(6)))

def main():

    # vos appels à la fonction secondaire ici
    lsyr = syracuse_l(15)
    syr_plot(lsyr)
    print(temps_de_vol(lsyr))
    print(temps_de_vol_en_altitude(lsyr))
    print(altitude_maximale(lsyr))


if __name__ == "__main__":
    main()