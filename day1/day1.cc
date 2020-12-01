#include <unordered_set>
#include <iostream>
#include <vector>
#include <algorithm>

int main() {
    auto set = std::unordered_set<int>();
    auto v = std::vector<int>();

    int a;
    while (std::cin >> a) {
        v.push_back(a);
    }

    // part 1 O(n)
    for (int a : v) {
        int diff_2020 = 2020 - a;
        if (set.count(diff_2020)) {
            std::cout << "Part 1: " << a * diff_2020 << "\n";
        }
        set.insert(a);
    }

    // part 2 O(n^2)
    std::sort(v.begin(), v.end());
    // 2020 = sum = v[i] + v[j] + v[k]
    // lets assume i < j < k, v[i] <= v[j] <= v[k]
    for (unsigned i = 0; i < v.size() - 2; i++) {
        // we choose i-th element; the other 2 have to be in the i...end subarray
        int sum_2 = 2020 - v[i];
        set.clear();

        // basically part 1...
        for (unsigned j = i + 1; j < v.size(); j ++) {
            int diff_sum = sum_2 - v[j];
            if (set.count(diff_sum)) {
                std::cout << "Part 2: " << v[j] * diff_sum * v[i] << "\n";
                return 0;
            }
            set.insert(v[j]);
        }
    }
}

