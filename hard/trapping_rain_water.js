/**
 * @param {number[]} height
 * @return {number}
 */
var trap = function (height) {
    let ret = 0
    let l = 0, r = height.length - 1
    // lMax: highest bar from the left side
    // rMax: highest bar from the right side
    // These are updated dynamically
    //
    // Basic idea: 2 pointers, one from left, one from right 
    //
    // General clarification:
    // The potential amount of trapped water (lMax - height[l] or rMax - height[r])
    // becomes actual trapped water because the presence of a higher bar on the other
    // side ensures that the water at that level cannot flow further. Even though the
    // water might not physically touch that higher bar (as it might be trapped by a
    // different section of the terrain), the presence of the higher bar guarantees that
    // the water level can rise up to that height, effectively realizing the potential
    // and making it actual trapped water.
    //
    // Simple example:
    //                                                        |
    //          | ~                                           |   
    //          | ~    (whatever structure in the middle)     | |
    //          | | ... ... ... ... ... ... ... ... ... ... ..| |
    //            l                                           r
    // height[l] == 1, lMax = 3, left potential == 3 - 1 = 2
    // height[r] == 4, rMax = 4, right potential == 4 - 4 = 0 
    // -> only realized when a higher bar appears on the left (height[l] > height[r])
    //
    // the water in the example is garenteed to be trapped

    let lMax = 0, rMax = 0
    while (l < r) {
        lMax = Math.max(lMax, height[l])
        rMax = Math.max(rMax, height[r])
        if (height[l] < height[r]) {
            ret += lMax - height[l]
            l++
        } else {
            ret += rMax - height[r]
            --r
        }
    }
    return ret
};

// Test case 1
let height1 = [0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1];
let result1 = trap(height1);
console.log("Test case 1 result:", result1); // Expected output: 6

// Test case 2
let height2 = [4, 2, 0, 3, 2, 5];
let result2 = trap(height2);
console.log("Test case 2 result:", result2); // Expected output: 9