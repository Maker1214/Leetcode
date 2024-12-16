nums = [1,2,3,4]

def check(nums,values,tempV,target):
    for i in range(len(nums)):        
        values |= set(tempV)
        tempV = [0]
        for j in values:
            print(f"第{i}回, values為{values}")
            v = nums[i] + j
            if v == target: return True
            tempV.append(v)
        
    return False




if sum(nums) % 2: print("False")
else: print("True") if check(nums,set(),[0],sum(nums) // 2) else print("check False")












