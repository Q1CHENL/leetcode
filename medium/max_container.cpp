#include <vector>
#include <valarray>
#include <set>
#include <iostream>

class max_container {
public:

// LeetCode solution, a lot faster:
// The intuition behind this approach is that the area formed between the
// lines will always be limited by the height of the shorter line. Further,
// the farther the lines, the more will be the area obtained.
//
// We take two pointers, one at the beginning and one at the end of the array
// constituting the length of the lines. Futher, we maintain a variable
// maxarea\text{maxarea}maxarea to store the maximum area obtained till now.
// At every step, we find out the area formed between them, update
// maxarea\text{maxarea}maxarea and move the pointer pointing to the shorter
// line towards the other end by one step.
    int maxArea(std::vector<int> &height) {
        int max_final = 0;
        int left = 0, right = height.size() - 1;
        while (left < right) {
            if (height.at(left) <= height.at(right)) {
                max_final = std::max(max_final, height.at(left) * (right - left));
                left++;
            } else {
                max_final = std::max(max_final, height.at(right) * (right - left));
                right--;
            }
        }
        return max_final;
    }
//    My original idea: find max for every height from the farthest edge
//    int maxArea(std::vector<int> &height) {
//        int max_final = 0;
//        int size = (int) height.size();
//        int half_size = size / 2;
//        bool odd = height.size() % 2;
//        for (int i = 0; i < size; ++i) {
//            int max = 0;
//            int curr = height.at(i);
//            if (curr == 0) continue;
//            int start_index = i < half_size ? (int) size - 1 : 0;
//            bool start_from_front = start_index == 0;
//            for (int j = start_index; j != (start_from_front ? size : 0); j += (start_from_front ? 1 : -1)) {
//                if (odd && i == half_size) continue;
//                if (height.at(j) < curr || i == j) continue;
//                max = std::abs(j - i) * curr;
//                break;
//            }
//            max_final = std::max(max_final, max);
//        }
//        int mid = size / 2;
//        //middle case for odd height count
//        if (odd && height.at(mid) != 0) {
//            //from begin
//            for (int j = 0; j < mid; ++j) {
//                if (height.at(j) < height.at(mid) || j == mid) continue;
//                max_final = std::max(max_final, std::abs(mid - j) * (height.at(mid)));
//                break;
//            }
//            //from behind
//            for (int j = size - 1; j > mid; --j) {
//                if (height.at(j) < height.at(mid) || j == mid) continue;
//                max_final = std::max(max_final, std::abs(mid - j) * (height.at(mid)));
//                break;
//            }
//        }
//        return max_final;
//    }
};




int main() {
    max_container mc;
    std::vector<int> vec;
    vec.emplace_back(10);
    vec.emplace_back(9);
    vec.emplace_back(8);
    vec.emplace_back(7);
    vec.emplace_back(6);
    vec.emplace_back(5);
    vec.emplace_back(4);
    vec.emplace_back(3);
    vec.emplace_back(2);
    vec.emplace_back(1);

    int max_area = mc.maxArea(vec);
    std::cout << "max area: " << max_area << std::endl;
}
