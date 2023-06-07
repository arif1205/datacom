#include <iostream>
#include <vector>

using namespace std;

// Function to calculate the checksum codeword
uint8_t calculateChecksum(const vector<uint8_t> &numbers)
{
  uint16_t sum = 0;

  // Calculate the sum of all numbers
  for (uint8_t number : numbers)
  {
    sum += number;
  }

  // Take the 8 least significant bits of the sum
  uint8_t checksum = sum & 0xFF;

  // Invert the checksum
  checksum = ~checksum;

  return checksum;
}

int main()
{
  // List of five 8-bit numbers
  vector<uint8_t> numbers = {0x12, 0x34, 0x56, 0x78, 0x9A};

  // Calculate the checksum codeword
  uint8_t checksum = calculateChecksum(numbers);

  // Output the checksum
  cout << "Checksum: 0x" << hex << uppercase << static_cast<int>(checksum) << endl;

  return 0;
}