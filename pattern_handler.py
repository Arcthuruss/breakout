from classes import Brique

 #  THE read_pattern, THE read_pattern IS REAL
def read_pattern(number,difficulty) :
    with open(f"patterns/{difficulty}/pattern_{number}.txt",'r', encoding='utf-8') as f :
        data = f.read()
    data = data.split('\n')[1:]
    delimiter = data.index('')
    symbols_list, pattern = [ligne.split(' - ') for ligne in data[:delimiter]], data[delimiter+1:]
    symbols_list = dict([(i[0],eval(i[1])) for i in symbols_list])

    level = [[Brique(j*symbols_list[symbol][0],i*symbols_list[symbol][1]+54,symbols_list[symbol][0],symbols_list[symbol][1],symbols_list[symbol][2]) for j,symbol in enumerate(ligne)] for i,ligne in enumerate(pattern)]

    return level
