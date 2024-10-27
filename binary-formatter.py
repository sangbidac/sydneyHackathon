import hashlib
import sys

def sha256_pad_two_u32(int1, int2):
    # Step 1: Convert each u32 integer to 4-byte big-endian format and concatenate
    message = int1.to_bytes(4, 'big') + int2.to_bytes(4, 'big')
    
    # Step 2: Append the '1' bit (0x80 in hex) as per padding requirements
    padded_message = message + b'\x80'
    
    # Step 3: Add zeroes to make the length 448 bits (56 bytes) for the 512-bit block
    padded_message += b'\x00' * (56 - len(padded_message))
    
    # Step 4: Append the original message length as a 64-bit big-endian integer (in bits)
    message_length = (len(message) * 8).to_bytes(8, 'big')
    padded_message += message_length
    
    return padded_message

def hash_two_ints(int_array):
    # Convert each integer to an 8-byte big-endian byte array and concatenate them
    byte_data = int_array[0].to_bytes(4, 'big') + int_array[1].to_bytes(4, 'big')
    
    # Generate the SHA-256 hash
    sha256_hash = hashlib.sha256(byte_data).hexdigest()
    return sha256_hash

if __name__ == '__main__':
    
    _, dob, passport_id = sys.argv

    dob_timestamp = int(dob)
    passport_id = int(passport_id)

    padded_value = sha256_pad_two_u32(dob_timestamp, passport_id)
    hex_padded_value = padded_value.hex()
    
    hash = hash_two_ints([dob_timestamp, passport_id])
    
    print(padded_value.hex())
    
    for i in range(0, len(hex_padded_value), 8):
        print(int(hex_padded_value[i:i+8], 16))
    
    # print('0x' + dob_hex + passport_hex + extra_bit + length)
    # print(int(dob_hex, 16), int(passport_hex, 16), int(extra_bit, 16), int(length, 16))
        
    print('0x' + hash)
    for i in range(0, len(hash), 8):
        print(int(hash[i:i+8], 16))