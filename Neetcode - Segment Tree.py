class SegmentTree:
    def __init__(self, nums):
        """
        初始化线段树
        :param nums: 输入数组
        """
        self.n = len(nums)
        self.tree = [0] * (4 * self.n)  # 线段树的存储空间通常是 4 倍数组大小
        self.build(0, 0, self.n - 1, nums)

    def build(self, node, start, end, nums):
        """
        递归构建线段树
        :param node: 当前树节点索引
        :param start: 当前节点覆盖的区间起点
        :param end: 当前节点覆盖的区间终点
        :param nums: 输入数组
        """
        if start == end:  # 叶子节点
            self.tree[node] = nums[start]
            print(f"node is {node}, self.tree[node] is {nums[start]}, start is {start} , end is {end}")
        else:
            mid = (start + end) // 2
            left_child = 2 * node + 1
            right_child = 2 * node + 2
            self.build(left_child, start, mid, nums)  # 左子树
            self.build(right_child, mid + 1, end, nums)  # 右子树
            self.tree[node] = self.tree[left_child] + self.tree[right_child]  # 根据需求修改（如求和）
            print(f"node is {node}, self.tree[node] is {self.tree[node]}, left_child is {left_child} , right_child is {right_child}")


    def query(self, node, start, end, l, r):
        """
        区间查询
        :param node: 当前树节点索引
        :param start: 当前节点覆盖的区间起点
        :param end: 当前节点覆盖的区间终点
        :param l: 查询区间的起点
        :param r: 查询区间的终点
        :return: 查询结果
        """
        if r < start or l > end:  # 完全不相交
            return 0  # 根据需求修改（如区间最小值可返回 float('inf')）
        if l <= start and end <= r:  # 完全包含
            return self.tree[node]
        # 部分重叠
        mid = (start + end) // 2
        left_child = 2 * node + 1
        right_child = 2 * node + 2
        left_sum = self.query(left_child, start, mid, l, r)
        right_sum = self.query(right_child, mid + 1, end, l, r)
        return left_sum + right_sum  # 根据需求修改

    def update(self, node, start, end, idx, value):
        """
        单点更新
        :param node: 当前树节点索引
        :param start: 当前节点覆盖的区间起点
        :param end: 当前节点覆盖的区间终点
        :param idx: 需要更新的索引
        :param value: 更新值
        """
        if start == end:  # 叶子节点
            self.tree[node] = value
        else:
            mid = (start + end) // 2
            left_child = 2 * node + 1
            right_child = 2 * node + 2
            if start <= idx <= mid:  # 更新在左子树
                self.update(left_child, start, mid, idx, value)
            else:  # 更新在右子树
                self.update(right_child, mid + 1, end, idx, value)
            self.tree[node] = self.tree[left_child] + self.tree[right_child]  # 根据需求修改

    def range_query(self, l, r):
        """
        对外的区间查询接口
        """
        return self.query(0, 0, self.n - 1, l, r)

    def point_update(self, idx, value):
        """
        对外的单点更新接口
        """
        self.update(0, 0, self.n - 1, idx, value)

nums = [9,7,2,8,3]
obj = SegmentTree(nums)
obj.build(0,0,len(nums) - 1, nums)
print(obj.tree)
