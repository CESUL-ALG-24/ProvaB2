def obter_acrescimos(tempo_jogo: int) -> tuple[int, int]:
    acrescimos_total = tempo_jogo - 90
    acrescimos_t1 = acrescimos_total // 3
    acrescimos_t2 = acrescimos_t1 * 2

    return acrescimos_t1, acrescimos_t2
