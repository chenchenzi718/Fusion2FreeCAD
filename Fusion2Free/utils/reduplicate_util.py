import pickle


def read_pkl(file_path):
    """
    读取指定路径的 pkl 文件并返回其内容。

    参数:
    file_path (str): pkl 文件的路径

    返回:
    object: 反序列化后的 Python 对象
    """
    try:
        with open(file_path, 'rb') as file:
            data = pickle.load(file)
        return data
    except FileNotFoundError:
        print(f"文件未找到: {file_path}")
    except pickle.UnpicklingError:
        print(f"无法反序列化文件: {file_path}")
    except Exception as e:
        print(f"读取文件时发生错误: {e}")


def get_filter_set(pkl_data):
    train_list = pkl_data['train']
    val_list = pkl_data['val']
    test_list = pkl_data['test']
    filter_set = set([index[:8] for index in train_list + val_list + test_list])
    return filter_set


def filter_id_set():
    pkl_file = r"D:\name_and_rebuild\Fusion2Free-master\deepcad_data_split_6bit.pkl"
    content = read_pkl(pkl_file)
    brep_gen_filter_set = get_filter_set(content)
    return brep_gen_filter_set


# 使用示例
if __name__ == "__main__":
    pkl_file = r"D:\name_and_rebuild\Fusion2Free-master\deepcad_data_split_6bit.pkl"
    content = read_pkl(pkl_file)
    if content is not None:
        print("pkl 文件内容:")
        print(content)
        filter_set = get_filter_set(content)
        # print(filter_set)
        # print(len(filter_set))
