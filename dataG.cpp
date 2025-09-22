#include <iostream>
#include <fstream>
#include <vector>
#include <algorithm>
#include <random>
#include <direct.h>  // For _mkdir on Windows
#include <string>    // For std::to_string

int main() {
    // Create data directory if it doesn't exist
    _mkdir("data");
    
    std::random_device rd;
    std::mt19937 gen(rd());
    
    // Generate files for size experiment (powers of 2 from 2^10 to 2^20)
    std::vector<int> sizes = {1024, 2048, 4096, 8192, 16384, 32768, 65536, 131072, 262144, 524288, 1048576};
    
    for (int size : sizes) {
        std::vector<int> data(size);
        std::uniform_int_distribution<> dis(1, size * 10);
        
        // Generate random data
        for (int i = 0; i < size; i++) {
            data[i] = dis(gen);
        }
        
        // Sort the data for binary search
        std::sort(data.begin(), data.end());
        
        // Generate 10 search pairs (dato, posicion)
        std::vector<std::pair<int, int>> search_pairs;
        
        // Add 7 existing elements from random positions within each decile
        int num_elements = std::min(7, size); // Don't try to get more elements than array size
        
        for (int i = 0; i < num_elements; i++) {
            int decile_start = (i * size) / num_elements;
            int decile_end = ((i + 1) * size) / num_elements;
            if (i == num_elements - 1) decile_end = size; // Last segment goes to end
            
            // Random position within this segment
            std::uniform_int_distribution<> segment_dis(decile_start, std::max(decile_start, decile_end - 1));
            int random_index = segment_dis(gen);
            
            // Ensure we don't go out of bounds
            if (random_index >= size) random_index = size - 1;
            
            search_pairs.push_back({data[random_index], random_index});
        }
        
        // Add 3 non-existing elements (position = -1)
        std::uniform_int_distribution<> search_dis(size * 10 + 1, size * 15);
        for (int i = 0; i < 3; i++) {
            int non_existing = search_dis(gen);
            search_pairs.push_back({non_existing, -1});
        }
        
        // Write to file in data folder
        std::string filename = "data/data_size_" + std::to_string(size) + ".txt";
        std::ofstream file(filename);
        
        // First line: 10 pairs (dato, posicion)
        for (const auto& pair : search_pairs) {
            file << "(" << pair.first << "," << pair.second << ") ";
        }
        file << std::endl;
        
        // Second line: array size
        file << size << std::endl;
        
        // Third line: sorted array data
        for (int val : data) {
            file << val << " ";
        }
        file << std::endl;
        file.close();
        
        std::cout << "Generated " << filename << std::endl;
    }
    
    return 0;
}
