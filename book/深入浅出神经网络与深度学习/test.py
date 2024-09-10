import random
import matplotlib.pyplot as plt

def coin_flip(min_flips, max_flips):
    # 参数表示抛掷硬币次数大小,min表⽰最少抛掷次数,max表⽰最多抛掷次数
    ratios = []
    # range(min, max+1) 储存的是min到max的自然数。因此，此处为max+1
    x = range(min_flips, max_flips + 1)
    # 记录每一批次抛掷的结果。例如，第一批次抛掷硬币是抛min次，查看硬币正反面结果
    for number_Flips in x:
        numHeads = 0  # 初始化，硬币正面朝上的计数为0
        for n in range(number_Flips):
            if random.random() < 0.5:  # random.random()从[0, 1)随机取出一个数
                numHeads += 1  # 当随机取出的数小于0.5时，正面朝上的计数加1
        numTails = number_Flips - numHeads  # 用本次试验总抛掷次数减去正面朝上次数就是本次试验中反面朝上次数
        ratios.append(numHeads / float(numTails))  # 正反面计数的比值

    plt.title('Heads/Tails Ratios')
    plt.xlabel('Number of Flips')
    plt.ylabel('Heads/Tails')
    plt.plot(x, ratios)
    plt.hlines(1, 0, x[-1], linestyles='dashed', colors='y')
    plt.show()

coin_flip(2, 10000)