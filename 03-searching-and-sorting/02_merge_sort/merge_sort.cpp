/**
 * Problem: Merge Sort
 * 
 * Time Complexity: O(N log N)
 * Space Complexity: O(N)
 */

#include <iostream>
#include <vector>

void merge(std::vector<int>& arr, int left, int mid, int right) {
    std::vector<int> temp;
    int i = left, j = mid + 1;

    while (i <= mid && j <= right) {
        if (arr[i] <= arr[j]) {
            temp.push_back(arr[i++]);
        } else {
            temp.push_back(arr[j++]);
        }
    }
    while (i <= mid) temp.push_back(arr[i++]);
    while (j <= right) temp.push_back(arr[j++]);

    for (int k = 0; k < static_cast<int>(temp.size()); ++k) {
        arr[left + k] = temp[k];
    }
}

void mergeSort(std::vector<int>& arr, int left, int right) {
    if (left >= right) return;
    int mid = left + (right - left) / 2;
    mergeSort(arr, left, mid);
    mergeSort(arr, mid + 1, right);
    merge(arr, left, mid, right);
}

int main() {
    std::cout << "[C++] Merge Sort Test\n";
    std::vector<int> arr = {64, 25, 12, 22, 11};
    mergeSort(arr, 0, arr.size() - 1);

    std::cout << "Sorted array: ";
    for (int x : arr) std::cout << x << " ";
    std::cout << "\n";
    return 0;
}
