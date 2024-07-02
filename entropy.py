'''
przepływność:
R=S/N
R- przepływność
S- rozmiar pliku wyjściowego w bitach
N- liczba pikseli w obrazie
'''
'''
średnia długość bitowa kodu wyjściowego
L=S/N
S i N to samo co wcześniej 
'''
'''
Rate=rozmiar danych przed skompresowaniem/rozmiar danych po skompresowaniu
'''
import math
from collections import Counter
import communication


def calculate_entropy_from_file(filename):
    # Odczytanie wartości pikseli z pliku tekstowego
    with open(filename, 'r') as f:
        pixel_values = [int(line.strip()) for line in f]

    # Obliczenie rozkładu wartości pikseli
    total_pixels = len(pixel_values)
    pixel_counts = Counter(pixel_values)
    
    # Obliczenie entropii
    entropy = 0
    for count in pixel_counts.values():
        probability = count / total_pixels
        entropy -= probability * math.log2(probability)
    
    return entropy

def bit_number(n):
    return math.ceil(math.log2(n + 1))

pixels_in_pic = 262144
decode_stream = communication.read_data_from_txt('stream') #strumień
final_state = communication.read_data_from_txt('current_state')[0] #stan

filename = 'pixel_values.txt'
entropy = calculate_entropy_from_file(filename)
print(f'Entropia wartości pikseli: {entropy} bitów/piksel')


bitrate=(len(decode_stream)+bit_number(final_state))/pixels_in_pic
print(f'przepływność przed kompresją:{8} bitów/piksel')
print(f'przepływność po kompresji: {bitrate} bitów/piksel')



compression_rate=(pixels_in_pic*8)/(len(decode_stream)+bit_number(final_state))
print(f'stopien kompresji: {compression_rate}')

f_values=communication.read_data_from_txt('f_value')
total_bits=0
for f_value in f_values:
    total_bits+=bit_number(f_value)

CDF_values=communication.read_data_from_txt('CDF_value')
for CDF_value in CDF_values:
    total_bits+=bit_number(CDF_value)

total_bits=total_bits+len(decode_stream)+bit_number(final_state)

newer_bitrate=total_bits/pixels_in_pic
print(f'przepływność TOTAL po kompresji: {newer_bitrate} bitów/piksel')
