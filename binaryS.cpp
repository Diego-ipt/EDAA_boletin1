#include <iostream>
#include <fstream>
#include <vector>
#include <chrono>
#include <string>
#include <sstream>
#include <ctime>
#include "search/binary_search.cpp"

int main(int argc, char* argv[]) {
    if (argc != 3) {
        std::cerr << "Usage: " << argv[0] << " <file_name> <pair_position>" << std::endl;
        return 1;
    }
    
    std::string filename = argv[1];
    int pair_position = std::stoi(argv[2]);
    
    if (pair_position < 0 || pair_position >= 10) {
        std::cerr << "Error: pair_position must be between 0 and 9" << std::endl;
        return 1;
    }
    
    // Read the file
    std::ifstream file(filename);
    if (!file.is_open()) {
        std::cerr << "Error: Cannot open file " << filename << std::endl;
        return 1;
    }
    
    // Read first line with pairs
    std::string pairs_line;
    std::getline(file, pairs_line);
    
    // Parse pairs to extract the target value
    std::vector<std::pair<int, int>> pairs;
    std::stringstream ss(pairs_line);
    std::string pair_str;
    
    while (ss >> pair_str) {
        // Remove parentheses and split by comma
        if (pair_str[0] == '(') {
            pair_str = pair_str.substr(1, pair_str.length() - 2); // Remove ( and )
            size_t comma_pos = pair_str.find(',');
            int value = std::stoi(pair_str.substr(0, comma_pos));
            int expected_pos = std::stoi(pair_str.substr(comma_pos + 1));
            pairs.push_back({value, expected_pos});
        }
    }
    
    if (pair_position >= pairs.size()) {
        std::cerr << "Error: pair_position " << pair_position << " out of range" << std::endl;
        return 1;
    }
    
    int target_value = pairs[pair_position].first;
    int expected_position = pairs[pair_position].second;
    
    // Read array size
    int size;
    file >> size;
    
    // Read array data
    std::vector<int> data(size);
    for (int i = 0; i < size; i++) {
        file >> data[i];
    }
    file.close();
    
    // Perform binary search with timing using multiple iterations
    std::int64_t result = -1;
    const int iterations = 100000; // Multiple iterations for measurable time
    
    auto start = std::chrono::high_resolution_clock::now();
    for (int i = 0; i < iterations; i++) {
        result = binary_search(data.data(), size, target_value);
    }
    auto end = std::chrono::high_resolution_clock::now();
    
    // Calculate average time per operation in nanoseconds
    auto total_duration = std::chrono::duration_cast<std::chrono::nanoseconds>(end - start);
    long long average_time = total_duration.count() / iterations;
    
    // Output time
    std::cout << average_time << " " << result << std::endl;
    
    return 0;
}
