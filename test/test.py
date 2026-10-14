di_reg = 0b101  # 模拟DI0、DI2点位导通
do_reg = 0

# 逻辑：DI0触发且DI2限位未触发，则DO0输出电机运行
if (di_reg >> 0) & 1 and not (di_reg >> 2) & 1:
    do_reg |= 1 << 0

print(f"DI状态: {bin(di_reg)}, DO输出: {bin(do_reg)}")
