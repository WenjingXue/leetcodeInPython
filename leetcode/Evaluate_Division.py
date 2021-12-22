class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        node_group_weight = {}
        
        def find(node_id):
            if node_id not in node_group_weight:
                ## for the node which is not recorded, the root node is the node itself, the weight is 1
                node_group_weight[node_id] = (node_id,1)
            group_id, node_weight = node_group_weight[node_id]
            if group_id != node_id:
                new_group_id, group_weight = find(group_id)
                node_group_weight[node_id] = (new_group_id, group_weight * node_weight)
            return node_group_weight[node_id]
        
        def union(dividend, divisor, value):
            dividend_group_id, dividend_weight = find(dividend)
            divisor_group_id, divisor_weight = find(divisor)
            if dividend_group_id !=divisor_group_id:
                node_group_weight[dividend_group_id] = (divisor_group_id, divisor_weight * value / dividend_weight)
                
        for (dividend, divisor),value in zip(equations,values):
            union(dividend, divisor, value)
            
        res = []
        for (dividend, divisor) in queries:
            if dividend not in node_group_weight or divisor not in node_group_weight:
                res.append(-1.0)
            else:
                dividend_group, dividend_weight = find(dividend)
                divisor_group, divisor_weight = find(divisor)
                if dividend_group != divisor_group:
                    res.append(-1.0)
                else:
                    res.append(dividend_weight/divisor_weight)
        return res
