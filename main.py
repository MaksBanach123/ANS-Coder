from ans_coder import AnsCoder
from ans_decoder import AnsDecoder
import communication
from time import time

if __name__ == "__main__":
    # Kodowanie
    print("__ENCODE__")
    coder = AnsCoder("pixel_values.txt")
    values = coder.open()
    prob = coder.probability(values)
    f, CDF = coder.determine_f_and_CDF(prob)
    communication.write_data_to_txt('f_value', f)
    communication.write_data_to_txt('CDF_value', CDF)
    communication.write_data_to_txt('image_length', len(values))

    print(f'Initial state: {coder.initial_state}')
    stream = ''
    start = time()
    print("Coding has started")
    for word in values:
        coder.current_state, stream = coder.encode(word, f, CDF, stream)

    communication.write_data_to_txt('current_state', coder.current_state)
    communication.write_data_to_txt('stream', stream)
    end = time()
    print(f"Successfully encoded in: {end - start} [s]")
    print(f"End state: {coder.current_state}")
    print(f"Stream length: {len(list(stream))}")
    coder.reset_state()

    print(40*"_")

    # Dekodowanie
    # Zmienne do dekodowania (komunikacja przy pomocy plików)
    print('__DECODE__')
    decode_x = communication.read_data_from_txt('current_state')[0]
    print(decode_x)
    decode_stream = communication.read_data_from_txt('stream')
    decode_f = communication.read_data_from_txt('f_value')
    decode_CDF = communication.read_data_from_txt('CDF_value')
    image_length = communication.read_data_from_txt('image_length')[0]
    decode_stream = list(decode_stream)

    decoder = AnsDecoder()
    decodedWords = []  # lista słów zdekodowanych
    start_2 = time()
    print("Decoding has started")
    while (len(decodedWords)!=image_length):  #dekoduj dopóki długości tablic się nie zrównają (słowa powinny być te same), do zmiany warunek
        decode_x, word, decode_stream = decoder.decode(decode_x,
                                                    decode_f,
                                                    decode_CDF,
                                                    decode_stream)
        decodedWords.append(word)

    #decodedWords = [value for value in decodedS]  #zmiana na wartości bitowe
    decodedWords.reverse()
    communication.write_data_to_txt('image_after_decoding', decodedWords)
    end_2 = time()
    assert values==decodedWords
    print(f"Successfully decoded in: {end_2 - start_2} [s]")

