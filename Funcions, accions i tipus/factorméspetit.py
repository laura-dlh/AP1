# l'entrada és un nombre enter (n), on n>=2
# retorna el factor més petit si és compost
# retorna None si és primer
import yogi
n = yogi.read(int)
def factor_mes_petit(n: int) -> int | None:
    i = 2
    while i * i <= n:
        if n % i == 0:
            return i
        i = i + 1
    return None

print (factor_mes_petit(n))


