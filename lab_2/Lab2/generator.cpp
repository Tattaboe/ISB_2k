#include <iostream>
#include <random>

std::string generate_random_shuffle() {
    std::random_device rd;
    std::shuffle_order_engine<std::mt19937, 2> gen(rd());

    std::string result;
    for (int i = 0; i < 128; ++i) {
        result += std::to_string(gen() % 2);
    }

    return result;
}

int main() {
    std::string randomBits = generate_random_shuffle();
    std::cout << randomBits << std::endl;

    return 0;
}