import common

HEX_TO_BINARY = {
    "0": "0000",
    "1": "0001",
    "2": "0010",
    "3": "0011",
    "4": "0100",
    "5": "0101",
    "6": "0110",
    "7": "0111",
    "8": "1000",
    "9": "1001",
    "A": "1010",
    "B": "1011",
    "C": "1100",
    "D": "1101",
    "E": "1110",
    "F": "1111",
}


class Packet:
    def __init__(self, original_message, binary_message):
        self.original_message = original_message
        self.binary_message = binary_message
        self.pointer = 0

    def __consume_int(self, number_of_bits):
        bits = self.binary_message[self.pointer:self.pointer + number_of_bits]
        value = int(bits, 2)
        self.pointer += number_of_bits

        return value

    def parse_data(self):
        version = self.__consume_int(3)
        type_id = self.__consume_int(3)
        data = self.__consume_data(type_id)

        return {
            "version": version,
            "type_id": type_id,
            "data": data
        }

    def __consume_data(self, type_id):
        if type_id == 4:
            return self.__consume_literal_data()

        return self.__consume_operator_data()

    def __consume_literal_data(self):
        literal = 0
        consumed = 0b10000

        # while the consumed part starts with a 1
        while consumed & 0b10000:
            consumed = self.__consume_int(5)
            literal = (literal << 4) + (consumed & 0b1111)

        return literal

    def __consume_operator_data(self):
        length_type_id = self.__consume_int(1)

        if length_type_id == 0:
            return self.__consume_by_length(self.__consume_int(15))
        elif length_type_id == 1:
            return self.__consume_by_number(self.__consume_int(11))
        else:
            raise ValueError(f"Unknown length type id {length_type_id}")

    def __consume_by_length(self, length):
        final_pointer = self.pointer + length
        packets = []

        while self.pointer < final_pointer:
            packets.append(self.parse_data())

        return packets

    def __consume_by_number(self, number):
        packets = []

        for n_packet in range(number):
            packets.append(self.parse_data())

        return packets

    def sum_versions(self, data):
        version = data["version"]
        type_id = data["type_id"]
        subdata = data["data"]

        if type_id == 4:
            return version

        for inner in subdata:
            version += self.sum_versions(inner)

        return version


if __name__ == "__main__":
    for input_file in common.inputs:
        for line in common.read_file(input_file):
            binary_message = ""
            for character in line:
                binary_message += HEX_TO_BINARY[character]

            packet = Packet(line, binary_message)
            data = packet.parse_data()

            version_sum = packet.sum_versions(data)
            print(f"Version sum is {version_sum} for {input_file}")
