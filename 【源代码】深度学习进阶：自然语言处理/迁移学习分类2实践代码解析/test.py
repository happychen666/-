import pandas as pd
from collections import Counter
from functools import reduce
from sklearn.utils import shuffle
import torch

def data_loader(train_data_path, valid_data_path, batch_size):
    """
    从文件中加载数据，准备训练和验证数据的生成器，并确保验证集有足够的数据满足批次要求。

    :param train_data_path: 训练数据文件路径
    :param valid_data_path: 验证数据文件路径
    :param batch_size: 每批数据的大小
    :return: 训练数据生成器，验证数据生成器，训练数据样本数，验证数据样本数
    """
    
    # 加载训练和验证数据，不包含标题行
    train_data = pd.read_csv(train_data_path, header=None, sep="\t").drop([0])
    valid_data = pd.read_csv(valid_data_path, header=None, sep="\t").drop([0])
    
    # 打印训练集和验证集中正负样本的数量
    print("训练数据集的类别分布:")
    print(dict(Counter(train_data[1].values)))
    print("验证数据集的类别分布:")
    print(dict(Counter(valid_data[1].values)))
    
    # 确保验证集数据量大于等于一个批次的大小
    if len(valid_data) < batch_size:
        raise ValueError("批次大小或数据分割不匹配！")
    
    # 定义生成器函数，返回数据的每个批次
    def _loader_generator(data):
        """
        数据批次生成器函数，针对训练或验证数据进行批次处理。

        :param data: 训练或验证数据
        :yield: 每批数据和对应标签的生成器
        """
        
        for batch in range(0, len(data), batch_size):
            # 初始化列表存储每个批次的编码数据和标签
            batch_encoded = []
            batch_labels = []
            
            # 打乱数据顺序并获取一个批次
            for item in shuffle(data.values.tolist())[batch: batch + batch_size]:
                # 使用 BERT 模型对数据进行编码（假设 `get_bert_encode` 函数已定义）
                encoded = get_bert_encode(item[0])
                
                # 将编码数据和标签分别添加到列表
                batch_encoded.append(encoded)
                batch_labels.append([int(item[1])])
            
            # 将列表转换为模型所需的张量格式
            encoded = reduce(lambda x, y: torch.cat((x, y), dim=0), batch_encoded)
            labels = torch.tensor(reduce(lambda x, y: x + y, batch_labels))
            
            # 生成编码数据和标签元组
            yield (encoded, labels)
    
    # 返回训练和验证集的生成器以及样本数量
    return (
        _loader_generator(train_data), 
        _loader_generator(valid_data), 
        len(train_data), 
        len(valid_data)
    )
