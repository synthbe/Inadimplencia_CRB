def busca_binaria(key, array, st, end):
    if st > end:
        return -1

    half = st + (end - st) // 2
        
    if key > array[half]:
        return busca_binaria(key, array, half, end)
    elif key < array[half]:
        return busca_binaria(key, array, st, half)
    elif key == array[half]:
        return half


    
        
        