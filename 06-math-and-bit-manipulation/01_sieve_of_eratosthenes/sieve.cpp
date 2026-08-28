/**
 * Problem: Sieve of Eratosthenes
 * 
 * Time Complexity: O(N log log N)
 * Space Complexity: O(N)
 */

#include <iostream>
#include <vector>

std::vector<int> sieve(int n) {
    std::vector<bool> isPrime(n + 1, true);
    isPrime[0] = isPrime[1] = false;

    for (int p = 2; p * p <= n; ++p) {
        if (isPrime[p]) {
            for (int i = p * p; i <= n; i += p) {
                isPrime[i] = false;
            }
        }
    }

    std::vector<int> primes;
    for (int i = 2; i <= n; ++i) {
        if (isPrime[i]) primes.push_back(i);
    }
    return primes;
}

int main() {
    std::cout << "[C++] Sieve Test\n";
    std::vector<int> primes = sieve(30);
    std::cout << "Primes up to 30: ";
    for (int p : primes) std::cout << p << " ";
    std::cout << "\n";
    return 0;
}
