// For example: let nums = [5, 7, 7, 8, 8, 10];
// binarySearch will find the second 8
// helperSearch will search the left boundary in [5, 7, 7, 8, 8] and right boundary in [8, 10] 
function searchRange(nums: number[], target: number): number[] {
    let midIndex = binarySearch(nums, target)
    if (midIndex == -1) {
        return [-1, -1]
    }
    let leftBound = helperSearch(nums.slice(0, midIndex + 1), target, true)
    let rightBound = helperSearch(nums.slice(midIndex, nums.length), target, false)
    let start = leftBound
    let end = midIndex + rightBound
    return [start, end]
};

function binarySearch(nums: number[], target: number): number {
    let left = 0
    let right = nums.length - 1
    let mid = Math.floor((right - left) / 2)
    while (left <= right) {
        if (nums[mid] == target) {
            return mid
        } else if (nums[mid] < target) {
            left = mid + 1
        } else {
            right = mid - 1
        }
        mid = Math.floor((right + left) / 2)
    }
    return -1
};

function helperSearch(nums: number[], target: number, toLeft: boolean): number {
    if (nums.length == 1) return 0
    let l = 0
    let r = nums.length - 1
    let mid = Math.floor((r + l) / 2)
    while (l < r) {
        if (nums[mid] == target) {
            if (toLeft) {
                if (mid - 1 >= 0 && nums[mid - 1] != target || mid - 1 < 0) {
                    return mid
                }
                r = mid - 1
            } else {
                if (mid + 1 <= nums.length - 1 && nums[mid + 1] != target || mid + 1 > nums.length - 1 ) {
                    return mid
                }
                l = mid + 1
            }
        } else {
            if (toLeft) {
                l = mid + 1
            } else {
                r = mid - 1
            }
        }
        mid = Math.floor((r + l) / 2)
    }
    return mid
}

let nums = [5, 7, 7, 8, 8, 10];
let nums1 = [2, 2]
let nums2 = [1]
let target = 1;

let ret = searchRange(nums2, target)
console.log(ret)
