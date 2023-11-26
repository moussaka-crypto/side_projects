import random
import matplotlib.pyplot as plt

def flip_bit_at(a, index):
    return a[:index] + str(int(a[index]) ^ 1) + a[index+1:]

def hamming_encoder(data):
    if len(data) % 4 != 0:
        data = data + '0' * (4 - (len(data) % 4))
    
    encoded_data = ""
    generator = [[1,0,0,0],[0,1,0,0],[0,0,1,0],[0,0,0,1],[1,1,1,0],[1,1,0,1],[1,0,1,1]]
    res = 0
    
    for i in range(0, len(data),4):
        block = data[i:i+4]
        for y in range(0,len(generator)):
            for x in range(0,len(generator[y])):
                res += (int(block[x]) & generator[y][x])
            encoded_data += str(res%2)
            res = 0
                
    return encoded_data

def hamming_decoder(encoded_data):
    decoded_data = ""
    
    syndrome = ""
    paritycheck=[[1,1,1,0,1,0,0],[1,1,0,1,0,1,0],[1,0,1,1,0,0,1]]
    paritycheckT=["111","110","101","011","100","010","001"]
    
    res = 0
    
    for i in range(0, len(encoded_data), 7):
        block = encoded_data[i:i+7] 
        for y in range(0,len(paritycheck)):
            for x in range(0,len(paritycheck[y])):
                res += (int(block[x]) & paritycheck[y][x])
            syndrome += str(res%2)
            res = 0

        for y in range(0, len(paritycheckT)):
            if syndrome != "000":
                # Korrigieren des fehlerhaften Bits
                error_bit = paritycheckT.index(syndrome)
                block = flip_bit_at(block, error_bit)            
        decoded_data += block[0] + block[1] + block[2] + block[3]
        syndrome = ""    
    
    return decoded_data    


def channel_bsc(p):
    error_word = ''

    for _ in range(100):
        if random.random() < p:
            error_word += '1' 
        else:
            error_word += '0' 
    
    return error_word

def main():
    Ldata = 100
    N_iteration = 100
    p_bsc = [x*0.1 for x in range(8, 1, -1)]
    p_bsc += [x*0.01 for x in range(18, 0, -2)]
    
    bit_error_rates = []
    channel_error_rates = []
    
    for p in p_bsc:
        total_bit_errors = 0
        total_channel_errors = 0
        
        for i in range(N_iteration):
            data = ""
            
            for _ in range(0, Ldata):
                data += str(random.randint(0, 1))
                
            encoded_data = hamming_encoder(data)
            """
            BSC CHANNEL
            """
            received_data = encoded_data
            
            for index,bit in enumerate(channel_bsc(p)):
                if bit == '1':
                    received_data = flip_bit_at(received_data, index)
            """"""
            decoded_data = hamming_decoder(received_data)

            bit_errors = sum(c != d for c, d in zip(data, decoded_data))
            channel_errors = sum(c != r for c, r in zip(encoded_data, received_data))
            
            total_bit_errors += bit_errors
            total_channel_errors += channel_errors

        bit_error_rate = total_bit_errors / (N_iteration * Ldata)
        channel_error_rate = total_channel_errors / (N_iteration * len(encoded_data))
        
        bit_error_rates.append(bit_error_rate)
        channel_error_rates.append(channel_error_rate)

    plt.semilogy(p_bsc, bit_error_rates, 'o-', label='Bit error rate')
    plt.semilogy(p_bsc, channel_error_rates, 'o-', label='Channel error rate')

    plt.xlabel('Probability of transmission error p')
    plt.ylabel('Error rate')
    plt.title('Bit and channel error rate')
    plt.grid(True)

    plt.legend()

    plt.show()
    
    
if __name__ == "__main__":
    main()
    